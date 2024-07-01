import moeda


preco = float(input("Insira o preço: "))
a = float(input("Insira em quanto se deseja aumentar ou diminuir o preço: "))

moeda.moeda(moeda.aumentar(preco, a))
moeda.moeda(moeda.diminuir(preco, a))
moeda.moeda(moeda.dobro(preco))
moeda.moeda(moeda.metade(preco))