"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
    If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
def inteiro():
    while True:
        try:
            a = int(input("Insira número inteiro: "))
        except:
            print("Somente números inteiros são aceitos por este programa: ")
        else:
            return a
def divisivel(n):
    if n%4 == 0:
        print(f"O número {n} ", end = "")
        return 4
    elif n%2 == 0:
        print(f"O número {n} ", end = "")
        return 2
    else:
        print(f"O número {n} ", end = "")
        return 1

def resposta(n):
    if n == 4:
        print("é divisível por 4.")
    elif n == 2:
        print("é par.")
    else:
        print("é ímpar.")

resposta(divisivel(inteiro()))