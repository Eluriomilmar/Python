#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:
#A) Qual é o total gasto na compra
#B) Quantos produtos custam mais de R$1000
#C) Qual é o nome do produto mais barato
total = 0
qtd_caros = 0
barato_preco = 0
barato_nome = ""
while True:
    aux = float(input("Insira o valor do produto: "))
    total += aux
    if aux > 1000:
        qtd_caros += aux
    if barato_preco == 0:
        barato_preco = aux
        barato_nome = str(input("Qual o nome do produto? "))
    elif aux < barato_preco:
        barato_preco = aux
        barato_nome = str(input("Qual o nome do produto? "))
    cont = str(input("Deseja continuar a execução do programa? (S/N) "))
    if cont.upper() == "N":
        break
print(f"O total gasto na compra foi {total:.2f}\{qtd_caros} custaram mais de R$1000.00\nO nome do produto mais barato é {barato_nome}")