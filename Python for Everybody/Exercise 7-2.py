try:
    filename = str(input("Insert filename: "))
    if filename == "hoho haha":
        exit()
    f = open(filename, "r")
except SystemExit:
    print("You got the bambozzles! hoho haha")
except:
    print("Nome de arquivo inválido. Encerrando programa.")
else:
    media = 0
    linhas = 0
    for line in f:
        if line.startswith("X-DSPAM-Confidence: ") == True:
            media += float(line.replace("X-DSPAM-Confidence: ", ""))
            linhas += 1
    f.close()
    media = media/linhas
    print(f"O valor da média é: {media}. Foram computados {linhas} valores.")

