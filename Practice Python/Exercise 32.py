from random import choice


def palpite(palavra, tentativa=" ", erros=[], acertos=[]):
    if tentativa == " ":
        for i in range(len(palavra)):
            print("_", end="")
    tentativa = str(input("\nInsira letra da tentativa: ")).upper()
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
    print(f"\nErros: {erros}")
    if len(erros) == 6:
        return print(f"Perdeu! Encerrando programa. A palavra era {palavra}")
    if len(palavra) == sequencia:
        return print(f"Venceu! A palavra é {palavra}.\n\nEncerrando programa")
    return palpite(palavra, tentativa, erros, acertos)


def cria_lista(arq):
    with open(arq, "r") as dicionario:
        vetor = dicionario.read().split("\n")
        return choice(vetor)


palpite(cria_lista("sowpods.txt"), " ", [], [])
