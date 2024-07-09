def horizontal(jogo):
        for i in range(len(jogo)):
                jogador1 = 0
                jogador2 = 0
                for j in range(len(jogo[i])):
                        if jogo[i][j] != 0:
                                if jogo[i][j] == 1:
                                        jogador1 += jogo[i][j]
                                else:
                                        jogador2 += jogo[i][j]
                if jogador1 == 3 or jogador2 == 6:
                        if jogador1 == 3:
                                return 1
                        else:
                                return 2


def vertical(jogo):
        for i in range(3):
                jogador1 = 0
                jogador2 = 0
                for j in range(3):
                        if jogo [j][i] != 0:
                                if jogo [j][i] == 1:
                                        jogador1 += jogo[j][i]
                                else:
                                        jogador2 += jogo[j][i]
                if jogador1 == 3 or jogador2 == 6:
                        if jogador1 == 3:
                                return 1
                        else:
                                return 2


def transversal1(jogo):
        jogador1 = 0
        jogador2 = 0
        for i in range(3):
                for j in range(3):
                        if i == j:
                                if jogo [i][j] != 0:
                                        if jogo [i][j] == 1:
                                                jogador1 += 1
                                        else:
                                                jogador2 += 2
        if jogador1 == 3:
                return 1
        if jogador2 == 6:
                return 2


def transversal2(jogo):
        jogador1 = 0
        jogador2 = 0
        for i in range(3):
                for j in range(3):
                        if i == 0 and j == 2:
                                if jogo[i][j] != 0:
                                        if jogo[i][j] == 1:
                                                jogador1 += 1
                                        else:
                                                jogador2 += 2
                        if i == 1 and j == 1:
                                if jogo [i][j] != 0:
                                        if jogo[i][j] == 1:
                                                jogador1 += 1
                                        else:
                                                jogador2 += 2
                        if i == 2 and j == 0:
                                if jogo[i][j] != 0:
                                        if jogo[i][j] == 1:
                                                jogador1 += 1
                                        else:
                                                jogador2 += 2

        if jogador1 == 3:
                return 1
        if jogador2 == 6:
                return 2


def juncao(partida):
        if horizontal(partida) != None:
                return horizontal(partida)
        if vertical(partida) != None:
                return vertical(partida)
        if transversal1(partida) != None:
                return transversal1(partida)
        if transversal2(partida) != None:
                return transversal2(partida)


jogo = [[2, 2, 1],
	    [2, 1, 0],
	    [1, 1, 2]]

print(f"O jogador {juncao(jogo)} venceu.")