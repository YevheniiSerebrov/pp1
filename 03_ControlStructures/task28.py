n = 10
a, b = 0, 1
print(f"{a} {b}", end=" ")
for i in range(1,n+1):
    sum=a+b
    a=b
    b=sum
    print(sum, end = " ")



