#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import urllib, time, re, Image, os
import numpy as N

#set the start and end date (YYYY MM DD HH)
#will auto increment by 1 hour

######################### CHANGE ###############################
site="XGO" # ie, XNC = NB, XGO = NS, XMB = CB
scale="RAIN" # SNOW or RAIN
start_date = time.strptime("2011 11 11 11 UTC", "%Y %m %d %H %Z")
end_date = time.strptime("2011 11 11 15 UTC", "%Y %m %d %H %Z")
in_dir = 'D:/radar_percip/GIF/XGO/'
out_dir = 'D:/radar_percip/NPY/COMBO/'
################################################################

def radgif2npy(a):
    
    c = a[240][240]
    for (x,y), value in N.ndenumerate(a):
        #if (a[x,y]==4 or a[x,y]==3 or a[x,y]==c):
        if (a[x,y]==c or a[x,y]==4):
            b = a[cmp(0,x)+x:x+2, cmp(0,y)+y:y+2]
            b=b.flatten()
            b=b[b != 4]
            #b=b[b != 3]
            b=b[b != c]
            counts = N.bincount(b)
            a[x,y] = N.argmax(counts)

    summer_mm = {a[151][525]:200, \
         a[165][525]:143, \
         a[179][525]:101, \
         a[193][525]:70, \
         a[207][525]:49, \
         a[221][525]:34, \
         a[235][525]:24, \
         a[249][525]:17, \
         a[263][525]:12, \
         a[277][525]:8, \
         a[291][525]:4, \
         a[305][525]:3, \
         a[319][525]:2, \
         a[333][525]:1}

    d = a*0
    
    for k, v in summer_mm.iteritems():
        d[a==k] = v

    return d

################################################################

start_time = time.mktime(start_date)-4*3600
end_time = time.mktime(end_date)-3*3600
at_time = start_time

for at_time in range(start_time,end_time,3600):
    x=time.gmtime(at_time)
    name=str(x.tm_year)+("","0")[int(x.tm_mon)<10]+str(x.tm_mon)+("","0")[int(x.tm_mday)<10]+str(x.tm_mday)+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)

    t1= time.time()

    xgo = Image.open('D:/radar_percip/GIF/XGO/'+"xgo"+name+'.gif')
    xnc = Image.open('D:/radar_percip/GIF/XNC/'+"xnc"+name+'.gif')
    xmb = Image.open('D:/radar_percip/GIF/XMB/'+"xmb"+name+'.gif')
    xgo = N.array(N.asarray(xgo))
    xnc = N.array(N.asarray(xnc))
    xmb = N.array(N.asarray(xmb))
    xgo = radgif2npy(xgo)
    xnc = radgif2npy(xnc)
    xmb = radgif2npy(xmb)

    xnc1 = xnc[125:480,157:580]
    xgo[0:xnc1.shape[0],0:xnc1.shape[1]][xnc1!=0] = (xnc1[xnc1!=0]+xgo[0:xnc1.shape[0],0:xnc1.shape[1]][xnc1!=0])/2
    #currently averages where non 0, should be taking max probably. 
    #xgo[0:xnc1.shape[0],0:xnc1.shape[1]][xnc1!=0] = xnc1[xnc1!=0]


    xmb1 = xmb[95:480,0:306]
    xgo[0:xmb1.shape[0],xgo.shape[1]-xmb1.shape[1]:xgo.shape[1]][xmb1!=0] = (xmb1[xmb1!=0] +xgo[0:xmb1.shape[0],xgo.shape[1]-xmb1.shape[1]:xgo.shape[1]][xmb1!=0])/2
    #xgo[0:xmb1.shape[0],xgo.shape[1]-xmb1.shape[1]:xgo.shape[1]][xmb1!=0] = xmb1[xmb1!=0]

    combo = xgo *20

    N.save(out_dir+name, combo)
    f2 = Image.fromarray(N.array(N.clip(combo,0,255),'uint8'))
    #f2 = Image.fromarray(d)
    f2.save(out_dir+name+"combo.gif")
    
    print name, time.time()-t1

################################################################
