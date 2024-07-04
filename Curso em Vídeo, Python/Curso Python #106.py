"""Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o programa se encerrará.
Importante: use cores."""
from datetime import datetime
import time

def escreva(a):
    """
    -> Imprime na tela uma mensagem cercada por "~"
    :param a: String contendo a mensagem
    """
    print("~"*len(a))
    print(a)
    print("~"*len(a))


def contagem(a, b, passos):
    """
    -> Faz uma contagem e mostra na tela
    :param a: Início da contagem
    :param b: Fim da contagem
    :param passos: Passos da contagem
    """
    if passos < 0:
        passos = -1 * passos
    if passos == 0:
        passos = 1
    if a < b:
        while a < b:
            print(f"{a}", end = " ", flush = True)
            a += passos
            time.sleep(0.1)
    else:
        while b < a:
            print(f"{a}", end = " ", flush = True)
            a -= passos
            time.sleep(0.1)
    if a == b:
        print(f"{a}", end = " ", flush = True)
        time.sleep(0.1)
    time.sleep(0.1)
    print("FIM!")


def sorteia():
    """
    -> Sorteia 5 números inteiros de 0 a 10
    """
    lista = list()
    for i in range(5):
        lista.append(random.randint(0,10))
    return lista

print("\n1: Escreva\n2: Contagem\n3: Sorteia\n4: FIM\n")
escolha = "."
while escolha != "FIM":
    escolha = str(input("Digite a função a ser executada: "))
    if escolha == "Escreva":
        help(escreva)
    elif escolha == "Contagem":
        help(contagem)
    elif escolha == "Sorteia":
        help(sorteia)
    elif escolha == "FIM":
        break