def aumentar(n = 1000, a = 20, format = True):
    """
    -> Aumenta em a% o valor de n
    """
    res = (n*(a/100)+n)
    if format == True:
         return moeda(res)
    else:
         return res


def diminuir(n = 1000, a = 20, format = True):
    """
    -> Diminui em a% o valor de n
    """
    res = (n*((100-a)/100))
    if format == True:
         return moeda(res)
    else:
         return res


def dobro(n = 1000, format = True):
    """
    -> Dobra o valor de n
    """
    res = (n*2)
    if format == True:
         return moeda(res)
    else:
         return res


def metade(n = 1000, format = True):
    """
    -> Diminui pela metade o valor de n
    """
    res = (n/2)
    if format == True:
        return moeda(res)
    else:
         return res
    

def moeda(n):
    print(f"R${n:.2f}".center(20))

def resumo(n):
    #(f"{moeda(aumentar(n))}\n{moeda(diminuir(n))}\n{moeda(dobro(n))}\n{moeda(metade(n))}")
    moeda(dobro(n))
