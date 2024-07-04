"""Crie um módlo chamado moeda.py que tenha as funções incorporadas: aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumaas dessas funções."""
from Ex107.utilidadesCeV import moeda
preco = float(input("Insira o preço: "))
print(f"A metade de R${preco} é: {moeda(preco)}")
