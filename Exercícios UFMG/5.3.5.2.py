#função iterativa de e^x

n = int(input("Insira a quantidade de iterações que deseja calcular na função Pn: "))

def positivo_negativo(n):
    if n%2 == 0:
        resultado = 1
    else:
        resultado = -1
    return resultado

def fatorial(n):
    resultado = 1
    while n >= 0:
        if n == 0:
            resultado = resultado * 1
            n = n - 1
        else:
            resultado = resultado * n
            n = n - 1
    return resultado

def somatorio(n):
    resultado = 0
    while n >= 0:
        resultado = positivo_negativo(n)/fatorial(n) + resultado
        n = n - 1
    return resultado

resultado = somatorio(n)

print("A função Pn foi calculada com o resultado de: %f" % resultado)