import Image
import numpy as np

a = Image.open('1km_fill1.tif')
a.mode = 'I'
a = np.array(np.asarray(a))
##print 27880*22088
##a=np.zeros((27880/4,22088/4))
##a+=16

b=a*0
x=3318
y=1012
x=3710
y=188
x=280
y=94
b[x,y]=1
p=2

#TEST1##############

##while 1:
##    #somethwere this needs to make sure new cells
##    #included in the watershed are bordered by a
##    #minimum value which is already in the watershed
##    #print "a"
##    #THIS IS THE INEFFICIENT STEP
##    n = np.where(b==1)
##    #print "b"
##    b[np.where(b>0)]+=1
##    for j in range(np.prod(n[0].shape)):
##        if p==1:print n
##        xi=n[0][j]
##        yi=n[1][j]
##        ai=a[xi-1:xi+2,yi-1:yi+2]
##        if p==1:print a[xi-1:xi+2,yi-1:yi+2]
##        bi=b[xi-1:xi+2,yi-1:yi+2]
##        if p==1:print bi
##        bi=np.where((ai>=a[xi][yi])&(bi==0),1,bi)
##        if p==1:print bi
##        b[xi-1:xi+2,yi-1:yi+2]=bi
##        if p==1:print b[xi-1:xi+2,yi-1:yi+2]
##    print len(n[0])
##    if len(n[0])==0:break

#TEST2##############

##while 1:
##    #somethwere this needs to make sure new cells
##    #included in the watershed are bordered by a
##    #minimum value which is already in the watershed
##    #print "a"
##    #THIS IS THE INEFFICIENT STEP
##    n = np.where(b==1)
##    #print "b"
##    b[np.where(b>0)]+=1
##    #print len(np.where(b>0)[0])
##    for j in range(np.prod(n[0].shape)):
##        if p==1:print n
##        xi=n[0][j]
##        yi=n[1][j]
##        ai=a[xi-1:xi+2,yi-1:yi+2]
##        if p==1:print a[xi-1:xi+2,yi-1:yi+2]
##        bi=b[xi-1:xi+2,yi-1:yi+2]
##        if p==1:print bi
##        bi=np.where((ai>=a[xi][yi])&(bi==0),1,bi)
##        if p==1:print bi
##        b[xi-1:xi+2,yi-1:yi+2]=bi
##    ##The above over estimates the WS
##    #THIS IS THE NEW LINE to make sure the min cell is in the watershed
##    print len(n[0])
##    for j in range(np.prod(n[0].shape)):
##        xi=n[0][j]
##        yi=n[1][j]
##        bi=b[xi-1:xi+2,yi-1:yi+2]
##        print "B ONE"
##        print bi
##        ai=a[xi-1:xi+2,yi-1:yi+2]
##        print "B TWO"
##        print ai
##        b[xi][yi]=-1
##        print "B THREE"
##        print bi
##        try:
##            if bi[np.where(ai==ai.min())].any()==1:b[xi][yi]=1
##            print "B FOUR"
##            print bi
##            break
##        except ValueError:
##            print "Watershed has touched the edge"
##            break
##    print len(n[0])
##    if len(n[0])==0:break

#TEST3##############

while 1:
    #print "a"
    #THIS IS THE INEFFICIENT STEP
    n = np.where(b==1)
    #b[np.where(b>0)]+=1
    #print "b"
    #print len(np.where(b>0)[0])
    for j in range(np.prod(n[0].shape)):
        xi=n[0][j]
        yi=n[1][j]
        k=np.index_exp[xi-1:xi+2,yi-1:yi+2]
        b[k]=np.where((a[k]>=a[xi][yi])&(b[k]==0),1,b[k])
        #if b[k][np.where(a[k]==a[k].min())].any()==0:b[xi][yi]-=1
        #if (a[k]==a[k].min()+b[k]).any()==True:b[xi][yi]-=2
        b[xi][yi] += -2 if (((a[k]==a[k].min())== True )&((b[k]<1)==True)).any()==True else 1
        if j==2:
            print a[k]
            print a[k]==a[k].min()
            print b[k]
            print b[k]<1
            print ((a[k]==a[k].min())== True )&((b[k]<1)==True)
            print (((a[k]==a[k].min())== True )&((b[k]<1)==True)).any()
        #print b[k][np.where(a[k]==a[k].min())].any()==0
        
    ##The above over estimates the WS
    #THIS IS THE NEW LINE to make sure the min cell is in the watershed
##    print len(n[0])
##    for j in range(np.prod(n[0].shape)):
##        xi=n[0][j]
##        yi=n[1][j]
##        kern=np.index_exp[xi-1:xi+2,yi-1:yi+2]
##
##        bi=b[kern]
##        ai=a[kern]       
##        try:
##            if bi[np.where(ai==ai.min())].any()==0:b[xi][yi]-=1
##        except ValueError:
##            print "Watershed has touched the edge"
##            break
    print len(n[0])
    if len(n[0])==0:break

#OUTPUTS#############################################

b=np.where(b>0,255,0)
f2 = Image.fromarray(np.array(np.clip(b,0,255),'uint8'))
f2.save('D:/radar_percip/temp/1km_valley_ws4.gif')

f2 = Image.fromarray(np.array(np.clip(a,0,255),'uint8'))
f2.save('D:/radar_percip/temp/1km_valley.gif')
