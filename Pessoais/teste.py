import re, codecs

with open("soletrando.txt", "r", encoding="latin_1") as arquivo:
    for palavras in arquivo:
        print(palavras)