#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
#que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag)
numeros = 0
soma = 0
aux = 0
while soma != 999:
    soma = int(input("Insira número inteiro para ser somado: "))
    if soma != 999:
        aux += soma
        numeros += 1
print(f"Foram digitados {numeros} números e sua soma foi igual a {aux}")
