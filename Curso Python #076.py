"""Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
No final, mostre uma listagem de preços, organizando os dados em forma tabular."""
lista = ("Lapis", 1.75, "Borracha", 2, "Caderno", 15.90, "Estojo", 25, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
for i in range(len(lista)):
    if i%2 == 0:
        print(f"{lista[i]}", end = "")
        j = 0
        while j < 20 - len(lista[i]):
            print(".", end="")
            j += 1
    else:
        print(f"R${lista[i]:.2f}")