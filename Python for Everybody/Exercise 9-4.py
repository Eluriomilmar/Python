""" Add code to the above program to figure out who has the most messages in the file."""


a = input("Insira nome do arquivo aqui: ")
maximo = None
dicio = dict()
with open(a, "r") as arquivo:
    for palavras in arquivo:
        palavras = palavras.splitlines()
        for linha in palavras:
            linha = linha.split(" ")
            if linha[0] == "From":
                if linha[1] in dicio:
                    dicio[linha[1]] += 1
                else:
                    dicio[linha[1]] = 1
for i, k in dicio.items():
    print(f"{i}: {k}")
    if maximo == None or maximo < k:
        pessoa = i
        maximo = k
print(f"O endereço {pessoa} tem a maior quantidade de mensagens no arquivo, com {maximo} mensagens.")