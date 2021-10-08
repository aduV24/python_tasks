#This python program asks the user to enter names of pupils and then outputs 
#The total number of names entered using a while loop.

name = input("Please enter a name: ")
i = 0

while name.lower() != "stop":
    i += 1
    name = input("Please enter a name: ") 

print(f"The total number of names entered is {i}")