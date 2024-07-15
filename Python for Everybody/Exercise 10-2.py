a = input("Insira nome do arquivo: ")
dicio = dict()
with open(a, "r") as arquivo:
    for palavras in arquivo:
        palavras = palavras.splitlines()
        for linha in palavras:
            if linha.startswith("From "):
                linha = linha.split(" ")
                linha = linha[6]
                linha = linha.split(":")
                if linha[0] in dicio:
                    dicio[linha[0]] += 1
                else:
                    dicio[linha[0]] = 1
dicio = dict(sorted(dicio.items()))
for i, j in dicio.items():
    print(f"{i}: {j}")