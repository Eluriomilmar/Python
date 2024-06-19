#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nomes separadamente.
nome = input("insira nome aqui: ")
print(f"O primeiro nome é: {nome[:nome.find(" "):]}\nO último nome é {nome[nome.rfind(" ")::]}")