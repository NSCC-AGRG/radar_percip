import Image
import numpy as np

a = Image.open('1km_fill1.tif')
a.mode = 'I'
a = np.array(np.asarray(a))

##a[290]=0
##a[:,150]=0
runs=0
#a[290][150]=0
b=a*0
#b=np.where(a>a[290][150],250,b)

##c=np.where(a==500)
##c=c+a[290][150]

x=290
y=150
#print c
b[x,y]=-1
#TEST1#################################################
##while runs<40:
##    c=c*0
##    print "Run",runs
##    n = np.where(b==100)
##    print n
##    for j in range(np.prod(n[0].shape)):
##        xi=n[0][j]
##        yi=n[1][j]
##        c[xi-1:xi+1,yi-1:yi+1]=100
##        b=np.where(aa[xi][yi],c-100,b)
##    b+=c
##    runs+=1
p=1
#TEST2#################################################
##while runs<3:
##    if p==1:print "Run",runs
##    n = np.where(b==-1)
##    g = np.where(b==100)
##    if p==1:print n
##    if p==1:print g
##    if p==1:print range(np.prod(n[0].shape))
##    for j in range(np.prod(n[0].shape)):
##        xi=n[0][j]
##        yi=n[1][j]
##
##        if p==1:print a[xi-1:xi+2,yi-1:yi+2]
##        d=a[xi-1:xi+2,yi-1:yi+2]
##        
##        if p==1:print runs,j, "ONE"
##        if p==1:print b[xi-1:xi+2,yi-1:yi+2]
##        c=b[xi-1:xi+2,yi-1:yi+2]
##
##        if p==1:print runs,j, "TWO"
##        c=np.where(((d>=d[1][1])&(c==-1))|(c==100),100,0)
##        if p==1:print b[xi-1:xi+2,yi-1:yi+2]
##
##        if p==1:print runs,j, "THREE"
##        b[xi-1:xi+2,yi-1:yi+2]=-1
##        if p==1:print b[xi-1:xi+2,yi-1:yi+2]
##
##        if p==1:print runs,j, "FOUR"
##        b[n]=100
##        b[g]=100
##        if p==1:print b[xi-1:xi+2,yi-1:yi+2]
##        
##    runs+=1

#TEST3#################################################
##x=360
##y=150
x=274
y=101
b[x,y]=1
p=2

while 1:
    n = np.where(b==1)
    b[np.where(b>0)]+=1
    for j in range(np.prod(n[0].shape)):
        if p==1:print n
        xi=n[0][j]
        yi=n[1][j]
        ai=a[xi-1:xi+2,yi-1:yi+2]
        if p==1:print a[xi-1:xi+2,yi-1:yi+2]
        bi=b[xi-1:xi+2,yi-1:yi+2]
        if p==1:print bi
        bi=np.where((ai>=a[xi][yi])&(bi==0),1,bi)
        if p==1:print bi
        b[xi-1:xi+2,yi-1:yi+2]=bi
        if p==1:print b[xi-1:xi+2,yi-1:yi+2]
    print len(n[0])
    if len(n[0])==0:break

#b=np.where((a<200)&(a>100),200,0)

##e = a[cmp(0,x)+x:x+2, cmp(0,y)+y:y+2]
##
##print e

while runs<2:
##    for (x,y), value in np.ndenumerate(b):
##        look = b[cmp(0,x)+x:x+2, cmp(0,y)+y:y+2]
##        #print look.sum()
##        if look.sum()>0:
##            b[x,y]=250
    runs+=1
    
b=np.where(b>0,255,0)
f2 = Image.fromarray(np.array(np.clip(a,0,255),'uint8'))
f2.save('D:/radar_percip/temp/1km_fill1.gif')

f2 = Image.fromarray(np.array(np.clip(b,0,255),'uint8'))
f2.save('D:/radar_percip/temp/1km_fill2.gif')
