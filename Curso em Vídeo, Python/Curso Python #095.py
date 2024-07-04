"""Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador."""
jogadores = list()
jogador = dict()
gols = list()
while True:
    jogador["nome"] = str(input("Insira o nome do jogador: "))
    media = 0
    for i in range(int(input(f"Quantas partidas {jogador["nome"]} jogou? "))):
        gols.append(int(input(f"Quantos gols na {i+1}ª partida: ")))
        media += gols[i]
    jogador["media"] = media/len(gols)
    jogador["gols"] = gols[:]
    jogador["jogos"] = len(gols)
    jogadores.append(jogador.copy())
    gols.clear()
    if str(input("Deseja continuar a execução do programa? (condição de parada: 'N'): ")).upper() == "N":
        break
print(f"Os jogadores cadastrados são: ", end = "")
for i in jogadores:
    print("\n")
    for j, k in i.items():
        if j == "nome":
            print(f"{k}: ", end = "")
        if j == "media":
            print(f"média de {k} gols em {i["jogos"]} partidas. ", end = "")
        if j == "gols":
            print(f"Sua pontuação em cada partida foi: \n", end = "")
            for l in range(len(k)):
                print(f"partida {l+1}: {k[l]} ")

