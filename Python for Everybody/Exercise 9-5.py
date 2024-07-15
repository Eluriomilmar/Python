"""This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from
(i.e., the whole email address).
At the end of the program, print out the contents of your dictionary."""

end = dict()
arquivo = input("Insira nome do arquivo: ")
with open(arquivo, "r") as arquivo:
    for palavras in arquivo:
        palavras = palavras.splitlines()
        for linha in palavras:
            linha = linha.split(" ")
            if linha[0] == "From":
                resto = linha[1].split("@")
                if linha[1] in end:
                    end[linha[1]] += 1
                else:
                    end[linha[1]] = 1
for i, j in end.items():
    print(f"{i}: {j}")
