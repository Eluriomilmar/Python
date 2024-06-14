#Crie um script Python que leia dois números e tente mostrar a soma entre eles.
print("O programa irá requisitar dois números e efetuará a sua soma com precisão de duas casas decimais")
numero1 = float(input("Insira o primeiro número da soma: "))
numero2 = float(input("Insira o segundo número da soma: "))
print("O resultado da soma, é igual a: %.2f" % (numero1 + numero2))