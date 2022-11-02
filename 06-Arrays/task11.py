a1=["water","book","sky"]
a2=["water","book","sky"]
b1=[True,False]
b2=[True,False,True]
c1=[5,3,1]
c2=[5,3,1]
d1=[3,2,1]
d2=[3,2]
def compare(ar1,ar2):
    print("Array1: ", end="")
    for i in ar1: print(i, end = " ")
    print("")
    print("Array2: ", end="")
    for i in ar1: print(i, end = " ")
    print("")
    for i in range(len(ar1)):
        if len(ar1)==len(ar2) and ar1[i]==ar2[i]:
            a=True
            continue
        else: a=False
        break   
    if a == True:
        print("Comparison: arrays are the same")
    else: print("Comparison: arrays are not the same")
compare(a1, a2)
compare(b1, b2)
compare(c1, c2)
compare(d1, d2)