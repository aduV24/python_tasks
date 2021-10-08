weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
BMI = round(weight/(height*height),2)
if BMI >= 30:
    print(f"your BMI is {BMI},you are obese")
elif BMI>=25:
    print(f"your BMI is {BMI},you are overweight")
elif BMI>=18.5:
    print(f"your BMI is {BMI},you are normal")
else:
    print(f"your BMI is {BMI},you are underweight")