#Função recursiva da forma  somatório(n, k=0) de (1/k!) para n -> inf, #porém trunquei o n em 10

import math


n = int(input("Insira a quantidade de iterações do somatório: "))
print("A função somatório com fatorial de %i iterações é de: " % n, end=("")) # #Isso é exibido no fim do programa, como a variável "k" é reutilizada, comecei o print aqui

def fatorial(n):
    i = 0
    resultado = 0
    while i <= n:
        if i == 0:
            resultado = 1
            i = i + 1
        else:
            resultado = resultado * (resultado + 1)
            i = i + 1
    return resultado

def somatorio(n):
    soma = 0
    k = 0
    while k <= n:
        soma = soma + (1/fatorial(k))
        k = k + 1
    return soma

print("%f" % somatorio(n))