#Faça um programa que mostre a  tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.
while True:
    tabuada = int(input("Digite o valor pra o qual se deseja fazer a tabuada: "))
    if tabuada < 0:
        break
    conta = 1
    while conta < 11:
        print(f"{tabuada}x{conta}={conta*tabuada}")
        conta += 1
