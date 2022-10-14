weight=int(input("Enter your weight: "))
height = int(input("Enter your height in cm: "))
BMI = weight/(0.01*height)**2
print(BMI)
if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal weight")
elif 25 <= BMI < 30:
    print("Pre-obesity")
elif 30 <= BMI <35:
    print("Obesity class I")
elif 35 <= BMI < 40:
    print("Obesity class II")
elif BMI >= 40:
    print("Obesity class III")