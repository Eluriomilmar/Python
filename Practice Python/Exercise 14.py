"""Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates."""


def cria():
    func = []
    while True:
        try:
            a = str(input("Insira nome a ser adicionado na lista, digite sair para encerrar o programa: "))
        except:
            print("Valor inválido, tente novamente.")
        else:
            if a.upper() == "SAIR":
                return func
            else:
                func.append(a)


def exclui_repetidos(l):
    l = set(l)
    l = list(l)
    return l


print(exclui_repetidos(cria()))
