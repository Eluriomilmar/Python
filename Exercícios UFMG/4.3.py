#Faça um algoritmo para encontrar o menor de 3 inteiros
#distintos com, no máximo, 3 comparações.

import math
import sys
print("Este programa compara qual o maior número inteiro entre 3 inputs distintos dados pelo usuário")
a = float(input("Insira o primeiro número: "))
if math.ceil(a) != math.floor(a):
    print ("Input incorreto, número não é inteiro")
    sys.exit()
b = float(input("Insira o segundo número: "))
if math.ceil(b) != math.floor(b):
    print ("Input incorreto, número não é inteiro")
    sys.exit()
c = float(input("Insira o tereiro número: "))
if math.ceil(c) != math.ceil(c):
    print("Input incorreto, número não é inteiro")
    sys.exit()
if a != b and a != c and b != c:
    if a > b:
        if a > c:
            print("O número %.0f é o maior deles" % a)
            sys.exit()
        elif a < c:
            print("O número %.0f é o maior deles" % c)
            sys.exit()
    else:
        if b > c and b != c:
            print("O número %.0f é o maior deles" % b)
            sys.exit()
        elif b < c:
            print("O número %.0f é o maior deles" % c)
            sys.exit()
print("Dois ou mais números são iguais")