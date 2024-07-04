"""Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""
import random
tupla = (random.random(), random.random(), random.random(), random.random(), random.random())
print(tupla)
print(f"O maior número é: {max(tupla)} \nO menor número é: {min(tupla)}")