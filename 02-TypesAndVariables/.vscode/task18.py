a=int(input("Write a for triangle: "))
b=int(input("Write b for triangle: "))
c=int(input("Write c for triangle: "))
p=(a+b+c)/2
AreaHeron=(p*(p-a)*(p-b)*(p-c))**(1/2)
print("The area for the triangle is ", AreaHeron)