from random import randint


def computador():
    oponente = ["Pedra", "Papel", "Tesoura"]
    a = randint(0, 2)
    return oponente[a]


def jogada():
    while True:
        try:
            joga = str(input("Insira Pedra, Papel ou Tesoura: "))
            if joga.upper() == "PEDRA" or joga.upper() == "TESOURA" or joga.upper() == "PAPEL":
                return jogada
            else:
                raise ValueError
        except:
            print("Únicos valores válidos são Pedra, Papel e Tesoura.")


def vitoria(jogada, computador):
    print(f"Você jogou {jogada} e o computador jogou {computador}, você venceu!")


def derrota(jogada, computador):
    print(f"Você jogou {jogada} e o computador jogou {computador}, você perdeu!")


def empate(jogada, computador):
    print(f"Você jogou {jogada} e o computador jogou {computador}, vocês empataram!")


def jogo(jogada, computador):
    if computador.upper() == jogada.upper():
        empate(jogada, computador)
        print("Empatou!")
    elif jogada.upper() == "TESOURA":
        if computador.upper() == "PEDRA":
            derrota(jogada, computador)
        else:
            vitoria(jogada, computador)
    elif jogada.upper() == "PEDRA":
        if computador.upper() == "PAPEL":
            derrota(jogada, computador)
        else:
            vitoria(jogada, computador)
    elif jogada.upper() == "PAPEL":
        if computador.upper() == "TESOURA":
            derrota(jogada, computador)
        else:
            vitoria(jogada, computador)


def cont():
    while True:
        try:
            a = str(input("Deseja jogar pedra, papel, tesoura? (S/N): "))
            if a.upper() != "S" and a.upper() != "N":
                raise ValueError
        except:
            print("O programa só aceita respostas S e N.")
        else:
            if a.upper() == "S":
                jogo(jogada(), computador())
            else:
                break


cont()