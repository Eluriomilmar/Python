from random import choice

def spin_row():
    symbols = ["🍒","🍉","🍋","🔔","⭐"]
    return [choice(symbols) for _ in range(3)]

def print_row(row):
    print(" ".join(row))

def get_payout(row, bet):
    equal = 0
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            equal += 1
    if equal == 2:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    else:
        return 0


def main():
    balance = 100
    print("_" * 20, end="")
    print("\nSymbols:🍒🍉🍋🔔⭐\n", end="")
    print("_" * 20)
    while balance > 0:
        print(f"Current balance: R${balance:.2f}")
        bet = int(input("Place your bet amount: "))
        if bet > balance or bet < 1:
            print("Invalid bet")
            while bet > balance or bet < 1:
                int(input("Insert bet amount: "))
        balance -= bet
        print(f"{balance}")
        row = spin_row()
        print_row(row)
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won R${payout}")
        else:
            print("You lost this time")
        balance += payout
        game_on = input("Do you wish to continue? (Y/N): ").upper()
        if game_on == "N":
            break
        print(f"Game over. Final balance: R${balance}")

if __name__ == "__main__":
    main()