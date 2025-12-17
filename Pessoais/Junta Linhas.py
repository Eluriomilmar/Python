with open("texto.txt", "r", encoding="ISO-8859-1") as arquivo:    #Abre arquivo de texto no modo leitura
    conteudo = arquivo.read().replace("\n", " ")    #Lê o conteúdo do arquivo de texto e substitui quebras de linha por espaços, armazena conteúdo na variável "conteudo".
    with open("texto.txt", "w", encoding="ISO-8859-1") as arquivo2:    #Abre arquivo de texto no modo de escrita
        conteudo = arquivo2.write(conteudo)    #Escreve no arquivo o conteúdo armazenado no segundo passo
        arquivo2.close()    #Fecha o modo escrita do bloco de notas
    arquivo.close()    #Fecha o modo leitura do bloco de notas
