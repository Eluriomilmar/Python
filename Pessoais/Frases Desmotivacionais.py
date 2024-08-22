import curses
from random import choice

def printa_menu():
    screen.addstr(0, 0, "O que deseja fazer? ")
    screen.addstr(1, 0, "1: Ler frase desmotivacional")
    screen.addstr(2, 0, "2: Inserir nova frase desmotivacional no banco")
    screen.addstr(3, 0, "3: Encerrar o programa")


def checa_numero():
    while True:
        try:
            screen.addstr(4, 0, "Insira opção(1-3): ")
            opcao = screen.getkey()
            screen.addstr(f"{opcao}")
            if int(opcao) < 1 or int(opcao) > 3:
                raise ValueError
        except:
            screen.addstr(5, 0, "Insira somente valores de 1 a 3! ")
            screen.refresh()
        else:
            break
    return int(opcao)


def opcoes(num):
    if num == 1:
        with open("Frases Desmotivacionais.txt", "r", encoding="ISO-8859-1") as arq:
            frase = arq.read().split("\n")
            escolha = choice(frase)
            screen.clear()
            screen.refresh()
            printa_menu()
            screen.addstr(6, 0, f"{escolha}")
            screen.refresh()
    elif num == 2:
        with open("Frases Desmotivacionais.txt", "a", encoding="ISO-8859-1") as arq:
            screen.addstr(7, 0, "Insira a frase a ser adicionada: ")
            curses.echo()
            nova_frase = screen.getstr()
            nova_frase = str(nova_frase)
            nova_frase = nova_frase[2:-1]
            arq.write("\n")
            arq.write(nova_frase)
            screen.addstr(10, 0, "Frase adicionada com sucesso, aperte ENTER para prosseguir.")
            screen.refresh()
            curses.noecho()
            screen.getch()
            screen.clear()
    elif num == 3:
        screen.addstr(10, 0, "O programa está sendo encerrado, aperte ENTER para finalizar.")
        screen.refresh()
        screen.getch()



screen = curses.initscr()
curses.noecho()
opcao = 0
while opcao != 3:
    printa_menu()
    opcao = checa_numero()
    opcoes(opcao)