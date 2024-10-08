trem = input("Insira input a ser invertido: ")
invertida = []
for i in range(len(trem)):
    invertida.append(trem[len(trem)-i-1])

invertida = "".join(invertida)
print(invertida)

#alternativamente eu poderia só ter feito invertida = trem[::-1]


