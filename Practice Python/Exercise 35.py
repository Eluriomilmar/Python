from collections import Counter
import json


with open("calendario.json", "r") as c:
    dicio = json.load(c)


lista = []
for i, j in dicio.items():
    print(f"{i}: {j}")
    if j in lista:

