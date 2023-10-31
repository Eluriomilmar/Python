# Versão recursiva do cálculo de Pi
# Como esse programa não será usado por alguém, eu não reduzi o valor do input em 1, portanto 0 = 1

valor = int(input("Insira a quantidade de iterações que se deseja usar no cálculo de Pi: "))

numerador = 4
def calculo_denominador(i):
    if i == 0:
        return 3
    else:
        aux = (2*i)*(2*i+1)*(2*i+2)
        if i%2 == 0:
            return -(numerador/aux) + calculo_denominador(i-1)
        else:
            return (numerador/aux) + calculo_denominador(i-1)

print("O valor de Pi com %i iterações é igual a: %f" % (valor, calculo_denominador(valor)))