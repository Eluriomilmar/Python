menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25
}

cart = []
total = 0
header = ("valores", "preços")
print(f"{header[0]:10}: {header[1]}")
print("------------------")
for key,value in menu.items():
    print(f"{key:10}: R${value:.2f}")
print("------------------")
sentinel = -1
while sentinel != "q":
    sentinel = input("Which item you'd like to buy? ").lower()
    if sentinel != "q":
        if menu.get(sentinel) is not None:
            cart.append(sentinel)
for snack in cart:
    if snack in menu:
        total += menu.get(snack)
print(f"Total: R${total:.2f}")