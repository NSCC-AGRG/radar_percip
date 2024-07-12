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
end_date = time.strptime("2011 11 11 13 UTC", "%Y %m %d %H %Z")
in_dir = 'D:/radar_percip/GIF/XGO/'
out_dir = 'D:/radar_percip/NPY/COMBO/'
################################################################

def radgif2npy(site,name):

    a = Image.open('D:/radar_percip/GIF/'+site+'/'+site+name+'.gif')
    a = N.array(N.asarray(a))

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

    a=a[0:480,0:480]

    if a[240][240]==0:
        return a

    mask = Image.open('D:/radar_percip/GIFmask.gif')
    mask = N.array(N.asarray(mask))
    a=N.where(mask==0,-6666,a)

    #put in ifs conditional on site for n1 (graticule), n2(roads)
    n1 = a[240][240]
    n2 = -9999

    if a[280][240]==n1:
        if site=="xgo": n2 = a[246][205]
        if site=="xnc": n2 = a[271][230]
        if site=="xmb": n2 = a[272][149]
    print n1,a[280][240], n2, a[246][205]
    
    for (x,y), value in N.ndenumerate(a):
        if (a[x,y]==n1 or a[x,y]==n2):
            b = a[cmp(0,x)+x:x+2, cmp(0,y)+y:y+2]
            b=b.flatten() 
            b=b[b != n1]
            b=b[b != n2]
            counts = N.bincount(b)
            a[x,y] = N.argmax(counts)

    a=N.where(a==-6666,0,a)
    c = a*0
    
    for k, v in summer_mm.iteritems():
        c[a==k] = v

    return c

################################################################

start_time = time.mktime(start_date)-4*3600
end_time = time.mktime(end_date)-3*3600
at_time = start_time

for at_time in range(start_time,end_time,3600):
    x=time.gmtime(at_time)
    name=str(x.tm_year)+("","0")[int(x.tm_mon)<10]+str(x.tm_mon)+("","0")[int(x.tm_mday)<10]+str(x.tm_mday)+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)

    t1= time.time()
    print name
    
    xgo = radgif2npy("xgo",name)
    xnc = radgif2npy("xnc",name)
    xmb = radgif2npy("xmb",name)

    xnc1 = xnc[125:480,157:580]
    xnc2 = xgo*0
    xnc2[0:xnc1.shape[0],0:xnc1.shape[1]] = xnc1
    xgo = N.where(xnc2>xgo,xnc2,xgo)

    xmb1 = xmb[95:480,0:306]
    xmb2 = xgo*0
    xmb2[0:xmb1.shape[0],xgo.shape[1]-xmb1.shape[1]:xgo.shape[1]] = xmb1
    xgo = N.where(xmb2>xgo,xmb2,xgo)

    combo = xgo *20

    N.save(out_dir+name, combo)
    f2 = Image.fromarray(N.array(N.clip(combo,0,255),'uint8'))
    f2.save(out_dir+name+"combo.gif")
    
    print time.time()-t1

################################################################
