import itertools
import numpy as np
from functools import reduce
import sys

sim1 = np.genfromtxt("/Users/lgarcia/Desktop/fake_array.txt", names=True)

z = sim1["ztotal"]
x = sim1["logOverden"]
y = sim1["logT"]
#print(z[:])

min_x = np.min(x)
max_x = np.max(x)
min_y = np.min(y)
max_y = np.max(y)

print(min_x,max_x,min_y,max_y)

num_bin = 20

dx = (max_x - min_x)/num_bin
dy = (max_y - min_y)/num_bin

print(dx,dy)

z_arr = []
x_arr = []
y_arr = []

for i in range(0, num_bin):
    x_old = min_x + i*dx
    x_new = x_old + dx
    mid_x = (x_old + x_new)*0.5
    ind_x = np.where((x >= x_old) & (x < x_new))
    for j in range(0, num_bin):
        x_arr.append(mid_x)
        y_old = min_y + j*dy
        y_new = y_old + dy
        mid_y = (y_old + y_new)*0.5
        y_arr.append(mid_y)
        ind_y = np.where((y >= y_old) & (y < y_new))
        indices = reduce(np.intersect1d,(ind_x,ind_y))
        #print(len(indices))
        z_new = z[indices]
        z_now = np.mean(z_new)
        z_arr.append(z_now)

#data = np.column_stack((x_arr,y_arr,z_arr))        
#np.savetxt('grid_den_T_zmean.txt', data,fmt='%1.4e',delimiter='\t')
print(len(x_arr),len(y_arr),len(z_arr))

np.savetxt('grid_den_T_zmean.txt', np.transpose([x_arr,y_arr,z_arr]))

#print(x_arr[:])
#print(y_arr[:])
#print(z_arr[:])

### Two problems:

### 1. The routine does not support very large arrays... When the array is empty, there's a nan because it's taking the mean of nothing... solved!


### 2. It's losing one value in the boundary of T... 

### Chris' recommendations:
### Change the range of the min and max to cover all of the points and don't have issues with the boundaries
### Focus on my region of interest












#a.compress((a>5.5).flat)

## 
## for i in range(num_bin + 1):
##     kx.append(min_x + i*dx)
##     ky.append(min_y + i*dy)
    
#print(kx[:],ky[:])

#my_array = np.ndarray((num_bin + 1, num_bin + 1),dtype = object)

#for j,l in itertools.product(range(0num_bin + 1), range(num_bin + 1)):
    #my_array[i, j] = (kx[j],ky[l])
#print(my_array)

## def display():
##     kx = []
##     for i in range(num_bin + 1):
##         kx.append(min_x + i*dx)
##     return kx
## print(display())

## k_x = []
## k_y = []

## k_x.extend([]*(num_bin + 1))
## k_y.extend([]*(num_bin + 1))

## k_x.append([])
## k_y.append([])

## for i in range(0, num_bin) :
##     x_old = min_x + i*dx
##     k_x[i].append(x_old)
##     print(i,k_x[i])

## for j in range(0, num_bin -2):
##     y_old = min_y + j*dy
##     k_y[j].append(y_old)

#print(k_x)




        
    
    
