# This python program contains a logical error

print('This program prints all the even numbers \n between 1 and the a number of your choice\n')

number = int(input("Enter a number of your choice: "))

print(f"The Even numbers between 1 and {number} are:")
for i in range(number):
    if i%2 == 0:
        print(i)
