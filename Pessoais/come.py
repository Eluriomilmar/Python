import curses
from random import randint
import keyboard

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


def imprimeComida(tamTabx = 5, tamTaby = 5 , jogadory=0, jogadorx=0):
    comiday = jogadory
    comidax = jogadorx
    while comiday == jogadory and comidax == jogadorx:
        comiday = randint(1, tamTabx - 2)
        comidax = randint(1, tamTaby - 2)
    screen.addstr(comiday, comidax, "o")
    screen.refresh()
    return comiday, comidax

def mexeJogador(y, x, comiday, comidax):
    if keyboard.read_key() == "up":
        y, x = imprimeJogador(y - 1, x, y, x)
        if y == comiday and x == comidax:
            imprimeComida(5,5, y, x)
    if keyboard.read_key() == "down":
        y, x = imprimeJogador(y + 1, x, y, x)
        if y == comiday and x == comidax:
            imprimeComida(5,5, y, x)
    if keyboard.read_key() == "left":
        y, x = imprimeJogador(y, x - 1, y, x)
        if y == comiday and x == comidax:
            imprimeComida(5,5, y, x)
    if keyboard.read_key() == "right":
        y, x = imprimeJogador(y, x + 1, y, x)
        if y == comiday and x == comidax:
            imprimeComida(5,5, y, x)
    return y, x


##gameplay init
screen = curses.initscr()
tamanhoTabuleiro = imprimeTabuleiro(5, 5)
posicaoJogador = imprimeJogador()
posicaoComida  = imprimeComida(tamanhoTabuleiro[0], tamanhoTabuleiro[1], posicaoJogador[0], posicaoJogador[1])
while True:
    posicaoJogador = mexeJogador(posicaoJogador[0], posicaoJogador[1], posicaoComida[0], posicaoComida[1])
