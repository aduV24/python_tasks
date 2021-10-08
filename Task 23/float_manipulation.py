# This program asks the user for 10 floats and performs various
# mathematical operations using the math module
floats = []

for i in range(1, 11):
    num = float(input(f"Please enter float {i}: "))
    floats.append(num)

n = len(floats)
print()
# Calculate total
total = sum(floats)
print(f"The total is: {round(total, 2)}")

# Display the index of the minimum and maximum
min_index = floats.index(min(floats))
print(f"The index of the minimum number is {min_index}")
max_index = floats.index(max(floats))
print(f"The index of the maximum number is {max_index}")

# Find the average
average = total/n
print(f"The average is {round(average, 2)}")

# Find the median
# Learnt how to use the floor division here :
# https://www.geeksforgeeks.org/python-arithmetic-operators/

median1 = floats[n//2]
median2 = floats[n//2 - 1]
median = (median1 + median2) / 2
print(f"The median is {median}")
