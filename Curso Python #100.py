"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior."""
import random


def sorteia():
    lista = list()
    for i in range(5):
        lista.append(random.randint(0,10))
    return lista

def soma(a):
    soma = 0
    for i in range(len(a)):
        soma += a[i]
    return soma


print(soma(sorteia()))