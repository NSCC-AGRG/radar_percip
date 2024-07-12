#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import urllib, time, re, Image, os
import numpy as N

#set the start and end date (YYYY MM DD HH)
#will auto increment by 1 hour

######################### CHANGE ###############################
site="XGO" # ie, XNC = NB, XGO = NS, XMB = CB
scale="RAIN" # SNOW or RAIN
start_date = time.strptime("2007 11 11 11 UTC", "%Y %m %d %H %Z")
end_date = time.strptime("2008 3 11 13 UTC", "%Y %m %d %H %Z")
in_dir = 'D:/radar_percip/GIF/XGO/'
out_dir = 'D:/radar_percip/CSV/XGO/'
################################################################
start_time = time.mktime(start_date)-4*3600
end_time = time.mktime(end_date)-3*3600
at_time = start_time
nodata=[]
#f = open(out_dir+"test1.txt", 'w+')

for at_time in range(start_time,end_time,3600):
    x=time.gmtime(at_time)
    name=str(x.tm_year)+("","0")[int(x.tm_mon)<10]+str(x.tm_mon)+("","0")[int(x.tm_mday)<10]+str(x.tm_mday)+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)

    h = Image.open(in_dir+site+name+'.gif')
    i = N.array(N.asarray(h))

    summer_mm = {i[151][525]:199.8125, \
                 i[165][525]:142.8028, \
                 i[179][525]:100.7319, \
                 i[193][525]:70.4192, \
                 i[207][525]:49.0825, \
                 i[221][525]:34.338, \
                 i[235][525]:24.2003, \
                 i[249][525]:17.0824, \
                 i[263][525]:11.7957, \
                 i[277][525]:7.55, \
                 i[291][525]:3.9535, \
                 i[305][525]:2.5, \
                 i[319][525]:1, \
                 i[333][525]:0.7}

    b = i*0.0
    c = i*0.0

    for k, v in summer_mm.iteritems():
        b[i==k] = v

#this next section attempts to conditionally filter out the graticule

    d = b
    d = N.where(d==0,N.NaN,d)
    d=N.ma.masked_array(d,N.isnan(d))  

    #x,y = N.where((i==93)|(i==4)|(i==0))
    x,y = N.where((i==i[240][240])|(i==4)|(i==3))
    for i in range(len(x)):
        c[x[i],y[i]]=d[cmp(0,x[i])+x[i]-1:x[i]+2, cmp(0,y[i])+y[i]-1:y[i]+2].mean()

    ci = N.isnan(c)
    c[ci]=0
    b = c+b
    N.save('D:/radar_percip/NPY/XGO/'+name, b)
    x = str(name)+", "+str(b.mean())+"\n"
    print x
    #f.write(x)



##for fn in os.listdir(xgo_dir):
##    xgo_size += os.path.getsize(xgo_dir+fn)
##    if os.path.getsize(xgo_dir+fn)/1024 < 3:
##        xgo_null_count += 1
##    xgo_count += 1
##    name = os.path.splitext(fn)[0]
##    h = Image.open(xgo_dir+fn)
##    #N.save('D:/radar_percip/NPY/XGO/'+name, a)
##    if test_count == 0:
##        break
##    test_count -=1
##
##print xgo_count, xgo_null_count, xgo_size/xgo_count/1024

