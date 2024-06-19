#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = int(input("Insira a leitura da velocidade do carro: "))
if velocidade > 80:
    velocidade = velocidade - 80
    print(f"Será cobrada uma multa de R${velocidade * 7}.")
else:
    print("O carro está dentro do limite de velocidade estabelecido.")