import random
a = random.randint(1,6)
b=int(input("Guess the number from the dice: "))
if a==b:
    print(f"{True}, number is: {a}")
else: print(f"{False}, number is: {a}")