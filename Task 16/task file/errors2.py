# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

animal = "Lion" #Syntax Error:  'lion is a string literal, needs quoatation
animal_type = "cub" # Compilation error: incorrect space indentation, needs to be in line with variable 'animal'
number_of_teeth = 16


full_spec = f"This is a {number_of_teeth}. It is a {animal} and it has {animal_type} teeth" #logical Error: Needs a 'f' before the quotation for string formatting; The 'animal' and 'number_of_teeth' variables are put in wrong place holders 

print (full_spec) # Syntax Error: missing parentheses

