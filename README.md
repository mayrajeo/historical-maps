# Utilizing historical maps in identification of long-term land use changes

## Abstract

> Knowledge in the magnitude and historical trends in land use and land cover is needed to understand the changing status of the key elements of the landscape and to better target management efforts. However, this information is not easily available before the start of satellite campaign missions. Scanned historical maps are a valuable but underused source of land use and land cover information. As a case study, we used U-Net to automatically extract fields, mires, roads, waterways and water bodies from scanned historical maps dated 1965, 1984 and 1985 for our 900 km² study area in Southern Finland. We then used these data, along with the topographic databases from 2005 and 2022 to quantify the LULC changes for the past 57 years. For example, the total area of fields decreased by around 27 km² and the total length of watercourses increased by around 2250 km in our study area.

## Data used

<img src='nb_figures/area_map.jpeg' width='700'>

The study area is located in the vicinity of Evo, Finland, and consists of 9 map sheets. From each map sheet, we have two different historical scanned maps, older from 1965 and newer from either 1984 or 1985. The maps were provided by [National Land Survey of Finland](https://www.maanmittauslaitos.fi/en/e-services/old-printed-maps), and the ground control points for each individual map were acquired from [vanhatkartat.fi](https://vanhatkartat.fi) by Shingle Oy. Reference data from 2005 and 2022 is based on topographic database by NLS Finland, and it can be acquired for instance from [Paituli download service](https://paituli.csc.fi/download.html).

## Getting started

Much of the work relies heavily on https://github.com/jaeeolma/drone_detector, and instructions for its installation work here also.

## Authors

* Janne Mäyrä (coresponding author), Finnish Environment Institute SYKE
* Sonja Kivinen, University of Eastern Finland
* Sarita Keski-Saari, University of Eastern Finland
* Laura Poikolainen, University of Eastern Finland
* Timo Kumpula, University of Eastern Finland

This work is a part of [IBC-CARBON](https://www.ibccarbon.fi/en-US) WP4.