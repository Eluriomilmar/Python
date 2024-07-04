"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
"""

import datetime

def pessoa():
    while True:
        try:
            nome = str(input("Insira o nome do usuário: "))
            ano = int(input("Insira a idade do usuário: "))
            if ano < 0:
                raise ValueError
        except:
            print("Input inválido, insira número inteiro!")
        else:
            return nome, ano


def repeticoes():
    while True:
        try:
            ciclos = int(input("Insira quantas vezes deseja repetir a mensagem: "))
            if ciclos < 1:
                raise ValueError
        except:
            print("Input inválido, insira número inteiro!")
        else:
            return ciclos


nome, ano = pessoa()
ciclos = repeticoes()
for i in range(ciclos):
    print(f"O usuário {nome} completará 100 anos em {100 - ano} anos, em {datetime.date.today().year - ano + 100}\n")