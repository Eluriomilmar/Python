inicial = float(input("Insira investimento inicial: "))
while inicial <= 0:
    inicial = float(input("Valor inicial deve ser maior que 0: "))
juros = float(input("Insira taxa de juros(%): "))
while juros <= 0:
    juros = float(input("Valor do juros deve ser maior que 0: "))
periodo = float(input("Insira quantidade de períodos: "))
while periodo <= 0:
    periodo = float(input("Valor do período deve ser maior que 0: "))
print(f"O valor registrado no período com juros de {juros}% é igual a: {pow((inicial + 1/juros), periodo)}")