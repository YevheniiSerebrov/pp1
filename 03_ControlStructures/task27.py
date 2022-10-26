# for i in range(6,-1,-3):
#     for j in range(1,4):
#         print(f' {i+j}',end='')
#     print()

x = 5
while x > -2:
    y = 1
    while y < 4 :
        y = y + 1
        print(f"{x+y} ", end=" ")
    x = x - 3
    print()