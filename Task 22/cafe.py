# This program calculates the total worth stock in a cafe using lists,
# dictionaries and loops

menu = ['Espresso', 'Capuccino', 'Chicken Sandwich', 'Hot chocolate']
stock = {menu[0]: 24, menu[1]: 30, menu[2]: 50, menu[3]: 56}
price = {menu[0]: 35, menu[1]: 22, menu[2]: 45, menu[3]: 20}

stock_worth = {}
total = 0
# loop through the price dictionary,multiply price and stock
# and find the total
for x in price:
    stock_worth[x] = stock[x] * price[x]
    total += stock_worth[x]

# Display the results
print("Stock")
print("---------------------------------------")
for keys, values in stock_worth.items():
    print(f"{keys.ljust(31)} R {values}")

print("---------------------------------------")
print(f"Total \t\t\t\tR {total}")
