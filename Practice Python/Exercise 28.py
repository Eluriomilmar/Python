a = []
while True:
    if len(a) == 0:
        a.append(int(input("Insira o valor da variável: ")))
        maior = a[len(a)-1]
        menor = a[len(a)-1]
    else:
        a.append(int(input("Insira o valor da variável, 0 para interromper: ")))
        if maior < a[len(a)-1]:
            maior = a[len(a)-1]
        if menor > a[len(a)-1]:
            menor = a[len(a)-1]
        if a[len(a)-1] == 0:
            break

print(f"O valor da maior variável é: {maior}\nO valor da menor variável é: {menor}")