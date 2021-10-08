# This program asks the user to enter a number and then calculates the average of
# the numbers entered using a while loop

num = int(input("Enter a number: "))

# Initialise the 'count' and 'total' variable to control the loop and accummulate
# the scores respectively 

count = 0
total = 0

while num != -1 :
    count += 1
    total += num
    num = int(input("Enter a number: "))

if total == 0:      # Handles the zero division error
    print("Exiting...")
else:
    average = total / count
    print(average)