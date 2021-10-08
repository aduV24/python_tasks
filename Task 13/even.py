# This program asks the user for a number and prints out all the even numbers from
# 1 up to the number given by the user using a while loop

num = int(input("Input a number: "))
i = 1
while i <= num:
    if i % 2 == 0:
        print(i)
    i+=1
