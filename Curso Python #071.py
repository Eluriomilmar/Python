#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: COnsidere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
saque = int(input("Insira o valor a ser sacado, em número inteiro: R$"))
ced_50 = 0
ced_20 = 0
ced_10 = 0
ced_1 = 0
while saque >= 50:
    saque -= 50
    ced_50 += 1
while saque >= 20:
    saque -= 20
    ced_20 += 1
while saque >= 10:
    saque -= 10
    ced_10 += 1
while saque >=1:
    saque -= 1
    ced_1 += 1
print(f"Deverão ser entreques {ced_50} cédulas de 50, {ced_20} cédulas de 20, {ced_10} cédulas de 10 e {ced_1} cédulas de 1.")