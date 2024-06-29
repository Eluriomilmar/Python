"""Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada"""
import time

def contagem(a, b, passos):
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


contagem(1, 10, 1)
contagem (10, 0, 2)
#contagem(int(input("Insira o inicio: ")), int(input("Insira o fim: ")), int(input("Insira o tamanho do passo: ")))