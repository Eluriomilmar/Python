#Faça um programa que leia o sexo de uma pessoa mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = "a"
while sexo != "M" and sexo != "F":
    sexo = str(input("Insira o sexo de uma pessoa aleatória(M/F): ")).upper()
    if sexo != "M" and sexo != "F":
        print("Valor incorreto, tente novamente.")
print(f"O sexo é {sexo}.\nFim do programa.")