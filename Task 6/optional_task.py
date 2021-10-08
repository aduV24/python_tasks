import math
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))
s=(a+b+c)/2
area = float(math.sqrt(s*(s-a)*(s-b)*(s-c)))
print("The area of the triangle with sides of length",a,"and",b,"and",c,"is",area,end=".")