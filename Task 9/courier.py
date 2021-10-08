package_price=float(input("Enter the price of the package: "))
distance = float(input("Enter the total distance in kms: "))
#=====================================================================#
transport = input("What mode of transport would you like? (air or freight): ")
if transport == "air":
    trans = distance * 0.36
else:
    if transport == "freight":
        trans = distance * 0.25
#=====================================================================#
insurance = input("Choose a type of insurance(full or limited): ")
if insurance == "full":
    insur = 50.00
else:
    if insurance == "limited":
        insur = 25.00
#=====================================================================#
gift = input("Do you want it gift wrapped?(yes or no): ")
if gift == "yes":
    gft = 15.00
else:
    if gift == "no":
        gft =0.00
#=====================================================================#
delivery = input("Choose a type of delivery(priority or standand): ")
if delivery == "priority":
    dlvry = 100.00
else:
    if delivery == "standard":
        dlvry = 20.00
#=====================================================================#
total = round(package_price + trans + insur + gft + dlvry,2)
print()
print(f"package price: {package_price}")
print(f"transport fare: {trans}")
print(f"insurance: {insur}")
print(f"gift wrapping: {gft}")
print(f"delivery: {dlvry}")

print (f"The total price is {total}")
 