"""Write a program to read through a file and print the contents of the file (line by line) all in upper case."""


with open("mbox-short.txt", "r") as f:
    frase = f.read().upper()
    print(frase)