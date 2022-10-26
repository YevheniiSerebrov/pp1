import numpy as np 
import pandas


import random
arr = np.arange(10)
arrr=np.arange(10)
for i in range(10):
    arrr[i]=i+1
    arr[i]= random.randint(10,90)
print(arr)
print(arrr)

