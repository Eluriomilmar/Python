""" Write a program to read through the mail box data and when you find line that starts with "From", you will split the line into words using the split function.
We are interested in who sent the message, which is the second word on the From line."""


with open("mbox-short.txt", "r") as f:
    frase = f.readlines()
    for linha in frase:
        if linha.startswith("From "):
            print(linha.split()[1])