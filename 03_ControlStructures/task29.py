n=None
sum=0
q=0
while n != 0:
    n=int(input("Enter number: "))
    sum = n + sum
    q=q+1
mean = sum/(q-1)    
print(f"Quantity = {q-1}, Sum = {sum}, Mean = {mean}")
    
