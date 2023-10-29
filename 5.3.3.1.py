#Função recursiva da forma  somatório(n, k=0) de (1/k!) para n -> inf

import math

n = math.inf
k = int(input("Insira a quantidade de iterações do somatório: "))
print("O valor da função com fatorial de %i iterações é de: " % k, end=(""))

def fatorial(k):
    if k == 0:
        return 1
    if k == 1:
        return 1
    elif k > 1:
        return k * fatorial(k-1)

def somatorio(k):
    if k == 0:
        return 1/fatorial(0)
    if k == 1:
        return 1/fatorial(1) + fatorial(0)
    elif k > 1:
        return 1/fatorial(k) + 1/fatorial(k-1)

print("%f" % somatorio(k))