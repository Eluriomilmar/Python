#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
primeiro = input("Insira o nome do primeiro aluno: ")
segundo = input("Insira o nome do segundo aluno: ")
terceiro = input("Insira o nome do terceiro aluno: ")
quarto = input("Insira o nome do quarto aluno: ")
lista = [primeiro, segundo, terceiro, quarto]
print(f"A ordem escolhida para a apresentação do trabalho é: {random.sample(lista, len(lista))}")