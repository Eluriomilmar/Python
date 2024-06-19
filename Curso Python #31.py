#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distancia = float(input("Insira a distância a ser percorrida na viagem: "))
if distancia > 200:
    print(f"O preço da viagem será de R${distancia*0.45:.2f}")
else:
    print(f"O preço da viagem será de R${distancia*0.5:.2f}")