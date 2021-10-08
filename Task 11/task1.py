num1 =60
num2 = 111
num3 = 100
if num1 > num2:
    print(num1)
else:
    print(num2)
print()
if num1 % 2 == 0:
    print("The first number is even")
else:
    print("The first number is odd")
print()
print("Numbers in descending order")
print("===================================")
if (num1 > num2) and (num1 > num3 ):
    if num2 > num3:
        print(f"{num1}\n{num2}\n{num3}")
    else:
        print(f"{num1}\n{num3}\n{num2}")
elif (num2 > num1) and (num2 > num3 ):
    if num1 > num3:
        print(f"{num2}\n{num1}\n{num3}")
    else:
        print(f"{num2}\n{num3}\n{num1}")

else:
    if num1 > num2:
        print(f"{num3}\n{num1}\n{num2}")
    else:
        print(f"{num3}\n{num2}\n{num1}")

