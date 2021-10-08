# This python program sorts and writes numbers in to a all_numbers.txt file 
# from  numbers1.txt and numbers2.txt files respectively


# Create an empty list to store numbers from both files
all_numbers = []

# Open each file, read each line and append to the all_numbers list
with open('numbers1.txt', 'r+', encoding='utf-8') as file1:
    for line in file1:
        line = line.strip('\n')
        all_numbers.append(int(line))

with open('numbers2.txt', 'r+', encoding='utf-8') as file2:
    for line in file2:
        line = line.strip('\n')
        all_numbers.append(int(line))

# Learnt how to sort items in a list here: https://www.geeksforgeeks.org/python-list-sort/
all_numbers.sort()

file3 = open('all_numbers.txt', 'w')

import json

# Write the numbers into the new file
for num in all_numbers:
    file3.write(str(num)+'\n')

print("All numbers sorted and written into the all_numbers.txt file")
