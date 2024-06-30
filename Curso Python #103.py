"""Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: O nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente"""


def ficha(nome = "Jogador", gols = 0):
    print(f"Nome do jogador: {nome}\nNúmero de gols: {gols}")
    print(f"O jogador {nome} fez {gols} gol(s) no camperonato.")

nome = str(input("Insira o nome do jogador: "))
gols = str(input("Insira a quantidade de gols: "))
if nome.isalpha() == False:
    nome = "x"
if gols.isdigit() == False:
    gols = -1
    gols = int(gols)
ficha(nome, gols)