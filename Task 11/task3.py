swim = float(input("Enter time for swimming:\n"))
cyc = float(input("Enter time for cycling:\n"))
run = float(input("Enter time for running:\n"))
#===========================================================#
total = swim + cyc + run
qual_time = 100

#===========================================================#
if total <= qual_time:
    print("Award:Provincial Colours")
elif total > qual_time and total <= (qual_time+5):
    print("Award: Provincial Half Colours")
elif total > (qual_time+5) and total <=(qual_time+10):
    print("Award: Provincial Scroll")
else:
    print("Sorry, no award")

