from random import choice
import re
import curses

def palpite(palavra, tentativa=" ", erros=[], acertos=[], fim=0):
    if tentativa == " ":
        screen.addstr(0, 0, "Palavra: ")
        for i in range(len(palavra)):
            screen.addstr("_")
        screen.addstr(1, 0, "Erros: ")
        screen.addstr(3, 0, " _______")
        screen.addstr(4, 0, "|      ")
        screen.addstr(5, 0, "|      o")
        screen.addstr(6, 0, "|")
        screen.addstr(7, 0, "|")
        screen.addstr(8, 0, "|")
    screen.addstr(9, 0 ,"Tentativa: ")
    tentativa = screen.getkey().upper()
    screen.addstr(9, 11, tentativa)
    screen.refresh()
    while len(tentativa) != 1 or bool(re.search("[A-ZÀ-ÿ]", tentativa)) is False:
        try:
            screen.addstr("\nInsira letra de A a Z: ")
            tentativa = screen.getkey().upper()
            if len(tentativa) != 1 or bool(re.search("[A-ZÀ-ÿ]", tentativa)) is False:
                raise ValueError
        except:
            screen.addstr("\nInsira somente um caractere alfabético.")
    screen.clear()
    sequencia = 0
    acerto = 0
    screen.addstr(0, 0, "Palavra: ")
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
                screen.addstr(i)
                sequencia += 1
                screen.refresh()
            else:
                screen.addstr("_")
                screen.refresh()
    elif acerto == 0:
        if tentativa not in erros:
            erros.append(tentativa)
            fim += 1
        for i in palavra:
            if i in tentativa or i in acertos:
                screen.addstr(i)
                sequencia += 1
            else:
                screen.addstr("_")
    screen.addstr(1, 0, "Erros: ")
    for i in range(len(erros)):
        if i < len(erros)-1:
            screen.addstr(f"{erros[i]}, ")
            screen.refresh()
        else:
            screen.addstr(f"{erros[i]}.")
            screen.refresh()
    if fim == 0:
        screen.addstr(3, 0, " _______")
        screen.addstr(4, 0, "|      ")
        screen.addstr(5, 0, "|      o")
        screen.addstr(6, 0, "|")
        screen.addstr(7, 0, "|")
        screen.addstr(8, 0, "|")
    elif fim == 1:
        screen.addstr(3, 0, " _______")
        screen.addstr(4, 0, "|      ")
        screen.addstr(5, 0, "|      o")
        screen.addstr(6, 0, "|      |")
        screen.addstr(7, 0, "|")
        screen.addstr(8, 0, "|")
    elif fim == 2:
        screen.addstr(3, 0, " _______")
        screen.addstr(4, 0, "|      ")
        screen.addstr(5, 0, "|      o")
        screen.addstr(6, 0, "|      |")
        screen.addstr(7, 0, "|     /")
        screen.addstr(8, 0, "|")
    elif fim == 3:
        screen.addstr(3, 0, " _______")
        screen.addstr(4, 0, "|      ")
        screen.addstr(5, 0, "|      o")
        screen.addstr(6, 0, "|      |")
        screen.addstr(7, 0, "|     / \\ ")
        screen.addstr(8, 0, "|")
    elif fim == 4:
        screen.addstr(3, 0, " _______")
        screen.addstr(4, 0, "|      ")
        screen.addstr(5, 0, "|      o")
        screen.addstr(6, 0, "|     /|")
        screen.addstr(7, 0, "|     / \\ ")
        screen.addstr(8, 0, "|")
    if fim == 5:
        screen.addstr(3, 0, " _______")
        screen.addstr(4, 0, "|      ")
        screen.addstr(5, 0, "|      o")
        screen.addstr(6, 0, "|     /|\\ ")
        screen.addstr(7, 0, "|     / \\ ")
        screen.addstr(8, 0, "|")
    if fim == 6:
        screen.addstr(3, 0, " _______")
        screen.addstr(4, 0, "|      |")
        screen.addstr(5, 0, "|      x")
        screen.addstr(6, 0, "|     /|\\ ")
        screen.addstr(7, 0, "|     / \\ ")
        screen.addstr(8, 0, "|")
        screen.addstr(9, 0, f"Perdeu! A palavra era {palavra}\n")
        screen.refresh()
        cont = cont_ou_nao()
        screen.addstr(cont)
        if cont == "N":
            screen.addstr(11, 0, "\nEncerrando programa. Aperte ENTER para encerrar.")
            screen.getkey().upper()
            return 0
        else:
            screen.clear()
            return palpite(cria_lista("soletrando2.txt"), " ", [], [])
    if len(palavra) == sequencia:
        screen.addstr(10, 0, f"Venceu! A palavra é {palavra}.")
        cont = cont_ou_nao()
        if cont == "N":
            screen.addstr(11, 0, "\nEncerrando programa. Aperte ENTER para encerrar.")
            screen.getkey().upper()
            return 0
        else:
            return palpite(cria_lista("soletrando2.txt"), " ", [], [])
    screen.addstr("\n")
    return palpite(palavra, tentativa, erros, acertos, fim)


def desambig(desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim):
    for j in desambiguacao:
        if j in palavra:
            acerto += 1
            acertos.append(j)
            if acerto == 1:
                for i in palavra:
                    if i in desambiguacao or i in acertos:
                        screen.addstr(i)
                        sequencia += 1
                        screen.refresh()
                    else:
                        screen.addstr("_")
                        screen.refresh()
    if acerto == 0:
        for i in tentativa:
            if i not in erros:
                erros.append(i)
                fim += 1
        for i in palavra:
            if i in desambiguacao or i in acertos:
                screen.addstr(i)
                sequencia += 1
                screen.refresh()
            else:
                screen.addstr("_")
                screen.refresh()
    return desambiguacao, acerto, palavra, acertos, sequencia, tentativa, erros, fim

def cont_ou_nao():
    while True:
        try:
            screen.addstr(11, 0, "Deseja jogar mais(S/N)?")
            screen.refresh()
            argumento = screen.getkey().upper()
            if argumento != "S" and argumento != "N":
                raise ValueError
        except:
            print("Somente são aceitos os valores S e N.")
        else:
            return argumento


def cria_lista(arq):
    with open(arq, "r", encoding="UTF-8") as dicionario:
        vetor = dicionario.read().upper().split("\n")
        return choice(vetor)


screen = curses.initscr()
curses.noecho()
curses.cbreak()
palpite(cria_lista("soletrando2.txt"), " ", [], [])

