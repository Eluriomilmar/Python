#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,27
dinheiro = float(input("Quanto dinheiro a pessoa possui na carteira? "))
print(f"Com R${dinheiro:.2f} a pessoa pode comprar US${dinheiro/3.27:.2f}.")