import json

calendario = dict()
with open("calendario.json", "r") as c:
    teste = json.load(c)
print(teste)

nome = str(input("Nome: "))
ano = str(input("Ano: "))
dicio = {nome: ano}
teste.update(dicio)
print (teste)

with open("calendario.json", "w") as c:
    json.dump(teste, c)