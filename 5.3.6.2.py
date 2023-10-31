# Cálculo iterativo da função de Pi
# Como esse programa não será usado por alguém, eu não reduzi o valor do input em 1, portanto 0 = 1

valor = int(input("Insira a quantidade de iterações que se deseja usar no cálculo de Pi: "))
print("O valor de Pi sendo calculado em %i iterações é igual a: " % valor, end=(""))

def Pi(i):
    aux = 0
    while i >= 0:
        if i == 0:
            aux = aux + 3
            i = i - 1
        else:
            if i%2 == 0:
                aux = aux -4/((2*i)*(2*i+1)*(2*i+2))
                i = i - 1
            else:
                aux = aux + 4/((2*i)*(2*i+1)*(2*i+2))
                i = i - 1
    return aux
print("%f" % Pi(valor))