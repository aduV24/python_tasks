# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print ("Welcome to the error program")  # Syntax Error; Missing parentheses
print ("\n") # Compilation error; incorrect space indentation, needs to be in line with the previous print statement

  
ageStr = "I'm 24 years old" # I'm 24 years old. #Logical Error: The string is missing "I'm"; Compilation error:incorrect 
                            # space indentation, needs to be in line with the previous print statement; runtime error: It 
                            # is meant to be an assignment statement witn one '='
    
    

age = 24 # Compilation error: incorrect space indentation, needs to be in line with the 'ageStr' variable;
         # Runtime error: can't cast  an alphanumeric string to an integer


print("I'm "+str(age)+" years old.") # Compilation error: incorrect space indentation, needs to be in line with the 'age' variable;
                                     # Runtime Error: 'age' needs to be casted to a string

three = 3 # Compilation error: incorrect space indentation, needs to be in line with the print statement;
          # Logical Error, '3' needs to be an integer, not a string

answerYears = age + three  # Compilation error: incorrect space indentation, needs to be in line with the 'three' variable;
                           

print ("The total number of years:" + str(answerYears))  # Syntax Error: Missing parentheses; Logical Error:'answerYears' is a variable,
                                                         # does not need the '"' ; Runtime Error:  'answerYears' needs to be casted to a string


answerMonths = (answerYears*12) + 6 # Runtime Error: Wrong variable name, needs to be 'answerYears' and not 'answer'
                                    # Logical Error: Needed a "+6" to give the right answer of 330    

print ("In 3 years and 6 months, I'll be " + str(answerMonths) + " months old") # Syntax Error; Missing parentheses; Runtime Error: 'answerMonths' needs to be casted to a string

#HINT, 330 months is the correct answer
