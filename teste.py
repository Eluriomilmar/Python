import random
cont = True
composta = list()
for i in range(3):
    composta.append([])
    for j in range(3):
            composta[i].append(random.randint(0,100))
print(composta)