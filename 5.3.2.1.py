#Função iterativa da forma 1+1/(1+(1/1+...., ou phi

i = int(input("Deseja calcular a função com quantos passos? "))
res = 0
while i > 0:
    if i == 1:
        res = 1 + res
        i = i - 1
    elif i > 1:
        res = 1/(1+res)
        i = i - 1

print("O resultado da função é igual a: %f" % res)