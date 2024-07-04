#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#acrescente o recurso de mostrar que tipo de triângulo será formado:
#-Equilátero: Todos os lados iguais.
#-Isóceles: Dois lados iguais.
#-Escaleno: Todos os lados diferentes
r1 = float(input("Insira o tamanho da reta 1: "))
r2 = float(input("Insira o tamanho da reta 2: "))
r3 = float(input("Insira o tamanho da reta 3: "))
if (r1 <= r2 + r3) and (r2 <= r1 + r3) and (r3 <= r2 + r1):
    print("As retas podem formar um triângulo")
    if r1 == r2 and r1 == r3:
        print("O triângulo é um triângulo equilátero.")
    elif (r1 == r2) or (r1 == r3) or (r2 == r3):
        print("O triângulo é um triângulo isóceles")
    else:
        print("O triângulo é um triângulo escaleno")
else:
    print("As retas não podem formar um triângulo")