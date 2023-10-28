def calculo(valor):
    if valor > 3000:
        return (valor - 3000) * 0.35 + 2000 * 0.2
    if valor > 1000:
        return (valor - 1000) * 0.2
    else:
        return 0


valor = float(input("Insira o salário: "))
print("O valor do salário é de %6.2f e imposto a ser pago é de %6.2f" % (valor, calculo(valor)))