# This program counts the number of characters, words, linews and vowels 
# in a file, it then displays the results 

# Iniatilse a counter for words, lines,characters and vowels
character_count = 0
word_count = 0
line_count = 0
vowel_count = 0
vowels = 'aeiou'

with open('input.txt','r+', encoding='utf-8') as file:
    # Loop through each line
    for line in file:
        # print(line.strip('\n'))
         
        # Count the characters in each line
        for k in line.strip('\n'):
             character_count+=1
 
        # Split the line into a list, loop thorugh the list and count each item
        words = line.strip('\n').split(" ")
        for word in words:
            word_count+=1
            
            # Check for vowels in each word
            for char in word:
                if char in vowels:
                    vowel_count+=1
        
        # count the line
        line_count+=1       

print(f"word count is {word_count}")
print(f"NUmber of lines is {line_count}")
print(f"vowel count is {vowel_count}")
print(f"Character count is {character_count}")