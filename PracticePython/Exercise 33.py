import json


def aniversarios(lista):
    nome = str(input("Insira o nome do aniversariante: "))
    if lista.get(nome) == None:
        ano = str(input("Insira a data de aniversário: "))
        a = dict()
        a = {nome: ano}
        return a
    else:
        print(f"{nome} nasceu em {lista.get(nome)}")
        return {nome: lista.get(nome)}


def cont():
    while True:
        try:
            a = str(input("Deseja continuar a execução do programa? (S/N): ")).upper()
        except:
            print("????")
        else:
            return a


with open("calendario.json", "r") as c:
    calendario = json.load(c)
while True:
    calendario.update(aniversarios(calendario))
    print(calendario)
    if cont() == "N":
        break
    print(calendario)
with open("calendario.json", "w") as c:
    json.dump(calendario, c)