#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido
import random
primeiro = input("Insira o nome do primeiro aluno: ")
segundo = input("Insira o nome do segundo aluno: ")
terceiro = input("Insira o nome do terceiro aluno: ")
quarto = input("Insira o nome do quarto aluno: ")
lista = [primeiro, segundo, terceiro, quarto]
print(f"O aluno sorteado para apagar o quadro foi: {random.choice(lista)}")