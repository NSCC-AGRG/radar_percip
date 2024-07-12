import numpy as np
import time

a = np.random.randint(7, size=(580,480))

#print a
t1 = time.time()

for (x,y), value in np.ndenumerate(a):
    if (a[x,y]==0 or a[x,y]==1):
        b = a[cmp(0,y)+y:y+2, cmp(0,x)+x:x+2]
        b=b.flatten()
        b=b[b != 0]
        b=b[b != 1]
        counts = np.bincount(b)
        a[x,y] = np.argmax(counts)

print time.time()-t1

