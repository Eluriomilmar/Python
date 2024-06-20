#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do Peso
#-Entre 18.5 e 25: Peso ideal
#-25 até 30: Sobrepeso
#-30 até 40: Obesidade
#-Acima de 40: Obesidade mórbida
altura = float(input("Insira a altura, em metros: "))
peso = float(input("Insira o peso, em Kg: "))
IMC = peso/(altura**2)
print(f"IMC: {IMC:.2f},", end=" ")
if IMC < 18.5:
    print("Abaixo do peso.")
elif IMC < 25:
    print("Peso ideal.")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")