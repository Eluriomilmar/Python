a = input("Insira o nome do arquivo: ")
dicio = dict()
count = 0
with open(a, "r") as arquivo:
    for palavras in arquivo:
        for letra in palavras:
            if letra.lower() in "qwertyuiopasdfghjklçzxcvbnm":
                if letra.lower() in dicio:
                    dicio[letra.lower()] += 1
                else:
                    dicio[letra.lower()] = 1
dicio = dict(sorted(dicio.items()))
for i, j in dicio.items():
    print(f"{i}: {j}")