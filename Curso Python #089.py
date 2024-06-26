"""Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente."""
cont = "S"
boletim = []
indice = 0
while cont == "S":
    notas_temp = [[], [], [], []]
    for i in range(len(notas_temp)-1):
        if i == 0:
            notas_temp[i] = str(input(f"Insira o nome do estudante: "))
        else:
            notas_temp[i] = float(input(f"Insira a nota {i} do aluno: "))
    notas_temp[3] = (notas_temp[1] + notas_temp[2])/2
    boletim.append(notas_temp[:])
    notas_temp.clear()
    cont = str(input("Deseja continuar a execução do programa? (S/N): ")).upper()
    indice += 1

print(f"{"N°":<4}{"Nome":<10}{"Média: ":^8}")
for i in range(len(boletim)):
    for j in range(len(boletim[i])):
        if j == 0:
            print(f"N°{i:<4}", end = "")
            print(f"{boletim[i][j]:<10}", end = "")
        if j == 3:
            print(f"{boletim[i][j]:^8}")
indice = -1
indice = int(input("Deseja mostrar as notas de algum aluno? (valor numérico, -1 encerra a aplicação: "))
cont = "S"
while cont == "S":
    if indice < 0:
        print("Programa encerrado com sucesso.")
        break
    else:
        print(f"O(A) Aluno(a) {boletim[indice][0]} tirou {boletim[indice][1]} na Prova 1 e {boletim[indice][2]} na Prova 2.")
        indice = int(input("Deseja consultar as notas de mais algum estudante? Insira o índice(-1 interrompe a aplicação): "))