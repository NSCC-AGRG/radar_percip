#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import urllib, time, re, Image
import numpy as N



#new local image is generated
    g = open(out_dir+"raw/"+site+name+'.gif', 'wb')
    g.write(z)
    g.close()
    print "-"
    
#Performs image processing with numpy
#greates a array from the image
    h = Image.open(out_dir+"raw/"+site+name+'.gif')
    i = N.array(N.asarray(h))

#recodes the image int values into a floating point array
    #coded_mm = [40,42,41,5,21,36,37,38,2,33,34,35,43,52]
    #summer_mm = {40:199.8125 , 42:142.8028, 41:100.7319, 5:70.4192, 21:49.0825, 36:34.338, 37:24.2003, 38:17.0824, 2:11.7957, 33:7.55, 34:3.9535, 35:2.5, 43:1, 52:0.7}
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
    print b.mean(),b.max()

    #makes the data easier to see as a gif
    b*=50

    #outputs the raster as a gif
    f1 = Image.fromarray(N.array(N.clip(b,0,255),'uint8'))
    f1.save(out_dir+site+name+'.gif')


#the final section will output the data to georefernced ascii and table data
    
print nodata

    
