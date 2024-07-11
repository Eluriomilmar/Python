"""Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
The following shows two executions of the program"""


def checa_input():
    try:
        a = float(input(""))
    except:
        print("Insira número! ")
        return checa_input()
    else:
        return a



a = []
print("Insira a quantidade de horas trabalhadas: ", end="")
a.append(checa_input())
print("\nInsira a quantidade de dinheiro recebido: ", end="")
a.append(checa_input())
a.append(a[1]/a[0])
if a[0] > 40:
    a[1] = a[1]*1.5
    a[2] = a[1]/a[0]
print(f"\nForam recebidos R${a[1]:.2f} por {a[0]:.1f} horas de trabalho, uma proporção de R${a[2]:.2f} por hora.")