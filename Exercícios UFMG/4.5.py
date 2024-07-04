#Escreva um programa Python que determine se um ano é
#bissexto ou não.


ano = int(input("Insira o valor do ano: "))

if ano % 400 == 0:
    print("O ano é bissexto")
elif ano % 100 == 0:
    print("O ano não é bissexto")
elif ano % 4 == 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")
