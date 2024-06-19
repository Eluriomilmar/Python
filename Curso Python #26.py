#Faça um programa uqe leia uma frase pelo teclado e mostre: QUantas vezes aparece a letra "A", em que posição ela aparece pela primeira vez e em que posição ela aparece pela última vez
frase = input("Insira frase aqui: ")
contagem = frase.count("a") + frase.count("A")
print(f"A quantidade de letras A é igual a: {contagem}\nA primeira ocorrência da letra A é na posição: {frase.upper().find("A")}\nA última ocorrência da letra A é na posição: {frase.upper().rfind("A")}")