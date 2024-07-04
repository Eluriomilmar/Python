"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""
palavras = ("Aprender", "Programar", "Linguagem", "Python", "Curso", "Gratis", "Estudar", "Praticar", "Trabalhar", "Mercado", "Programador", "Futuro")
for i in range(len(palavras)):
    print(f"Na palavra {palavras[i]}, temos a letra A: {palavras[i].upper().count("A")}, E: {palavras[i].upper().count("E")}, I: {palavras[i].upper().count("I")}, O: {palavras[i].upper().count("O")}, U: {palavras[i].upper().count("U")}")