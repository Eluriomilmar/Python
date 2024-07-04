"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibitos todos so valores únicos digitados, em ordem crescente."""
lista = []
cont = "S"
while cont == "S":
    valor = float(input("Insira valor a ser colocado na lista: "))
    if valor not in lista:
        lista.append(valor)
    cont = str(input("Deseja continuar adicionando valores? (S/N): ").upper())
    print("Número adicionado com sucesso!")
lista.sort()
print(f"{lista}")
