# def pow(x,n):
#     if x == 0:
#         return 0
#     elif n == 0:
#         return 1
#     elif x > 0 and n > 0:
#         res = x**pow(x,n-1)
#     print(res)

# pow(2,5)
def Power(x, y):
    if y>0:
        return x * Power(x, y-1)
    else:
        return 1
print(Power(5, 3))







