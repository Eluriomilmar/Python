#Função iterativa para calcular Phi

import math

Phi = float(0)
Loops = int(input("Deseja calcular Phi em quantas iterações? "))
print("O cálculo de Phi em %i iterações é igual a: " % Loops, end = (""))

while Loops > 0:
    if Phi == 0:
        Phi = math.sqrt(1)
        Loops = Loops -1
    else:
        Phi = math.sqrt(Phi+math.sqrt(1))
        Loops = Loops - 1

print("%f" % Phi)

