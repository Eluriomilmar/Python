with open("texto.txt", "r", encoding="ISO-8859-1") as arquivo:
    conteudo = arquivo.read().replace("\n", " ")
    with open("texto.txt", "w", encoding="ISO-8859-1") as arquivo2:
        conteudo = arquivo2.write(conteudo)
        arquivo2.close()
    arquivo.close()
