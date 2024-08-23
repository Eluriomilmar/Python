import curses, copy

def desenha_tabuleiro():
    for i in range(11):
        screen.addstr(3, i, "-")
        screen.addstr(7, i, "-")
    for i in range(11):
        screen.addstr(i, 3, "|")
        screen.addstr(i, 7, "|")
    screen.refresh()


def inicializa_jogo():
    tabuleiro = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    return tabuleiro


def verifica_jogada(x, y, jogo, jogador):
    if x <= 2 and y <= 2:
        jogo = preenche_tabuleiro(0, 0, jogador, jogo)
        return jogo
    elif x <= 2 and y <= 6:
        jogo = preenche_tabuleiro(0, 1, jogador, jogo)
        return jogo
    elif x <= 2 and y <= 10:
        jogo = preenche_tabuleiro(0, 2, jogador, jogo)
        return jogo
    elif x <= 6 and y <= 2:
        jogo = preenche_tabuleiro(1, 0, jogador, jogo)
        return jogo
    elif x <= 6 and y <= 6:
        jogo = preenche_tabuleiro(1, 1, jogador, jogo)
        return jogo
    elif x <= 6 and y <= 10:
        jogo = preenche_tabuleiro(1, 2, jogador, jogo)
        return jogo
    elif x <= 10 and y <= 2:
        jogo = preenche_tabuleiro(2, 0, jogador, jogo)
        return jogo
    elif x <= 10 and y <= 6:
        jogo = preenche_tabuleiro(2, 1, jogador, jogo)
        return jogo
    elif x <= 10 and y <= 10:
        jogo = preenche_tabuleiro(2, 2, jogador, jogo)
        return jogo

def preenche_tabuleiro(cx, cy, jogador, jogo):
    if jogo[cy][cx] == 0:
        jogo[cy][cx] = jogador
        if jogador == 1:
            screen.addstr(cy*4+1, cx*4+1, "x")
            screen.refresh()
        elif jogador == -1:
            screen.addstr(cy*4+1, cx*4+1, "o")
            screen.refresh()
        return jogo
    else:
        return jogo


def verifica_vencedor(jogo):
    coluna = [0, 0, 0]
    for i in range(3):
        linha = 0
        for j in range(3):
            linha = linha + jogo[i][j]
            if linha == 3:
                return 1
            elif linha == -3:
                return 2
            coluna[j] = coluna[j] + jogo[i][j]
            if coluna[j] == 3:
                return 1
            elif coluna[j] == -3:
                return 2
    if jogo[0][0] + jogo[1][1] + jogo[2][2] == 3:
        return 1
    if jogo[0][0] + jogo[1][1] + jogo[2][2] == -3:
        return 2
    if jogo[2][0] + jogo[1][1] + jogo[0][2] == 3:
        return 1
    if jogo[2][0] + jogo[1][1] + jogo[0][2] == -3:
        return 2
    return 0


screen = curses.initscr()
screen.keypad(1)
curses.noecho()
curses.mousemask(1)
curses.curs_set(1)
desenha_tabuleiro()
jogo = inicializa_jogo()
jogador1 = 1
jogador2 = -1
i = 0
while i < 9:
    screen.getch()
    _, x, y, _, _ = curses.getmouse()
    screen.refresh()
    retorno = copy.deepcopy(jogo)
    if i%2 == 0:
        jogo = verifica_jogada(x, y, jogo, jogador1)
        i += 1
        if retorno == jogo:
            i -= 1
        if verifica_vencedor(jogo) != 0:
            screen.addstr(14, 0, f"Jogador 1 Venceu!")
            curses.echo()
            screen.addstr(15, 0, f"Aperte ENTER para encerrar")
            screen.refresh()
            screen.getch()
            exit()
    else:
        jogo = verifica_jogada(x, y, jogo, jogador2)
        i += 1
        if retorno == jogo:
            i -= 1
        if verifica_vencedor(jogo) != 0:
            screen.addstr(14, 0, f"Jogador 2 Venceu!")
            curses.echo()
            screen.addstr(15, 0, f"Aperte ENTER para encerrar")
            screen.refresh()
            screen.getch()
            exit()

