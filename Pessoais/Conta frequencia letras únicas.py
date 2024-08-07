with open("soletrando2.txt", "r") as dicionario:
    dicio = dict()
    for palavras in dicionario:
        vetor = list(palavras)
        for i in range(len(vetor)):
            for j in range(len(vetor)):
                if i == j:
                    j += 1
                elif vetor[i] == vetor[j]:
                    vetor[j] = ""
        for i in vetor:
            if i.upper() not in dicio:
                dicio[i.upper()] = 1
            else:
                dicio[i.upper()] += 1
dicio.pop("\n")
dicio["A"] = dicio["A"] + dicio["Á"] + dicio["À"] + dicio["Ã"] + dicio["Â"]
dicio["E"] = dicio["E"] + dicio["É"] + dicio["Ê"]
dicio["I"] = dicio["I"] + dicio["Í"]
dicio["O"] = dicio["O"] + dicio["Ó"] + dicio["Õ"] + dicio["Ô"]
dicio["U"] = dicio["U"] + dicio["Ú"]
dicio["C"] = dicio["C"] + dicio["Ç"]
dicio.pop("À")
dicio.pop("Á")
dicio.pop("Â")
dicio.pop("Ã")
dicio.pop("É")
dicio.pop("Ê")
dicio.pop("Í")
dicio.pop("Ó")
dicio.pop("Õ")
dicio.pop("Ô")
dicio.pop("Ú")
dicio.pop("Ç")
dicio.pop("")
ordenado = sorted(dicio.items(), key=lambda x:x[1], reverse=True)
ordenado = dict(ordenado)
for i, j in ordenado.items():
    print(f"{i}: {j}")

