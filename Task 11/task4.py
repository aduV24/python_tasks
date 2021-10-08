num = int(input("Enter an integer:\n"))

if (num%2) == 0 and (num%5) == 0:
    print("The integer entered is divisible by 2 and 5")
elif (num%2) == 0 or (num%5) == 0:
    print("The integer entered is either divisible by 2 or 5")
else:
    print("The integer entered is neither divisible by 2 nor 5")