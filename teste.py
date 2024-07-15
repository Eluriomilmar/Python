import string


filename = input("Insira o nome do arquivo: ")
try:
    filehand = open(filename)
except:
    print("Arquivo inválido.")
    exit()
else:
    counts = dict()
    for line in filehand:
        line = line.rstrip()
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

print(counts)