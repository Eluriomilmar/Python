#Crie um programa uqe leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles
qtd = 0
soma = 0
valor = 0
print("O programa somará os valores digitados, exceto 999, que é a condição de parada.")
while True:
    qtd += 1
    valor = int(input("Valor: "))
    if valor == 999:
        break
    soma = soma + valor
print(f"Foram digitados {qtd} valores, e a soma entre eles é igual a {soma}")