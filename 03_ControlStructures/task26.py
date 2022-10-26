pin = "0805"
for i in range(0,3):
    a = input("Enter the PIN code: ")
    if a == pin:
        print("Right!")
        break
    elif 2-i == 0:
            print("Sorry, your payment card has been blocked")
    else: 
        print(f"Incorrect, you have {2-i} attempts")
        

