estado = dict()
brasil = list()
while True:
    estado["UF"] = str(input("Insira o nome do Estado(ext.): "))
    estado["Sigla"] = str(input("Insira a sigla correspondente ao Estado: "))
    brasil.append(estado.copy())
    if str(input("Deseja continuar a execução do progrma? (N para parar)")) == "N":
        break
print(brasil)
for i in brasil:
    for j, k in i.items():
        print(f"{j}: {k}")