#Função fatorial iterativa

fat = int(input("Insira número que se quer calcular o fatorial: "))
res = 1
print("O resultado do fatorial de %i é: " % fat, end = "")
while fat >= 1:
    res = res * fat
    fat = fat - 1
print("%i" % res)
