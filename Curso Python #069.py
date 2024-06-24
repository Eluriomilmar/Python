#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A) Quantas pessoas tem mais de 18 anos.
#B) Quantos homens foram cadastrados.
#C) Quantas mulheres tem menos de 20 anos
idade, sexo = 0, ""
maiores = 0
homens = 0
mulheres_menores = 0
while True:
    sexo = str(input("Insira o sexo da pessoa a ser cadastrada (F/M): "))
    idade = int(input("Insira idade da pessoa que está sendo cadastrada: "))
    sexo = sexo.upper()
    if sexo == "M":
        homens += 1
    if idade > 18:
        maiores += 1
    if sexo == "F" and idade < 20:
        mulheres_menores += 1
    cont = str(input("Deseja continuar a execução do programa? (S/N): "))
    cont = cont.upper()
    if cont == "N":
        break
print(f"Foram cadastradas {maiores} pessoas com mais de 18 anos\nForam cadastrados {homens} homens\nForam cadastradas {mulheres_menores} mulheres com menos de 20 anos")