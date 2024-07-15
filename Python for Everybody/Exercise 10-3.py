a = input("Insira o nome do arquivo: ")
dicio = dict()
with open(a, "r") as arquivo:
    for palavras in arquivo:
        palavras = palavras.splitlines()
        for linha in palavras:
            linha = linha.split()
            for palavra in linha:
                for letra in palavra:
                    if letra.isalpha() == True:
                        if letra in dicio:
                            dicio[letra.lower()] += 1
                        else:
                            dicio[letra.lower()] = 1
dicio = dict(sorted(dicio.items()))
for i, j in dicio.items():
    print(f"{i}: {j}")