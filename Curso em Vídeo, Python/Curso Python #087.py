"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
matriz = [[], [], []]
pares = 0
terceira_coluna_soma = 0
segunda_linha_maior = 0
for i in range(3):
    for j in range(3):
        numero = int(input(f"Insira o número da lacuna {i + 1}x{j + 1}: "))
        matriz[i].append(numero)
        if numero % 2 == 0:
            pares += numero
        if j == 2:
            terceira_coluna_soma += numero
        if i == 1:
            if j == 0:
                segunda_linha_maior = numero
            else:
                if segunda_linha_maior < numero:
                    segunda_linha_maior = numero
for i in range(3):
    print("\n")
    for j in range(3):
        print(f"{matriz[i][j]:<5}", end = "")

print(f"A soma de todos os valores pares digitados é: {pares}\nA soma dos valores da terceira coluna é: {terceira_coluna_soma}\nO maior valor da segunda linha é: {segunda_linha_maior}")