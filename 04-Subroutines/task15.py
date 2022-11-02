# import numpy as np 
# import pandas
# import random
# arr = np.arange(10)
# arrr=np.arange(10)
# for i in range(10):
#     arrr[i]=i+1
#     arr[i]= random.randint(10,90)
# print(arr)
# print(arrr)
import mymath
a1 = mymath.read_number()
b1 = mymath.generate_number()
print(a1,b1)
if a1 == b1:
    print("You win!")
else: print("You failed!")

