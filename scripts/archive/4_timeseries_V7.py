#Script will seek out and download historical radar data from environment canada 
#Created by Kevin K McGuigan, Applied Geomatics Research Group

import urllib, time, re, Image, os
import numpy as N

#set the start and end date (YYYY MM DD HH)
#will auto increment by 1 hour

######################### CHANGE ###############################
site="XGO" # ie, XNC = NB, XGO = NS, XMB = CB
scale="RAIN" # SNOW or RAIN
start_date = time.strptime("2007 10 02 04 UTC", "%Y %m %d %H %Z")
#end_date = time.strptime("2007 11 03 04 UTC", "%Y %m %d %H %Z")
end_date = time.strptime("2013 05 30 20 UTC", "%Y %m %d %H %Z")
in_dir = 'D:/radar_percip/NPY/V7/'
out_dir = 'D:/radar_percip/NPY/V7_TS2/'
################################################################

start_time = time.mktime(start_date)-4*3600
end_time = time.mktime(end_date)-3*3600
at_time = start_time

##a = Image.open('D:/radar_percip/NPY/V7/V7_'+'2007100204'+'.gif')
##a = N.array(N.asarray(a))
##combo=a*0
##combo = N.int32(combo)
##print combo.dtype
##
##for at_time in range(start_time,end_time,3600):
##    x=time.gmtime(at_time)
##    name=str(x.tm_year)+("","0")[int(x.tm_mon)<10]+str(x.tm_mon)+("","0")[int(x.tm_mday)<10]+str(x.tm_mday)+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)
##
##    t1= time.time()
##    #print name
##
##    a = Image.open('D:/radar_percip/NPY/V7/V7_'+name+'.gif')
##    a = N.array(N.asarray(a))
##
##    combo = combo+a
##    #print time.time()-t1
##
##print combo.max(), combo.min()
##N.save(out_dir+name, combo)
##combo = 255 - (((255)*(combo.max() - combo))/(combo.max()-combo.min()))
##f2 = Image.fromarray(N.array(N.clip(combo,0,255),'uint8'))
##f2.save(out_dir+"V7_"+name+".gif")

out_file = out_dir +"V7_"+ "TEST" +'_TS.txt'
##g = open(out_file,'w')
##g.close
g = open(out_file,'a++')
t1= time.time()
counter = 0
text=""

for at_time in range(start_time,end_time,3600):
    x=time.gmtime(at_time)
    name=str(x.tm_year)+("","0")[int(x.tm_mon)<10]+str(x.tm_mon)+("","0")[int(x.tm_mday)<10]+str(x.tm_mday)+("","0")[int(x.tm_hour)<10]+str(x.tm_hour)
    #print name
    a = Image.open('D:/radar_percip/NPY/V7/V7_'+name+'.gif')
    a = N.array(N.asarray(a))
    text+=name+" "+str(a[240][240])+"\n"
    #text=""
    if counter > 3000:
        g.write(text)
        text=""
        counter=0
    counter+=1
    
g.write(text)    
g.close
print time.time()-t1
   
################################################################
