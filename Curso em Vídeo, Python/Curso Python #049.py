#Refaça o desafio 009, usando um laço for.
num = float(input("Insira número para que seja efetuado o cálculo da tabuada: "))
for x in range(10):
    print(f"{x}*{num:.0f}={x*num:.0f}")