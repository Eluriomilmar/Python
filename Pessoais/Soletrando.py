from random import choice
import re


def palpite(palavra, tentativa=" ", erros=[], acertos=[]):
    if tentativa == " ":
        for i in range(len(palavra)):
            print("_", end="")
    tentativa = str(input("\nInsira letra da tentativa: ")).upper()
    while len(tentativa) != 1 or bool(re.search("[A-ZÀ-ÿ]", tentativa)) is False:
        try:
            tentativa = str(input("\nInsira letra de A a Z: ")).upper()
            if len(tentativa) != 1 or bool(re.search("[A-ZÀ-ÿ]", tentativa)) is False:
                raise ValueError
        except:
            print("\nInsira somente um caractere alfabético.")
    sequencia = 0
    if tentativa in palavra:
        acertos.append(tentativa)
        for i in palavra:
            if i in tentativa or i in acertos:
                print(i, end="")
                sequencia += 1
            else:
                print("_", end="")
    else:
        erros.append(tentativa)
        for i in palavra:
            if i in tentativa or i in acertos:
                print(i, end="")
                sequencia += 1
            else:
                print("_", end="")
    print(f"\nErros: {erros}")
    if len(erros) == 0:
        print("o")
    elif len(erros) == 1:
        print(" o")
        print(" |")
    elif len(erros) == 2:
        print(" o")
        print(" |")
        print("/")
    elif len(erros) == 3:
        print(" o")
        print(" |")
        print("/ \\ ")
    elif len(erros) == 4:
        print(" o")
        print("/|")
        print("/ \\ ")
    if len(erros) == 5:
        print(" o")
        print("/|\\ ")
        print("/ \\ ")
    if len(erros) == 6:
        print(" x")
        print("/|\\ ")
        print("/ \\ ")
        return print(f"Perdeu! Encerrando programa. A palavra era {palavra}")
    if len(palavra) == sequencia:
        return print(f"Venceu! A palavra é {palavra}.\n\nEncerrando programa")
    return palpite(palavra, tentativa, erros, acertos)


def cria_lista(arq):
    with open(arq, "r") as dicionario:
        vetor = dicionario.read().upper().split("\n")
        return choice(vetor)


palpite(cria_lista("soletrando2.txt"), " ", [], [])