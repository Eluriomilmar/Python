def show_balance():
    print("_" * 30, end = "")
    print(f"\nYour balance is R${balance:.2f}\n", end = "")
    print("_" * 30, end = "")

def deposit(value):
    global balance
    balance += value
    show_balance()

def withdraw(value):
    global balance
    if value <= balance:
        balance -= value
    else:
        print(f"\nInvalid operation due to not having enough money.")
    show_balance()

balance = 0
is_running = True
def main():
    global is_running
    print(f"_" * 30, end="")
    print(f"\nBanking Program\n")
    print(f"_" * 30, end="")
    while is_running:
        print(f"\n1. Show Balance"
              f"\n2. Deposit"
              f"\n3. Withdraw"
              f"\n4. Exit")
        option = input(f"\nInsert option: ")
        if option == "1":
            show_balance()
        elif option == "2":
            value = float(input("Insert your deposit value: "))
            deposit(value)
        elif option == "3":
            value = float(input("Insert your withdrawal value: "))
            withdraw(value)
        elif option == "4":
            is_running = False
        else:
            option = input(f"\nOnly inputs 1-4 are valid, press enter to continue.")

if __name__ == "__main__":
    main()
