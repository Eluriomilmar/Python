"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right."""


"""Tem algo errado aqui e eu não sei o que é"""


from random import randint


def palpite():
    a = -1
    while int(a) < 1 or int(a) > 9 or a.upper() == "SAIR":
        try:
            a = str(input("Tente adivinhar número sorteado de 1 a 9: "))
        except ValueError:
            print("Só são válidos valores de 1 a 9.")
        else:
            if a.upper() == "SAIR":
                return -1
            else:
                a = int(a)
                return a


def sorteio():
    a = randint(1, 9)
    return a


def checagem(a, b):
    tentativas = 1
    while a != b:
        if a == -1:
            break
        else:
            print("Errou! Tente novamente.")
            a = palpite()
            tentativas += 1
    if a == -1:
        return False
    else:
        return tentativas

if checagem(palpite(), sorteio()) == False:
    print("Programa fechado com sucesso.")
else:
    print(f"Você acertou com {checagem(palpite(), sorteio())} tentativas!")
