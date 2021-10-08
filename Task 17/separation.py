# This program asks the user for a sentence and then displays 
# each character of that senetence on a new line

string = input("Enter a sentence:\n")

# split string into  a list of words
words = string.split(" ")
# Iterate thorugh the string and print each word
for word in words:
    print(word)