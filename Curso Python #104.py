"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt(‘Digite um n: ‘)"""

def leiaInt(a = "coisa"):
    original = a
    while True:
        if a.isnumeric() == False:
            print("Erro! Insira valor numérico: ", end ="")
            a = str(input(""))
            original = a
        if "-" in a:
            a.replace("-", "1")
        if "." in a:
            a.replace(".", "1")
        if a.isdigit() == True:
            return original

a = str(input("Digite um n: "))
print(leiaInt(a))