ar=["ab", "abcdfe", "abcd", "abc", "abcde"]
max=0
for i in ar:
    print(i, end = " ")
print("")
for i in range(len(ar)):
    c=0
    for j in ar[i]:
       c=c+1
       if c>max:
            max=c
            d=ar[i]
print("longest name: "+ d)

               
