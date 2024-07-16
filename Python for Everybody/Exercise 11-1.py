import re


contagem = 0
expressao = input("Insira uma 'regular expression': ")
a = open("mbox-short.txt", "r")
for linha in a:
    if len(re.findall(expressao, linha)) > 0:
        contagem += 1
print(contagem)
a.close()
