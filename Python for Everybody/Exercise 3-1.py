"""Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours."""


a = []
a.append(float(input("Insira a quantidade de horas trabalhadas: ")))
a.append(float(input("Insira o valor recebido pelas horas trabalhadas: ")))
a.append(a[1]/a[0])
if a[0] > 40:
    a[2] = a[2]*1.5
print(f"Foram recebidos R${a[1]:.2f} por {a[0]:.1f} horas de trabalho, uma proporção de R${a[2]:.2f} por hora.")