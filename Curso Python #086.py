"""Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta."""
matriz = [[], [], []]
for i in range(3):
    for j in range(3):
        numero = int(input(f"Insira o número da lacuna {i + 1}x{j + 1}: "))
        matriz[i].append(numero)
for i in range(3):
    print("\n")
    for j in range(3):
        print(f"{matriz[i][j]:<5}", end = "")