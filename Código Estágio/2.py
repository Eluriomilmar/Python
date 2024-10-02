a = input("Insira string aqui: ")
cont = 0
for i in a:
    if i == "A" or i == "a": #poderia também usar o método .upper para tornar todos inputs caixa alta
        cont += 1
print(f"A letra A ocorre {cont} vezes")
