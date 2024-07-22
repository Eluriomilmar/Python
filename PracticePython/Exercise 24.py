def horizontal():
    return " --- "


def vertical():
    return "|    "


def imprime(n):
    for i in range(n):
        print(horizontal(), end="")
        if i == n-1:
            print("\n")
    for i in range(n+1):
        print(vertical(), end="")
        if i == n:
            print("\n")


def checagem():
    while True:
        try:
            i = int(input("Insira o tamanho do tabuleiro: "))
            if i < 1:
                raise ValueError
        except:
            print("Insira número inteiro maior que 0.")
        else:
            return i


a = checagem()
for i in range(a):
    imprime(a)
print(a*horizontal(), end="")