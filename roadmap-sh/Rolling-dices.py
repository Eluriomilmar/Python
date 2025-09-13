from random import randint
#● ┌ ─ ┐ │ └ ┘

dice_art = {
    6: ("┌ ─ ─ ─ ┐","│ ● ● ● │","│       │","│ ● ● ● │","└ ─ ─ ─ ┘"),
    5: ("┌ ─ ─ ─ ┐","│ ●   ● │","│   ●   │","│ ●   ● │","└ ─ ─ ─ ┘"),
    4: ("┌ ─ ─ ─ ┐","│ ●   ● │","│       │","│ ●   ● │","└ ─ ─ ─ ┘"),
    3: ("┌ ─ ─ ─ ┐","│     ● │","│   ●   │","│ ●     │","└ ─ ─ ─ ┘"),
    2: ("┌ ─ ─ ─ ┐","│     ● │","│       │","│ ●     │","└ ─ ─ ─ ┘"),
    1: ("┌ ─ ─ ─ ┐","│       │","│   ●   │","│       │","└ ─ ─ ─ ┘")
}

def main():
    amount_dice = int(input("How many dice do you want to roll? "))
    total = 0
    dices = []
    while amount_dice > 0:
        dices.append(randint(1,6))
        amount_dice -= 1

    for line in range(5):
        for dice in dices:
            print(dice_art.get(dice)[line], end="")
        print("", end="\n")
    for num in range(len(dices)):
        total += dices[num]
    print(f"\nTotal: {total}")


main()

