#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
try:
    n = int(input("digite um n: "))
except:
    n = int(input(f"O erro encontrado foi {erro.__cause__}\nInsira número inteiro válido: "))
else:
    print(f"Você digitou {n}")
finally:
    print("Programa encerrado.")