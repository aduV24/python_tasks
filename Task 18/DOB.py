# This program reads data from trh text file called DOB.txt and prints
# it out in two different sections.

#Create  two empty lists to store the names and DOBs
names = []
DOBs = [] 


with open('DOB.txt','r+',encoding='utf-8') as file:
    # loop through each line of file
    for  line in file:
        # split each line at the whitespace and save the list of splitted strings to a variable
        info = line.strip('\n').split(' ')
        # index the 1st two items and last 3 items and append them to the 'names' and 'DOBs' lists respectively
        # learnt about list indexing here ==> https://www.tutorialspoint.com/python/python_lists.htm
        names.append(info[0]+" "+info[1])
        DOBs.append(info[2]+" "+info[3]+" "+info[4])


# Loop through the 'names' and 'DOBs' lists respectively and print them out.

print("Names:")
print("---------")
for x in names:
    print(x)

print()

print("Date of birth")
print("--------------------")
for y in DOBs:
    print(y)