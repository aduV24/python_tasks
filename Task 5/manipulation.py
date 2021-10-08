str_manip = input("Type in a sentence:\n")
str_len = len(str_manip)
#Display length of string
print(f"The length of the sentence is {str_len}")
print()

#Save the last letter to a variable
last_letter = str_manip[str_len-1]
#Replace every occurrence of the last letter with "@" and display.
str_manip_1 = str_manip.replace(last_letter, "@")
print(str_manip_1)
print()

#Slice with a step to reverse 
# https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
print(str_manip[str_len-1:str_len-4:-1])
print()

#Slice and take the first 3 letters and last two letters and concatenate them
print(str_manip[0:3]+str_manip[str_len-2:])
print()

#Replace spaces with the new line escape seqence to display each word on a new line
new_line = str_manip.replace(" ","\n")
print(new_line)

