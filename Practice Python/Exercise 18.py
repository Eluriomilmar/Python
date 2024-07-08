import random
def computador():
    sorteio = []
    for i in range(4):
        sorteio.append(random.randint(0, 9))
    return sorteio


def tentativa():
    vet = []
    i = 0
    while i < 4:
        try:
            a = int(input("Insira número de 0 a 9: "))
            if a > 9:
                raise ValueError
        except:
            print("Insira número inteiro de 0 a 9!")
        else:
            vet.append(a)
            i += 1
    print(f"Tentativa: {vet}")
    return vet


def checagem(vet1, vet2):
    cows = 0
    bulls = 0
    for i in range(4):
        for j in range(4):
            if vet1[i] == vet2[j]:
                if i == j:
                    cows += 1
                else:
                    bulls += 1
    print(f"Cows: {cows}, Bulls: {bulls}")
    return cows, bulls


sorteio = computador()
cows = 0
while cows < 4:
    cows, bulls = checagem(sorteio, tentativa())


