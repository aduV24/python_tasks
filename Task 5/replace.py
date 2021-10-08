word = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
#Replace "!" with " "
word_1 = word.replace("!"," ")
print(word_1)
#Print string in upper case
print(word_1.upper())

#I learnt about strides/step from the a website hence I decided to use it in reversing the sentence
# https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
print(word_1[::-1])