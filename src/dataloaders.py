from fastai.vision.data import *
from fastai.vision.core import *
from fastai.data.all import *

class SegmentationDataLoadersFix(DataLoaders):
    "Basic wrapper around several `DataLoader`s with factory methods for segmentation problems"
    @classmethod
    @delegates(DataLoaders.from_dblock)
    def from_label_func(cls, path, fnames, label_func, valid_pct=0.2, seed=None, codes=None, item_tfms=None, batch_tfms=None, 
                        img_cls=PILImage,val_fnames=None,**kwargs):
        "Create from list of `fnames` in `path`s with `label_func`."
        dblock = DataBlock(blocks=(ImageBlock(img_cls), MaskBlock(codes=codes)),
                           splitter=FuncSplitter(lambda o: o.name in val_fnames) if val_fnames else RandomSplitter(valid_pct, seed=seed),
                           get_y=label_func,
                           item_tfms=item_tfms,
                           batch_tfms=batch_tfms)
        res = cls.from_dblock(dblock, fnames, path=path, **kwargs)
        return res