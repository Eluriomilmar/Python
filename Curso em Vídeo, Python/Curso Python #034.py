#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento será de 15%.
salario = float(input("Insira o valor do salário do funcionário: "))
if salario > 1250:
    salario = salario * 1.1
else:
    salario = salario * 1.15
print(f"O novo salário do funcionário é igual a {salario}")