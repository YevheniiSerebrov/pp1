a=[15,8,31,47,2,19]
def rever(a1):
    c=len(a1)
    print("existed array: ", end="")
    for i in a1:
        print(i, end=" ")
    print("")
    print("reversed array:", end=" ")
    for i in a1:
        c=c-1
        print(a1[c], end=" ")
rever(a)
       