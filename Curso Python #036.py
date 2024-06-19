#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
nome = str(input("Qual o nome do cliente? "))
salario = float(input("Qual o salário do cliente? "))
tempo = float(input("Em quantos anos o cliente pretende quitar a dívida? "))
casa = float(input("Insira o valor da casa: "))
salario = salario*12
if casa/tempo > salario*0.3:
    print(f"O empréstimo de {nome} não foi autorizado, pois {salario/tempo:.2f}% de seu salário ficaria comprometido.")
else:
    print(f"O empréstimo de {nome} foi aprovado, somente {salario/tempo:.2f} será comprometido!")