# Cálculo recursivo função fibonacci

n = int(input("Insira a quantidade de passos a serem calculados: "))

def Fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    elif i > 1:
        return (Fibonacci(i - 1)) + (Fibonacci(i - 2))

print("O resultado é igual a: %f" % Fibonacci(n))
