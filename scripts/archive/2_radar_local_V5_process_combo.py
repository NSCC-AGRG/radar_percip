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
out_dir = 'D:/radar_percip/NPY/COMBO/'
################################################################
start_time = time.mktime(start_date)-4*3600
end_time = time.mktime(end_date)-3*3600
at_time = start_time

for at_time in range(start_time,end_time,3600):
    x=time.gmtime(at_time)
    name=str(x.tm_year)+("","0")[int(x.tm_mon)<10]+str(x.tm_mon)+("","0")[int(x.tm_mday)<10]+str(x.tm_mday)+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)

    xgo = Image.open('D:/radar_percip/GIF/XGO/'+"xgo"+name+'.gif')
    xnc = Image.open('D:/radar_percip/GIF/XNC/'+"xnc"+name+'.gif')
    xmb = Image.open('D:/radar_percip/GIF/XMB/'+"xmb"+name+'.gif')
    xgo = N.array(N.asarray(xgo))
    xnc = N.array(N.asarray(xnc))
    xmb = N.array(N.asarray(xmb))

    t1= time.time()

    xnc1 = xnc[125:480,157:580]
    xgo[0:xnc1.shape[0],0:xnc1.shape[1]] = xnc1 + xgo[0:xnc1.shape[0],0:xnc1.shape[1]]

    xmb1 = xmb[95:480,0:306]
    xgo[0:xmb1.shape[0],xgo.shape[1]-xmb1.shape[1]:xgo.shape[1]] = xmb1 + xgo[0:xmb1.shape[0],xgo.shape[1]-xmb1.shape[1]:xgo.shape[1]]

    combo = xgo 

    N.save(out_dir+name, combo)
    f2 = Image.fromarray(N.array(N.clip(combo,0,255),'uint8'))
    #f2 = Image.fromarray(d)
    f2.save(out_dir+name+"combo.gif")
    print time.time()-t1
