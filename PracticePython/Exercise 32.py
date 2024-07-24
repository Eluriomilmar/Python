from random import choice


def palpite(palavra, tentativa=" ", erros=[], acertos=[]):
    if tentativa == " ":
        for i in range(len(palavra)):
            print("_", end="")
    tentativa = str(input("\nInsira letra da tentativa: ")).upper()
    while len(tentativa) > 1:
        try:
            tentativa = str(input("\nInsira letra da tentativa: ")).upper()
            if len(tentativa) > 1:
                raise ValueError
        except:
            print("Insira somente um caractere.")
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
        vetor = dicionario.read().split("\n")
        return choice(vetor)


palpite(cria_lista("sowpods.txt"), " ", [], [])
