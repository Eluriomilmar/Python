def aumentar(n, a):
    """
    -> Aumenta em a% o valor de n
    """
    return (n*(a/100)+n)


def diminuir(n, a):
    """
    -> Diminui em a% o valor de n
    """
    return (n*((100-a)/100))


def dobro(n):
    """
    -> Dobra o valor de n
    """
    return (n*2)


def metade(n):
    """
    -> Diminui pela metade o valor de n
    """
    return (n/2)

def moeda(n):
    i = str(n)
    for j in i:
        if j == ".":
            j = ","
    i = float(n)
    print(f"R${i:.2f}")