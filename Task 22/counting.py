# This program counts the number of times a character occurs
# (character frequency) in a string.

word = input("Enter a word:\n")

counter = {}

for char in word:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1

print(counter)
