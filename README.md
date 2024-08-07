# RADAR PERCIP DOWNLOADER

welcome to the wonderful world of radar percipitation. Every radar has a [story](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/radar-story.html).

## Radar Products Avilable:

### CAPPI (Constant Altitude Plan Position Indicator)  
The main advantage of CAPPI is its ability to provide a consistent altitude representation of precipitation over a large area. However, it can be contaminated by non-meteorological artifacts like trees and buildings due to the lack of Doppler processing.

### DPQPE (Dual-Pol Quantitative Precipitation Estimation) 
The primary benefit of DPQPE is its high accuracy in estimating precipitation rates close to the ground using dual-polarization techniques. Its main limitation is the effective range of 240 km, which may not fully cover very large weather systems.

[more info](https://www.canada.ca/en/environment-climate-change/services/weather-general-tools-resources/radar-overview/about.html)

## Annapolis Valley FLood Event - July 11, 2024
![image](/data/radar/CAPPI/GIF/CASGO/202407111830_CASGO_CAPPI_1.5_RAIN.gif)

full catalog available: [CASCM](/data/radar/CAPPI/GIF/CASCM), [CASGO](/data/radar/CAPPI/GIF/CASGO), [CASMB](/data/radar/CAPPI/GIF/CASMB), 

## Guide

Here you can download canada radar gifs. The radar station is the name of the radar facility, which can be found in the [radar catalog](https://climate.weather.gc.ca/radar/index_e.html).

### Maritime Radar Station IDs:

|Station ID | Location|
|-|-|
|CASCM | Chipman, NB|
|CASGO | Halifax, NS|
|CASMB | Sydney, NS|

### Rainfall Events in the Maritimes 

- Nov 22-23, 2021 [wikipedia](https://en.wikipedia.org/wiki/November_2021_Atlantic_Canada_floods)
- July 21-22, 2023 [wikipedia](https://en.wikipedia.org/wiki/2023_Nova_Scotia_floods#cite_note-1)
- July 11, 2024  [wikipedia](https://en.wikipedia.org/wiki/Hurricane_Beryl)

### scripts\gif_downloader.py
will download all gif files for a given time range and list of radar stations and save them in a folder called "data"

### scripts\archive
contains old versions of radar percipitation processing scripts, mainly for reference purposes.

## References

### Historical Radar Data, Gifs
- https://climate.weather.gc.ca/radar/ (interactive)
- https://dd.weather.gc.ca/radar/ (raw)

### ECCC Data info
- https://eccc-msc.github.io/open-data/msc-data/obs_radar/readme_radarimage-datamart_en/
- https://eccc-msc.github.io/open-data/usage/readme_en/#how-to-access-raw-data
- https://eccc-msc.github.io/open-data/msc-geomet/readme_en/

### US Data
- https://www.ncdc.noaa.gov/wct/data.php
- https://thredds.ucar.edu/thredds/catalog/catalog.html

### Global Radar
- https://wrd.mgm.gov.tr/Home/Wrd
- https://wrd.mgm.gov.tr/Radar/Details/YXpNMXRuTVJxQ2FsM1Rta3NwaVVaZz09

# Other sources etc..
- https://en.wikipedia.org/wiki/Nowcasting_(meteorology)
 - https://www.radar.mcgill.ca/imagery/nowcasting.html
- https://www.rainviewer.com/weather-radar-map-live.html
 - https://zoom.earth/maps/radar/#view=45.2029,-62.9264,7z/date=2024-07-19,15:07,-3 (uses rainviewer.com radar api)
 - https://www.ventusky.com/?p=42.33;-60.94;6&l=radar
 - https://weather.com/en-CA/weather/radar/interactive/l/584018bec07ce9573837c14fa59da031fa6fcdeb1c3c9e3b2b27cb79ce254b5a
 - https://www.wunderground.com/wundermap?lat=56.130&lon=-106.346&zoom=4&radar=1&wxstn=0 (uses weather.com radar api)
 - https://mesonet.agron.iastate.edu/current/radar.phtml
 - https://www.ncei.noaa.gov/maps/radar/ (uses radar layers from iastate)
 - https://www.meteoblue.com/en/weather/maps#coords=4.87/37.73/-78.5&map=radar~radarMap~none~none~none
 - https://gpm.nasa.gov/



