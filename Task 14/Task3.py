# This program uses a while loop to display a countdown from 20 t0 0
x = 20
while x >=0:
    print(x)
    x-=1

print("====================================================================")

# This program displays all even numbers betweeen 1 and 20 using a for loop
for i in range (1,21):
    if i%2 ==0:
        print(i)

print("====================================================================")

# This program displays a pattern using a for loop
star = "*"
for i in range (1,6):
    print(star * i)


print("====================================================================")

# This asks the user to enter two numbers and then computes the Greatest common 
# divisor of both numbers using a for loop

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

# I learnt how to get the minimum of two or more numbers using the min fucntion
# https://thepythonguru.com/python-builtin-functions/min/

smaller_no = min(num1,num2)

# Since the gcd of two numbers cannot exceed the smaller number, iterate through
# a range of numbers with between 1 and the smaller number compute and display the gcd

for i in range(1,smaller_no+1):
    if (num1%i == 0) and (num2%i == 0):
        gcd = i

print(f"The greatest common divisor is {gcd}")
