arr = [4,3,7,1,3]
def array2str(a):
    print("Array: ", end = "") 
    for i in a: print(i, end=" ")
array2str(arr)
print("")
def sum(b):
    sum=0
    for i in b: sum=sum+i
    print("Sum of values:",sum)
sum(arr)