#Reques item names from user
item1 = input("Enter name of first item: ")
item2 = input("Enter name of second item: ")
item3 = input("Enter name of third item: ")
print()

#Request item prices from user
print("Enter the price for each item below in two decimal places:")
price1 = float(input("Item1: "))
price2 = float(input("Item2: "))
price3 = float(input("Item3: "))

#Calculate total and average
#looked up the round function https://www.w3schools.com/python/ref_func_round.asp
total = round(price1+price2+price3,2) 
average = round(total/3,2)
print()

#Display items, total and average
print(f"The Total of {item1}, {item2}, {item3}, is R{total} and the average price of the items is R{average}")
