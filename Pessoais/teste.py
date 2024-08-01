import re, codecs

with open("soletrando2.txt", "r") as arquivo:
    count = 0
    for palavras in arquivo:
        if bool(palavras) == True:
            count += 1
    print(count)