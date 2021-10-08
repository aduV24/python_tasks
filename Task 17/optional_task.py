string = input("enter a word:\n")

# Create an empty string builer and initialise a counter
string_builder = ""
i = 1

while i <= len(string):
    # Index the srtring frokm the end and add to the string builder
    string_builder += string[-i]
    i += 1

# Check if the string_builedr matshes the word given
if string == string_builder:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")
