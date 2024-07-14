"""Rewrite the program that prompts the user for a list of numbers and
prints out the maximum and minimum of the numbers at the end when the user enters "done".
Write the program to store the numbers the user enters in a list and use the max() and min()
functions to compute the maximum and minimum numbers after the loop completes."""


count = 0
maxmin = []
while True:
    a = input("Insira número. SAIR para sair: ").upper()
    if count == 0 and a != "SAIR":
        maxmin.append(float(a))
        maxmin.append(float(a))
        count = -1
    if a == "SAIR":
        print(f"Valor mínimo: {maxmin[0]}\nValor máximo: {maxmin[1]}")
        break
    a = float(a)
    if min(maxmin) >= a:
        maxmin[0] = a
    if max(maxmin) <= a:
        maxmin[1] = a
