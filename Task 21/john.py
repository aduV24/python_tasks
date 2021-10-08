# This program continues to ask the user to enter a name until they enter "John"
# The program then displays all the incorrect names that was put in
wrong_inputs = []
name = input("Please input a name:\n")

while name != "John":
    wrong_inputs.append(name)
    name = input("Please input a name:\n")

print(f"Incorrect names:{wrong_inputs}")
