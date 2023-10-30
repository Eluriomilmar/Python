#Função recursiva da forma  somatório(n, k=0) de (1/k!) para n -> inf, #porém trunquei o n em 10

import math

#n = math.inf seria o caso ideal, porém a recursão só se permite ser feita 1000 vezes, por isso vou fixar n = k, para que sejam feitas 500 iterações de somatorio(n)


k = int(input("Insira a quantidade de iterações do somatório: "))
print("O valor da função somatório com fatorial de %i iterações é de: " % k, end=("")) #Isso é exibido no fim do programa, como a variável "k" é reutilizada, comecei o print aqui

def fatorial(k):
    if k == 0:
        return 1
    if k == 1:
        return 1
    elif k > 1:
        return (1/k) * fatorial(k-1)

def somatorio(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fatorial(n) + somatorio(n - 1) #para o somatório de 3, pro exemplo, a função faz 1/3! + 1/2! + 1/1!

print("%f" % somatorio(k))
print("\nFatorial: %f" % fatorial(k))