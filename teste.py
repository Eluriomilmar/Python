#arquivo somente para testes
valores = []
for i in range(10):
    valores.append(int(input("Insira valor para ser adicionado à lista: ")))
valores.sort(reverse=True)

for i, v in enumerate(valores):
    print(f"Na posição {i}, encontrei o valor {v}")