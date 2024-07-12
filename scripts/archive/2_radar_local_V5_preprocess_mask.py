#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import urllib, time, re, Image, os
import numpy as N

#set the start and end date (YYYY MM DD HH)
#will auto increment by 1 hour

######################### CHANGE ###############################
site="XGO" # ie, XNC = NB, XGO = NS, XMB = CB
scale="RAIN" # SNOW or RAIN
start_date = time.strptime("2008 11 11 11 UTC", "%Y %m %d %H %Z")
end_date = time.strptime("2008 11 11 11 UTC", "%Y %m %d %H %Z")
in_dir = 'D:/radar_percip/GIF/XGO/'
out_dir = 'D:/radar_percip/'
################################################################
start_time = time.mktime(start_date)-4*3600
end_time = time.mktime(end_date)-3*3600
at_time = start_time

for at_time in range(start_time,end_time,3600):
    x=time.gmtime(at_time)
    name=str(x.tm_year)+("","0")[int(x.tm_mon)<10]+str(x.tm_mon)+("","0")[int(x.tm_mday)<10]+str(x.tm_mday)+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)

    h = Image.open(in_dir+site+name+'.gif')
    a = N.array(N.asarray(h))

    t1= time.time()

    c = a[193][525]
    d = N.where(a==c,0,255)
    d = d[0:480,0:480]

    N.save(out_dir+"GIFmask", d)
    f2 = Image.fromarray(N.array(N.clip(d,0,255),'uint8'))
    #f2 = Image.fromarray(d)
    f2.save(out_dir+"GIFmask.gif")
    print time.time()-t1
    break
