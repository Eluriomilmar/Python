#Função recursiva da forma  somatório(n, k=0) de (1/k!) para n -> inf, #porém trunquei o n em 10

import math


k = int(input("Insira a quantidade de iterações do somatório: "))
print("A função somatório com fatorial de %i iterações é de: " % k, end=("")) # #Isso é exibido no fim do programa, como a variável "k" é reutilizada, comecei o print aqui


    while k >= 0:
        if k == 0:
            fatorial = fatorial * 1
            fatorial = fatorial - 1
        elif k == 1:
            fatorial = fatorial * 1
            fatorial = fatorial - 1
        elif k > 1:
            fatorial = fatorial * fatorial - 1
            fatorial = fatorial n - 1
