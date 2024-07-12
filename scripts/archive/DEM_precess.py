#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import urllib, time, re, Image, os
import numpy as N

a = Image.open('D:/radar_percip/temp/1km_fill1.tif')
print a
##a = N.array(N.asarray(a))
##print a

b = N.array(a.getdata()).reshape(a.size[::-1])
print b

f2 = Image.fromarray(N.array(N.clip(b,0,255),'uint8'))
f2.save('D:/radar_percip/temp/1km_fill1.gif')
