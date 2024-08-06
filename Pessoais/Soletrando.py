from random import choice
import re
import keyboard


def palpite(palavra, tentativa=" ", erros=[], acertos=[], fim=0):
    if tentativa == " ":
        print("Palavra: ", end="")
        for i in range(len(palavra)):
            print("_", end="")
        print("")
        print("\nErros: ", end ="")
        print("\n _______")
        print("|      ")
        print("|      o")
        print("|")
        print("|")
        print("|\n")
    print("Tentativa: ", end="", flush=True)
    tentativa = keyboard.read_hotkey(suppress=False).upper()
    print(tentativa)
    while len(tentativa) != 1 or bool(re.search("[A-ZÀ-ÿ]", tentativa)) is False:
        try:
            print("\nInsira letra de A a Z: ", end="")
            tentativa = keyboard.read_hotkey(suppress=False).upper()
            if len(tentativa) != 1 or bool(re.search("[A-ZÀ-ÿ]", tentativa)) is False:
                raise ValueError
        except:
            print("\nInsira somente um caractere alfabético.")
    sequencia = 0
    acerto = 0
    print("\nPalavra: ", end="")
    if tentativa in ["A", "Á", "À", "Ã", "Â"]:
        desambiguacao = ["A", "Á", "À", "Ã", "Â"]
        desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim = desambig(
            desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim)
    elif tentativa in ["E", "É", "È", "Ê"]:
        desambiguacao = ["E", "É", "È", "Ê"]
        desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim = desambig(
            desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim)
    elif tentativa in ["I", "Í", "Ì", "Î", "Ï"]:
        desambiguacao = ["I", "Í", "Ì", "Î", "Ï"]
        desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim = desambig(
            desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim)
    elif tentativa in ["O", "Ó", "Ò", "Ô", "Õ"]:
        desambiguacao = ["O", "Ó", "Ò", "Ô", "Õ"]
        desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim = desambig(
            desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim)
    elif tentativa in ["U", "Ú", "Ù", "Û"]:
        desambiguacao = ["U", "Ú", "Ù", "Û"]
        desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim = desambig(
            desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim)
    elif tentativa in palavra and len(tentativa) == 1:
        acertos.append(tentativa)
        for i in palavra:
            if i in tentativa or i in acertos:
                print(i, end="")
                sequencia += 1
            else:
                print("_", end="")
    elif acerto == 0:
        erros.append(tentativa)
        fim += 1
        for i in palavra:
            if i in tentativa or i in acertos:
                print(i, end="")
                sequencia += 1
            else:
                print("_", end="")
    print(f"\n\nErros: ", end="")
    for i in range(len(erros)):
        if i < len(erros)-1:
            print(f"{erros[i]}, ", end="")
        else:
            print(f"{erros[i]}.", end="")
    if fim == 0:
        print("\n _______")
        print("|      ")
        print("|      o")
        print("|")
        print("|")
        print("|")
    elif fim == 1:
        print("\n _______")
        print("|      ")
        print("|      o")
        print("|      |")
        print("|")
        print("|")
    elif fim == 2:
        print("\n _______")
        print("|      ")
        print("|      o")
        print("|      |")
        print("|     /")
        print("|")
    elif fim == 3:
        print("\n _______")
        print("|      ")
        print("|      o")
        print("|      |")
        print("|     / \\ ")
        print("|")
    elif fim == 4:
        print("\n _______")
        print("|      ")
        print("|      o")
        print("|     /|")
        print("|     / \\ ")
        print("|")
    if fim == 5:
        print("\n _______")
        print("|      ")
        print("|      o")
        print("|     /|\\ ")
        print("|     / \\ ")
        print("|")
    if fim == 6:
        print("\n _______")
        print("|      |")
        print("|      x")
        print("|     /|\\ ")
        print("|     / \\ ")
        print("|")
        print(f"Perdeu! A palavra era {palavra}\n")
        cont = cont_ou_nao()
        if cont == "N":
            return input("\nEncerrando programa. Aperte ENTER para encerrar.", flush=True)
        else:
            return palpite(cria_lista("soletrando2.txt"), " ", [], [])
    if len(palavra) == sequencia:
        print(f"Venceu! A palavra é {palavra}.\n", flush=True)
        cont = cont_ou_nao()
        if cont == "N":
            return input("\nEncerrando programa. Aperte ENTER para encerrar.", flush=True)
        else:
            return palpite(cria_lista("soletrando2.txt"), " ", [], [])
    print("\n", end="")
    return palpite(palavra, tentativa, erros, acertos, fim)


def desambig(desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim):
    for j in desambiguacao:
        if j in palavra:
            acerto += 1
            acertos.append(j)
            if acerto == 1:
                for i in palavra:
                    if i in desambiguacao or i in acertos:
                        print(i, end="")
                        sequencia += 1
                    else:
                        print("_", end="")
    if acerto == 0:
        for i in tentativa:
            erros.append(i)
        fim += 1
        for i in palavra:
            if i in desambiguacao or i in acertos:
                print(i, end="")
                sequencia += 1
            else:
                print("_", end="")
    return desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim

def cont_ou_nao():
    while True:
        try:
            print("Deseja jogar mais(S/N)? ", end="", flush=True)
            argumento = keyboard.read_hotkey(suppress=False).upper()
            if argumento != "S" and argumento != "N":
                raise ValueError
        except:
            print("Somente são aceitos os valores S e N.")
        else:
            return argumento


def cria_lista(arq):
    with open(arq, "r", encoding="latin-1") as dicionario:
        vetor = dicionario.read().upper().split("\n")
        return choice(vetor)


palpite(cria_lista("soletrando2.txt"), " ", [], [])
