try:
    a = int(input("Insira número de 0 a 9: "))
    if a > 9:
        raise ValueError
except:
    print("Insira número inteiro de 0 a 9!")
else:
    vet.append(a)