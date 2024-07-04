"""Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média"""
pessoa = dict()
todes = list()
mulheres = list()
velhos = list()
media = 0
while True:
    pessoa["nome"] = str(input("Insira o nome da pessoa a ser cadastrada: "))
    pessoa["sexo"] = str(input(f"Insira o sexo de {pessoa["nome"]} (M/F): ")).upper()
    pessoa["idade"] = int(input(f"Insira a idade de {pessoa["nome"]}: "))
    todes.append(pessoa.copy())
    cont = str(input("Deseja continuar cadastrando pessoas? (S/N)")).upper()
    if cont == "N":
        break
    elif cont == "S":
        print("Continuando a execução do programa\n\n")
    else:
        while cont != "S" and cont != "N":
            cont = str(input("Input incorreto, digite N ou S para prosseguir: ")).upper()
            if cont == "N":
                break

print(f"Foram cadastradas {len(todes)} pessoas")
for i in todes:
    for j, k in i.items():
        print(f"{j} {k}")
        if k == "M":
            mulheres.append(i.copy())
        if j == "idade":
            media += k
media = media/len(todes)
print(f"Foram cadastradas {len(todes)} pessoas.")
print(f"A média de idade é igual a {media}")
print(f"A lista somente com as mulheres é: ")
for i in mulheres:
    for j, k in i.items():
        print(f"{j}: {k}", end="   ")
    print("\n")

print(f"As pessoas com a idade acima da média {media} são: ", end = "")
for i in range(len(todes)):
    if todes[i]["idade"] > media:
        print(f"{todes[i]["nome"]}", end=" ")