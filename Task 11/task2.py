shape = input("Enter the shape of the builing(square,rectangular or round):\n")
if shape == "square":
    length = float(input("Enter the length of one side:\n"))
    area = round(length**2,2)
    print(f"The area that will be taken up by the building is {area}sqm")
#=================================================================================#
elif shape == "rectangle":
    length = float(input("Enter the length of one side:\n"))
    width =float(input("Enter the width:\n"))
    area = round(length*width,2)
    print(f"The area that will be taken up by the building is {area}sqm")
#=================================================================================#
elif shape == "round":
    import math 
    radius = float(input("Enter the radius:\n"))
    area = round((math.pi)*(radius**2),2)
    print(f"The area that will be taken up by the building is {area}sqm")