#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input("Insira o ângulo para o qual será calculado o seno, cosseno e a tangente: "))
angulo = math.radians(angulo)
print(f"Seno: {math.sin(angulo)}\nCosseno: {math.cos(angulo)}\nTangente: {math.tan(angulo)}")