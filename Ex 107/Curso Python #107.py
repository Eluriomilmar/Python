import moeda


preco = float(input("Insira o preço: "))
a = float(input("Insira em quanto se deseja aumentar ou diminuir o preço: "))

print(f"{preco} aumentado em {a}% é igual a: {moeda.aumentar(preco, a)}")
print(f"{preco} diminuido em {a}% é igual a: {moeda.diminuir(preco, a)}")
print(f"{preco} dobrado é igual a: {moeda.dobro(preco)}")
print(f"{preco} reduzido pela metade é igual a: {moeda.metade(preco)}")