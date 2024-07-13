frase = "frase aleatória com mais de 4 palavras"
nova_frase = frase.split(" ")
palavras = []
palavras.append(nova_frase[len(nova_frase)-2])
palavras.append(nova_frase[len(nova_frase)-1])
nova_frase.pop()
nova_frase.pop()
ultima = palavras + nova_frase
print(ultima)
ultima = ' '.join(ultima)
print(ultima)