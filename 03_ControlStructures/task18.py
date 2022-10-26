a=int(input("Enter the amount in PLN: "))
b=a%5
if b == 0:
    print(f"The amount of PLN{a} in coins:\n5 zl - {a//5}")
elif b == 2 or b == 4:
    print(f"The amount of PLN{a} in coins:\n5 zl - {a//5}\n2 zl - {b/2}  ")
elif b == 3:
    print(f"The amount of PLN{a} in coins:\n5 zl - {a//5}\n2 zl - {1}\n1 zl - {1}  ")
elif b == 1:
    print(f"The amount of PLN{a} in coins:\n5 zl - {a//5}\n1 zl - {1}")

