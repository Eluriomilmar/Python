"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number."""

def resto(a):
    for x in range(1, a+1):
        if a%x == 0:
            print(f"{x} é divisor de {a}")

def inteiro():
    while True:
        try:
            a = (int(input("Insira número inteiro: ")))
            if a < 1:
                raise ValueError
        except:
            print("Insira número inteiro!")
        else:
            return a


resto(inteiro())