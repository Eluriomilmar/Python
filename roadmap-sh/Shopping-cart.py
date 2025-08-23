#Shopping cart program

foods = []
prices = []
total = 0

food = ""
price = 0

while True:
    food = input("Input which food you're going to buy(q exit): ")
    if food == "q":
        break
    else:
        price = float(input(f"What's the price of {food}? "))
        foods.append(food)
        prices.append(price)

for i in range(len(foods)):
    if i > 0:
        if prices[i] > prices[i-1]:
            aux = prices[i]
            prices[i] = prices[i-1]
            prices[i-1] = aux
            aux = foods[i]
            foods[i] = foods[i-1]
            foods[i-1] = aux
            i -= 1

for i in range(len(foods)):
    print(f"{foods[i]}: {prices[i]:.2f}")
    total += prices[i]
print(f"Total: R${total:.2f}")