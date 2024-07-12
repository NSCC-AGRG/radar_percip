#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import urllib, time, re, Image
import numpy as N

#set the start and end date (YYYY MM DD HH)
#will auto increment by 1 hour

######################### CHANGE ###############################
site="XGO" # ie, XNC = NB, XGO = NS, XMB = CB
scale="RAIN" # SNOW or RAIN
start_date = time.strptime("2007 11 11 11 UTC", "%Y %m %d %H %Z")
end_date = time.strptime("2013 05 29 11 UTC", "%Y %m %d %H %Z")
out_dir = "V:/Kevin/radar_percip/scripts/v5_test/"
################################################################
start_time = time.mktime(start_date)-4*3600
end_time = time.mktime(end_date)-3*3600
at_time = start_time
nodata=[]

for at_time in range(start_time,end_time,3600):
    x=time.gmtime(at_time)
    name=str(x.tm_year)+("","0")[int(x.tm_mon)<10]+str(x.tm_mon)+("","0")[int(x.tm_mday)<10]+str(x.tm_mday)+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)
    print name

#reads the historical radar website for the approprate time
    while True:
        try:
            print "1"
            f = urllib.urlopen("http://www.climate.weatheroffice.gc.ca/radar/index_e.html?RadarSite="+site+"&sYear="+str(x.tm_year)+"&sMonth="+str(x.tm_mon)+"&sDay="+str(x.tm_mday)+"&sHour="+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)+"&sMin=00&Duration=12&ImageType=PRECIP_"+scale)                            
        except IOError as err:
            print "reconnecting.."
            time.sleep(3)
        else:
            print "."
            break
    x = f.read()
    f.close()
    print "."

#image url extension is found on historical radar page
    y=re.findall('/image.*?='+site,x)
    try:
        print y[0]
        while True:
            try:
                print "2"
                h = urllib.urlopen("http://www.climate.weatheroffice.gc.ca/radar" + str(y[0]).replace("amp;",""))
            except IOError as err:
                print "reconnecting.."
                time.sleep(3)
            else:
                print "."
                break
    except:
        print "################################ NO DATA #####################################"
        h = open('V:/Kevin/radar_percip/scripts/empty.gif', 'rb')
        nodata.append(name)
    z = h.read()
    h.close()

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

    
