"""Write a program to read through a mail log,
 build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary."""


a = input("Insira nome do arquivo aqui: ")
dicio = dict()
with open(a, "r") as arquivo:
    for palavras in arquivo:
        palavras = palavras.splitlines()
        for linha in palavras:
            linha = linha.split(" ")
            if linha[0] == "From":
                if linha[1] in dicio:
                    dicio[linha[1]] += 1
                else:
                    dicio[linha[1]] = 1
for i, k in dicio.items():
    print(f"{i}: {k}")