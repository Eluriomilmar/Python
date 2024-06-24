#Faça um programa que leia 5 valores numéricos e guarde-os em uma lsita.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = [0, 0]
menor = [0, 0]
lista = []
for i in range(5):
    lista.append(int(input(f"Insira O número que ficará na posição {i} da lista: ")))
    if i == 0:
        maior[0] = lista[i]
        maior[1] = i
        menor[0] = lista[i]
        menor[1] = i
    else:
        if lista[i] < menor[0]:
            menor[0] = lista[i]
            menor[1] = i
        if lista[i] > maior[0]:
            maior[0] = lista[i]
            maior[1] = i
print(f"O maior valor é {maior[0]} e se encontra na posição {maior[1] + 1} da lista.\nO menor valor é {menor[0]} e se encontra na posição {menor[1] + 1} da lista.")