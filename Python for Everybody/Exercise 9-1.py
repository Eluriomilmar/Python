"""Write a program that reads the words in words.txt and stores them as keys in a dictionary."""


dicio = dict()
a = input("Insira nome do arquivo: ")
with open(a, "r") as file:
    for palavras in file:
        linha = palavras.split()
        for palavra in linha:
            if palavra.lower() in dicio:
                dicio[palavra.lower()] += 1
            else:
                dicio[palavra.lower()] = 1
print(dicio)