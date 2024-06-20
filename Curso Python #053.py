#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
frase = str(input("Insira frase a ser verificada se é palíndromo: ")).replace(" ","")
for i in range(len(frase)):
    if (frase[i] != frase[len(frase)-1-i]):
        print("A frase não é palíndromo.")
        break
    if i == len(frase)-1:
        print("A frase é palíndromo.")