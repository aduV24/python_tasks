# This program allows a user to calculate their interest on an investment or 
# calculate the amount that should be repaid on a home loan each month
# Depending on their choice, they input some info and a formula is used to calcutate 
# the interest or monthly payment plan.

import math

print("Choose either 'investment or 'bond' from the menu below to proceed:\n")
print("Investment\t - to calculate the amount of interest you'llearn on interest")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan")
choice = input()

print()

#=================================================================================#
#     If the user chooses investment, the following operations are performed

if choice.lower() == "investment":
    deposit = float(input("Enter deposit amount:\n"))
    rate = float(input("Enter interest rate(as a percentage):\n"))
    year = int(input("Enter the number of years for investing:\n"))
    interest = input("Choose either 'simple' or 'compound' interest:\n")
    
    rate = rate / 100
    
    # Calculate and display the total return in investment based on their choice
    # (simple or compund)
    
    if interest.lower() == 'simple':
        amount = round(deposit * (1+rate*year),2)
        print()
        print(f"The total return on investment is {amount}")
   
    elif interest.lower() == "compound":
        amount = deposit * (math.pow((1+rate),year))
        amount = round(amount,2)
        print()
        print(f"The total return on investment is {amount}")
    
    else:
        print("Error, Enter either 'simple' or 'compound'")

#=================================================================================#
# Else If the user chooses bond, the following operations are performed

elif choice.lower() == "bond":
    value = float(input("Enter the present value of the house:\n"))
    rate = float(input("Enter interest rate:\n"))
    months = int(input("Enter the no of months you plan to repay the bond:\n"))

    # Calculate and display amount to be repaid every month
    
    m_rate = rate / 12
    
    m_repay = (m_rate * value) /(1- math.pow(1+m_rate,(-months)))
    m_repay =round(m_repay,2)

    print()
    
    print(f"According to the information you've provided, you'll have to repay {m_repay} every month.")

#=================================================================================#

else:
    print("Error, Enter either 'investment' or 'bond'")
    




