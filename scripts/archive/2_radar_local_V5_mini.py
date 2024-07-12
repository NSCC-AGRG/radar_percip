#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import os
import numpy as N

def GIFcount(GIFdir):
    GIFs = 0
    GIFsnull = 0
    for fn in os.listdir(GIFdir):
        if os.path.getsize(GIFdir+fn)/1024 < 3:
            GIFsnull += 1
        GIFs += 1
    return GIFs,GIFsnull

print GIFcount('D:/radar_percip/GIF/XGO/')
print GIFcount('D:/radar_percip/GIF/XMB/')
print GIFcount('D:/radar_percip/GIF/XNC/')
