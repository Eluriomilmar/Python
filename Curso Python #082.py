"""Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas."""
cont = True
lista = []
lista_par = []
lista_impar = []
while cont == True:
    lista.append(int(input("Insira número para ser adicionado à lista: ")))
    if lista[len(lista)-1] % 2 == 0:
        lista_par.append(lista[len(lista)-1])
    else:
        lista_impar.append(lista[len(lista)-1])
    var = str(input(("Deseja continuar a execução do programa? (S/N): "))).upper()
    if var == "S":
        cont = True
    elif var == "N":
        cont = False
if cont == False:
    print(f"Lista 1: {lista}\nLista com números pares: {lista_par}\nLista com números ímpares: {lista_impar}")