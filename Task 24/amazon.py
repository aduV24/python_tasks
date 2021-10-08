# This program reads the content of input.txt  file, performs some operations on
# each line and writes the answer into the output.txt file

def minimum(lst):
    return min(lst)


def maximum(lst):
    return max(lst)


def avg(lst):
    return sum(lst)/len(lst)


with open('input.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        # Slit the line at ":"" and select the numbers
        split_line = line.strip('\n').split(":")[1]
        nums = split_line.split(",")
        # Convert the string to integers
        num1 = [int(x) for x in nums]

# Write into the output file
with open('output.txt', 'w', encoding='utf-8') as outfile:
    outfile.write(f'The minimum of {num1} is {str(minimum(num1))}\n')
    outfile.write(f'The maximum of {num1} is {str(maximum(num1))}\n')
    outfile.write(f'The average of {num1} is {str(avg(num1))}')
    
print("Data written into output.txt")
