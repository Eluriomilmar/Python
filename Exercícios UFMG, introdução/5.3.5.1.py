#função recursiva de e^x

k = int(input("Insira em quantos passos deseja calcular a função somatório de Pn: "))

def fatorial(k):
    if k == 0 or k == 1:
        return 1
    elif k > 1:
        return k * fatorial(k-1)

def sinal(k):
    if k%2 == 0 or k == 0:
        return 1
    elif k%2 != 0:
        return -1

def somatorio(k):
    if k == 0:
        return 1
    else:
        return sinal(k)/(fatorial(k)) + somatorio(k-1)

print("A função Pn calculda em %i passos é igual a: %f" %(k, somatorio(k)))