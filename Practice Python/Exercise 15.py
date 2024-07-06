"""Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order."""


def frase():
    try:
        a = str(input("Insira frase a ser invertida aqui: "))
    except:
        print("Erro! Tente novamente.")
    else:
        return a


def inverte(a):
    a = "".join(a)
    a = a.split()
    a = a[::-1]
    a = " ".join(a)
    return a


print(inverte(frase()))