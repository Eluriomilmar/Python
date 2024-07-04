#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
cont = "S"
qtd = 0
soma = 0
while cont == "S":
    num = int(input("Insira número inteiro: "))
    if qtd == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    qtd += 1
    cont = str(input("Deseja continuar inserindo números? (S/N): "))
print(f"Foram inseridos {qtd} números, cuja média é igual a {soma/qtd:.2f}\nO maior número foi: {maior} e o menor número foi {menor}")