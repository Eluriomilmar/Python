import re


with open("soletrando.txt") as arquivo:
    with open("soletrando2.txt", "w") as arquivo2:
        for tudo in arquivo:
            tudo = tudo.lstrip()
            tudo = tudo.rstrip()
            tudo = tudo.replace(";", "")
            tudo = tudo.replace(".", "")
            arquivo2.write(tudo)
            arquivo2.write("\n")
        arquivo2.close()
    arquivo.close()