import numpy
a1=[4,36,12,28,9,44,5]
a2=[5,1,36]
# for i in a1:

# print(str(a1).replace(str(a2), ""))

for i in a1:
    for j in a2:
        print(str(i).replace(str(j), ""))
        