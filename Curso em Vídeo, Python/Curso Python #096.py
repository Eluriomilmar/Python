"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno."""
def area(a, b):
    print(f"A área do terreno é igual a {a*b}M²")


larg = float(input("Insira a largura do terreno: "))
comp = float(input("Insira o comprimento do terreno: "))
area(comp, larg)