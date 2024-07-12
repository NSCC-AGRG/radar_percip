#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import urllib, time, re, Image
import numpy as N

#set the start and end date (YYYY MM DD HH)
#will auto increment by 1 hour

######################### CHANGE ###############################
site="XMB" # ie, XNC = NB, XGO = NS, XMB = CB
scale="RAIN" # SNOW or RAIN
start_date = time.strptime("2013 05 30 20 UTC", "%Y %m %d %H %Z")
end_date = time.strptime("2013 09 03 20 UTC", "%Y %m %d %H %Z")
out_dir = "D:/radar_percip/GIF/XMB/"
################################################################
start_time = int(time.mktime(start_date)-4*3600)
end_time = int(time.mktime(end_date)-3*3600)
at_time = start_time
nodata=[]
skip = 0

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
                if skip > 1:
                    skip -= 1
                    raise Exception()
                h = urllib.urlopen("http://www.climate.weatheroffice.gc.ca/radar" + str(y[0]).replace("amp;",""))
                skip=0
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
        if skip ==0:
            skip = 13
    z = h.read()
    h.close()

#new local image is generated
    g = open(out_dir+site+name+'.gif', 'wb')
    g.write(z)
    g.close()
    print "-"

#the final section will output the data to georefernced ascii and table data
    
print nodata

    
