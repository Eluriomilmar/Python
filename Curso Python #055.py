#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos
for i in range(5):
    aux = int(input(f"Insira o peso da pessoa {i+1}: "))
    if i == 0:
        menor = aux
        maior = aux
    else:
        if aux > maior:
            maior = aux
        if aux < menor:
            menor = aux
print(f"O maior peso lido foi igual a {maior} e o menor peso lido foi igual a {menor}.")