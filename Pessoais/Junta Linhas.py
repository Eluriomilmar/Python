


with open("texto.txt", "r+", encoding="ISO-8859-1") as arquivo:
    conteudo = arquivo.read().replace("\n", " ")
    with open("texto_novo.txt", "a", encoding="ISO-8859-1") as arquivo_novo:
        arquivo_novo.write(f"{conteudo}")
