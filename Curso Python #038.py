#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: - O primeiro valor é maior, - O segundo valor é maior, - Não existe valor maior, os dois são iguais.
primeiro = int(input("Insira o primeiro valor: "))
segundo = int(input("Insira o segundo valor: "))
if primeiro > segundo:
    print("O primeiro valor é maior.")
elif segundo > primeiro:
    print("O segundo valor é maior.")
else:
    print("Os valores são iguais.")