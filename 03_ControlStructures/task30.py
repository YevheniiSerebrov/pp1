n = int(input("Input the value: "))
q=0
for i in range(1,n+1):
    if n% i == 0:
       q=q+1
    else:  q=q
if q == 2:
    print(f"Number {n} is a prime")
else: print(f"Number {n} has {q} natural factors ")