# This program asks the user to input a string, and characters they wish to
# strip, It then displays the string without those characters.

string = input("Enter a string:\n")
char = input("Enter characters you'd like to make disappear separated by a +\
              comma:\n")

# Split the characters given into a list and loop through them
for x in char.split(","):
    # Check if character is in string and replace it
    if x in string:
        string = string.replace(x, "")
    else:
        print(f"'{x}' is not in the string given")

print("\n" + string)
