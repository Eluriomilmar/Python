"""Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado"""
import random
from operator import itemgetter
resultados = dict()
for i in range(4):
    resultados[f"{i+1}"] = random.randint(1,6)
for j, k in resultados.items():
    print(f"O jogador {j} tirou {k}")
print("=-"*30)
ranking = dict()
ranking = sorted(resultados.items(), key=itemgetter(1), reverse = True)
for i in range(len(ranking)):
    print(f"O jogador {ranking[i][0]} tirou {ranking[i][1]} e ficou em {i+1}° lugar")