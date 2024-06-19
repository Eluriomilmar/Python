#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
distancia = float(input("Insira a quantidade de Km percorridos pelo carro: "))
dias = int(input("Insira a quantidade de dias pelos quais o carro foi alugado: "))
print(f"O valor a ser pago é igual a {distancia * 0.15 + dias * 60:.2f}")