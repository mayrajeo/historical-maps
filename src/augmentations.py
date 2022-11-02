from __future__ import annotations
from fastai.data.all import *
from fastai.vision.core import *
from fastai.vision.data import *
from fastai.vision.augment import *

__all__ = ['cutout_constant', 'RandomErasingSeg']

def _slice(area, sz):
    bound = int(round(math.sqrt(area)))
    loc = random.randint(0, max(sz-bound, 0))
    return loc,loc+bound

def cutout_constant(
    x:Tensor, # Input mask
    areas:list, # list of aras to cutout. Order rl, rh, cl, ch
    fillvalue:int=0 # Value to fill the areas with, default 0 
):
    "Replace all `areas`in `x` with constant `fillvalue`"
    chan,img_h,img_w = x.shape[-3:]
    for rl,rh,cl,ch in areas: x[...,rl:rh,cl:ch] = 0
    return x

class RandomErasingSeg(RandTransform):
    "Randomly selects a rectangle region in an image and randomizes its pixels. Mask pixels are replaced with 0"
    order = 100 # After Normalize
    def __init__(self,
        p:float=0.5, # Probability of applying Random Erasing
        sl:float=0., # Minimum proportion of erased area
        sh:float=0.3, # Maximum proportion of erased area
        min_aspect:float=0.3, # Minimum aspect ratio of erased area
        max_count:int=1, # Maximum number of erasing blocks per image, area per box is scaled by count
        erasing_mode:str='gaussian' # Type of erasing, either 'gaussian' or 'constant'
    ):
        store_attr()
        super().__init__(p=p)
        self.log_ratio = (math.log(min_aspect), math.log(1/min_aspect))
    
    def _bounds(self, area, img_h, img_w):
        r_area = random.uniform(self.sl,self.sh) * area
        aspect = math.exp(random.uniform(*self.log_ratio))
        return _slice(r_area*aspect, img_h) + _slice(r_area/aspect, img_w)
    
    def before_call(self,
        b,
        split_idx
    ):
        self.do = True
        img_h, img_w = fastuple((b[0] if isinstance(b, tuple) else b).shape[-2:])
        count = random.randint(1, self.max_count)
        area = img_h*img_w/count
        self.areas = [self._bounds(area, img_h, img_w) for _ in range(count)]
    
    def encodes(self,x:TensorImage):
        if self.erasing_mode == 'gaussian': return cutout_gaussian(x, self.areas)
        elif self.erasing_mode == 'constant': return cutout_constant(x, self.areas)
        else: return cutout_gaussian(x, self.areas) # default to gaussian
    
    def encodes(self, x:TensorMask): 
        return cutout_constant(x, self.areas)