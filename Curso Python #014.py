#Escreva um programa que converta uma temperatura digitada em °C para °F
celsius = float(input("Insira a temperatura em °C: "))
print(f"A temperatura em °F é igual a: {celsius * (9/5) + 32:.2f}")