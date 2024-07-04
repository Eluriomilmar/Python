#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
oposto = float(input("Insira o valor do cateto oposto: "))
adjacente = float(input("Insira o valor do cateto adjacente: "))
hipotenusa = math.sqrt(math.pow(oposto,2) + math.pow(adjacente, 2))
print(f"O valor da hipotenusa é igual a: {hipotenusa}")