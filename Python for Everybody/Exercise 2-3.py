"""Write a program to prompt the user for hours and rate per hour to compute gross pay."""


a = []
a.append(float(input("Insira a quantidade de horas trabalhadas: ")))
a.append(float(input("Insira o valor recebido pelas horas trabalhadas: ")))
a.append(a[1]/a[0])
print(f"Foram recebidos R${a[1]:.2f} por {a[0]:.1f} horas de trabalho, uma proporção de R${a[2]:.2f} por hora.")