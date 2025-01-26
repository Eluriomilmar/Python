import curses
from random import randint
import keyboard

"""Esse programa só é bem visualizado se executado fora da IDE"""

posicaoComida = [0, 0]
posicaoRabo = []

def imprimeTabuleiro(y, x):
    for i in range(y):
        for j in range(x):
            if i == 0 or i == 4:
                screen.addstr(i, j, "-")
            elif j == 0 or j == 4:
                screen.addstr(i, j, "|")
        screen.refresh()
    return y, x

def imprimeJogador(y = 1, x = 1, oldy = 1, oldx = 1):
    screen.addstr(oldy, oldx, " ")
    screen.addstr(y, x, "x")
    screen.refresh()
    return y, x


def imprimeComida(tamTabx = 5, tamTaby = 5 , jogadory = 0, jogadorx = 0):
    posicaoComida[0] = randint(1, tamTabx - 2)
    posicaoComida[1] = randint(1, tamTaby - 2)
    while posicaoComida[0] == jogadory and posicaoComida[1] == jogadorx:
        posicaoComida[0] = randint(1, tamTabx - 2)
        posicaoComida[1] = randint(1, tamTaby - 2)
    screen.addstr(posicaoComida[0], posicaoComida[1], "o")
    screen.refresh()

def mexeJogador(y, x, comiday, comidax):
    if keyboard.read_key() == "up":
        y, x = imprimeJogador(y - 1, x, y, x)
        if y == comiday and x == comidax:
            rabo = [y, x]
            posicaoRabo.append(rabo)
            imprimeComida(5,5, y, x)
        else:
            for i in range(len(posicaoRabo), 0, 1):
                if i != 0:
                    posicaoRabo[i] = posicaoRabo[i-1]
                else:
                    posicaoRabo[i] = [x, y]
    if keyboard.read_key() == "down":
        y, x = imprimeJogador(y + 1, x, y, x)
        if y == comiday and x == comidax:
            rabo = [y , x]
            posicaoRabo.append(rabo)
            imprimeComida(5,5, y, x)
        else:
            for i in range(len(posicaoRabo), 0, 1):
                if i != 0:
                    posicaoRabo[i] = posicaoRabo[i-1]
                else:
                    posicaoRabo[i] = [x, y]
    if keyboard.read_key() == "left":
        y, x = imprimeJogador(y, x - 1, y, x)
        if y == comiday and x == comidax:
            rabo = [y, x]
            posicaoRabo.append(rabo)
            imprimeComida(5,5, y, x)
        else:
            for i in range(len(posicaoRabo), 0, 1):
                if i != 0:
                    posicaoRabo[i] = posicaoRabo[i-1]
                else:
                    posicaoRabo[i] = [x, y]
    if keyboard.read_key() == "right":
        y, x = imprimeJogador(y, x + 1, y, x)
        if y == comiday and x == comidax:
            rabo = [y, x]
            posicaoRabo.append(rabo)
            imprimeComida(5,5, y, x)
        else:
            for i in range(len(posicaoRabo), 0, 1):
                if i != 0:
                    posicaoRabo[i] = posicaoRabo[i-1]
                else:
                    posicaoRabo[i] = [x, y]
    return y, x

def imprimeRabo():
    for i in range(len(posicaoRabo)):
        screen.addstr(10, 0, str(posicaoRabo))
        screen.refresh()

##gameplay init
screen = curses.initscr()
tamanhoTabuleiro = imprimeTabuleiro(5, 5)
posicaoJogador = imprimeJogador()
imprimeComida(tamanhoTabuleiro[0], tamanhoTabuleiro[1], posicaoJogador[0], posicaoJogador[1])
while True:
    posicaoJogador = mexeJogador(posicaoJogador[0], posicaoJogador[1], posicaoComida[0], posicaoComida[1])
    imprimeRabo()
