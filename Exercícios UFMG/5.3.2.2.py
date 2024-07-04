#Função recursiva da forma 1+1/(1+(1/1+...., ou phi

i = int(input("Deseja calcular a função com quantos passos? "))

def phi(passos):
    if passos == 1:
        return 1
    elif passos > 1:
        return 1 + 1/phi(passos -1)

print("O resultado é igual a: %f" % phi(i))