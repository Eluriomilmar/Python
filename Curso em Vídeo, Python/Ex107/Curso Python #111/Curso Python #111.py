from Ex107.UtilidadesCeV import moeda, dado

moeda.resumo(1000, 20)

n = dado.leiaDinheiro(str(input("Insira quantidade de dinheiro: ")))
moeda.dobro(n)