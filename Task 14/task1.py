# This python program asks the user to input a number and then displays the 
# times table for that number using a for loop

num = int(input("Please Enter a number: "))
print(f"The {num} times table is:")

# Initialise a loop and print out a times table pattern using the variable
for x in range(1,13):
    print(f"{num} x {x} = {num * x}")