#Faça um algoritmo para encontrar o maior ímpar de 3 inteiros.

print("O programa irá requisitar 3 números, tenha certeza que são inteiros e ímpares")

import math
import sys
print("Este programa compara qual o maior número inteiro e ímpar entre 3 inputs dados pelo usuário")
res = float('-inf')
aux = 0
while aux < 3:
    a = float(input("Insira o %0.fº número: " % (aux+1)))
    if math.ceil(a) != math.floor(a) or a%2 == 0:
        aux = aux+1
    else:
        if a > res:
            res = a
        aux = aux+1
if res == '-inf':
    print("Nenhum dos valores inseridos é ímpar e inteiro")
else:
    print("O maior número ímpar e inteiro inserido foi: %0.f" % res)