#Fatorial recursiva

fat = int(input("Insira o número do qual se deseja calcular o fatorial: "))

def fatorial(n):
    if n < 1:
        return 1
    else:
        return fatorial(n - 1) * n

print("O fatorial de %i é: %i" % (fat, fatorial(fat)))