dicio = dict()
arquivo = input("Insira o nome do arquivo: ")
with open(arquivo, "r") as a:
    for palavras in a:
        linhas = palavras.splitlines()
        for linha in linhas:
            linha = linha.split(" ")
            if linha[0] == "From":
                if linha[2] in dicio:
                    dicio[linha[2]] += 1
                else:
                    dicio[linha[2]] = 1
print(dicio)