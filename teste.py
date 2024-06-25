cont = True
composta = list()
while cont == True:
    base = list()
    base.append(int(input("Insira número inteiro: ")))
    base.append(int(input("Insira outro número inteiro: ")))
    composta.append(base[:])
    base.clear()
    if str(input("Deseja continuar? (S/N): ")).upper() == "S":
        cont = True
    else:
        cont = False
print(composta)