#Crie um programa que tenha uma tupla totalmente preenchida com uma  ontagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ("zero", "um", "dois" , "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
indice = -1
while indice < 0 or indice > 20:
    indice = int(input("Insira número a ser representado por inteiro: "))
print(numeros[indice])