"""Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments."""


def conta_caracteres(palavra, caractere):
    cont = 0
    for letra in palavra:
        if letra == caractere:
            cont += 1
    print(cont)


conta_caracteres("banana", "n")