"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function."""


def define_func():
    F = []
    while True:
        try:
            a = str(input("Insira número a ser adicionado na lista, SAIR para sair: "))
            if a.upper() == "SAIR":
                return F
        except:
            print("Insira valor numérico.")
        else:
            F.append(int(a))


def nova_lista(L):
    F = []
    F.append(L[0])
    if len(L) > 1:
        F.append(L[len(L)-1])
    return F


print(nova_lista(define_func()))