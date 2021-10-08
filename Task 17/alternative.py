# This program asks the user to input a word / sentence and makes
# each alternate character an upper case character and each other 
# characteer a lowewrcase character

string = input("Enter a word /sentence:\n")

# Create an empty list for the string builder and initialise a counter
string_builder = []
i = 0

# Create a loop that goes through the string
while i < len(string):

    # Use the even/odd logic to index alternate characters, put them in
    # upper /lower case and append them to the string builder's list

    if i % 2 == 0:
        string_builder.append(string[i].upper())
    else:
        string_builder.append(string[i].lower())
    i += 1

# Join the characters and display
print("".join(string_builder))