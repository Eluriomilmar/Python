#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
v1 = float(input("Insira o valor 1: "))
v2 = float(input("Insira o valor 2: "))
print("[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa")
menu = -1
while menu < 1 or menu > 5 or menu == 4:
    menu = int(input("Insira número válido de acordo com o menu: "))
    if menu == 1:
        print(f"O valor da soma de {v1} e {v2} é: {v1 + v2}")
    if menu == 2:
        print(f"O valor da multiplicação de {v1} e {v2} é: {v1 * v2}")
    if menu == 3:
        if v1 > v2:
            print(f"O valor de {v1} é maior que o de {v2}")
        elif v2 > v1:
            print(f"O valor de {v2} é maior que o de {v1}")
        else:
            print(f"Ambos os valores são iguais a {v1}")
    if menu == 4:
        v1 = float(input("Insira o valor 1: "))
        v2 = float(input("Insira o valor 2: "))
    if menu == 5:
        print("Programa finalizado com êxito.")