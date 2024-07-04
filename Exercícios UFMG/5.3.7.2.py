# Cálculo iterativo de fibonacci

i = int(input("Insira quantas iterações de Fibonacci deseja calcular: "))
print("O cálculo de Fibonacci com %i iterações é: " % i)

def fibonacci(i):
    aux = 0
    a = 0
    b = 0
    if i == 0:
        return 0
    if i == 1:
        return 1
    if i >= 2:
        a = 1
        b = 0
        aux = 2
        while aux <= i:
            if aux % 2 == 0:
                b = a + b
                aux = aux + 1
            else:
                a = a + b
                aux = aux + 1
    return a + b

print("%f" % fibonacci(i))