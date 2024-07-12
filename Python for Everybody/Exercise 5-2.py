"""Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average."""
import numbers

def checa_num(maior = 0, menor = 0, n = 0):
    try:
        a = input("Insira número, SAIR para sair: ")
        if a.upper() == "SAIR":
            return maior, menor
        a = float(a)
    except:
        print("Não sei como você chegou até aqui, parabéns.")
    else:
        if n == 0:
            return checa_num(maior = a, menor = a, n = 1)
        if a <= menor:
            return checa_num(maior = maior, menor = a, n = 1)
        if a >= maior:
            return checa_num(maior = a, menor = menor, n = 1)


maior, menor = checa_num()
print(f"Maior: {maior}\nMenor: {menor}")