#Recursiva
import math

Iteracoes = int(input("Em quantas iterações deseja calcular Phi? "))

def phiCalc(i):
    if i >= 1:
        return math.sqrt(1 + phiCalc(i - 1))
    else:
        return 1

Resultado = phiCalc(Iteracoes)

if Iteracoes >= 1:
    print ("O valor de Phi em %i iterações é igual a: %f" % (Iteracoes, Resultado))