have_length = False
up_case = False
low_case = False
have_num = False
check = 0
#==============================================#
length = input("Is your password at least 6 characters? (Yes or No): ")
if length == "Yes":
    have_length = True
    
upper_case = input("Does your password have uppper case characters? (Yes or No): ")
if upper_case == "Yes":
    up_case = True

lower_case = input("Does your password have lower case characters? (Yes or No): ")
if lower_case == "Yes":
    low_case = True

num = input("Does your password have numerical characters? (Yes or No): ")
if num == "Yes":
    have_num = True

#===============================================#
if have_length:
    check+=1
if up_case:
    check+=1
if low_case:
    check+=1
if have_num:
    check+=1

#===============================================#
if check >= 3:
    print("This is a suitable password")