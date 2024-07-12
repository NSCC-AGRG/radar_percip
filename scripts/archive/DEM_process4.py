import Image
import numpy as np

a = Image.open('1km_fill1.tif')
a.mode = 'I'
a = np.array(np.asarray(a))

b=a*0
x=3318
y=1012
x=3710
y=188
x=280
y=94
b[x,y]=1
p=2

while 1:
    #print "a"
    #THIS IS THE INEFFICIENT STEP
    n = np.where(b==1)
    b[np.where(b>0)]+=1
    #print "b"
    #print len(np.where(b>0)[0])
    for j in range(np.prod(n[0].shape)):
        xi=n[0][j]
        yi=n[1][j]
        k=np.index_exp[xi-1:xi+2,yi-1:yi+2]
        b[k]=np.where((a[k]>=a[xi][yi])&(b[k]==0),1,b[k])
        #if b[k][np.where(a[k]==a[k].min())].any()==0:b[xi][yi]-=1
        #if (a[k]==a[k].min()+b[k]).any()==True:b[xi][yi]-=2
        #b[xi][yi] += -2 if (((a[k]==a[k].min())== True )&((b[k]<1)==True)).any()==True else 1
##        if j==2:
##            print a[k]
##            print a[k]==a[k].min()
##            print b[k]
##            print b[k]<1
##            print ((a[k]==a[k].min())== True )&((b[k]<1)==True)
##            print (((a[k]==a[k].min())== True )&((b[k]<1)==True)).any()

    print len(n[0])
    if len(n[0])==0:break

#OUTPUTS#############################################

b=np.where(b>0,255,0)
f2 = Image.fromarray(np.array(np.clip(b,0,255),'uint8'))
f2.save('D:/radar_percip/temp/1km_valley_ws4.gif')

f2 = Image.fromarray(np.array(np.clip(a,0,255),'uint8'))
f2.save('D:/radar_percip/temp/1km_valley.gif')
