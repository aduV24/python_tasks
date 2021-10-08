# This program calculaets the total cost for a holiday using functions

# This function returns the cost for the hotel
def hotel_cost(num):
    cost_p_night = 450
    return cost_p_night * num


# Depending on the city, this function returns the travelling cost
def plane_cost(city):
    if city.title() == "Paris":
        return 150
    elif city.title() == "Mumbai":
        return 500
    elif city.title() == "California":
        return 250
    elif city.title() == "Texas":
        return 200
    elif city.title() == "Lagos":
        return 350
    elif city.title() == "Pretoria":
        return 150


# This funbtion returns the cost for car hire
def car_rental(num):
    cost_of_rental = 100
    return cost_of_rental * num


# This function calculates and returns the total cost for the holiday
def holiday_cost(nights, city, days):
    return hotel_cost(nights) + plane_cost(city) + car_rental(days)


print("Welcome to our holiday budgeting calculator")
print("-----------------------------------------------")

print("Available cities are Paris, Mumbai, California, Texas, Lagos, and"
      "Pretoria")

cities = ["Paris", "Mumbai", "California", "Texas", "Lagos", "Pretoria"]

# Ask for destination
destination = input("Please enter a destination:\n")
while destination.title() not in cities:
    destination = input("Please input one of the cities above:\n")

# Ask if staying in a hotel
hotel = input("Are you staying in a hotel?(y/n)")
while hotel != 'y' and hotel != 'n':
    hotel = input("Please give a y/n:\n")
if hotel == 'y':
    stay = int(input("How many nights:\n"))

# Ask if a car is needed
car = input("Do you need a car to drive on arrival?(y/n):\n")
while car != 'y' and car != 'n':
    car = input("Please give a y/n:\n")
if car == 'y':
    car_rent = int(input("For how many days: \n"))
print()

print("This is the breakdown for the total cost of your holiday")

# Display breakdown according to the information given
if hotel == 'y' and car == 'y':
    print(f"Flight to {destination}:".ljust(30), plane_cost(destination))
    print("Hotel:".ljust(30), hotel_cost(stay))
    print("Car Hire:".ljust(30), car_rental(car_rent))
    print("-----------------------------------------------")
    print("Total".ljust(30), holiday_cost(stay, destination, car_rent))

elif hotel == 'y' and car == 'n':
    print(f"Flight to {destination}:".ljust(30), plane_cost(destination))
    print("Hotel:".ljust(30), hotel_cost(stay))
    print("Car Hire:".ljust(30), car_rental(0))
    print("-----------------------------------------------")
    print("Total".ljust(30), holiday_cost(stay, destination, 0))

elif hotel == 'n' and car == 'y':
    print(f"Flight to {destination}:".ljust(30), plane_cost(destination))
    print("Hotel:".ljust(30), hotel_cost(0))
    print("Car Hire:".ljust(30), car_rental(car_rent))
    print("-----------------------------------------------")
    print("Total".ljust(30), holiday_cost(0, destination, car_rent))

else:
    print(f"Flight to {destination}:".ljust(30), plane_cost(destination))
    print("Hotel:".ljust(30), hotel_cost(0))
    print("Car Hire:".ljust(30), car_rental(0))
    print("-----------------------------------------------")
    print("Total".ljust(30), holiday_cost(0, destination, 0))
