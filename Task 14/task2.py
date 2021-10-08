# This program asks the user to input a year a number of years
# It then displays which of years were or will be leap years
# Using a for loop.

year = int(input("What year do you wwant to start with?: "))
num_of_years = int(input("How many years do you want to check?:"))

# Handling invalid inputs
if num_of_years <= 0 or year <= 0:
    print("Please input a positive integer greater than zero")

else:
    # Initialise the loop, decide if the current year is a leap year and display
    for i in range (num_of_years):
        if (year+i) % 4 == 0:
            print(f"{year+i} is a leap year")
        else:
            print(f"{year+i} isn't a leap year")
