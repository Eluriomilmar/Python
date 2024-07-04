jogador = dict()
gols = list()
media = 0
jogador["nome"] = str(input("Insira o nome do jogador: "))
for i in range(int(input(f"Quantas partidas {jogador["nome"]} jogou? "))):
    gols.append(int(input(f"Quantos gols na {i+1}ª partida: ")))
    media += gols[i]
jogador["media"] = media/len(gols)
jogador["gols"] = gols
print(f"O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.")
for i in range(len(jogador["gols"])):
    print(f"    => Na {i+1}ª partida, fez {jogador["gols"][i]} gols.")
print(f"{jogador["nome"]} fez um total de {jogador["media"] * len(jogador["gols"]):.0f} gols.")