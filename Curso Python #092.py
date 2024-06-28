from datetime import datetime
trab = dict()
trab["ano_atual"] = int(datetime.now().year)
trab["nome"] = str(input("Insira o nome da pessoa: "))
trab["idade"] = int(input(f"Insira ano de nascimento de {trab["nome"]}: "))
trab["cart_trab"] = int(input(f"Insira o número da carteira de trabalho (0 = não tem): "))
if trab["cart_trab"] != 0:
    trab["ano_contrat"] = int(input(f"Insira o ano de contratação: "))
    trab["salario"] = int(input(f"Insira o salário de {trab["nome"]}: "))
print(f"- O nome da pessoa é {trab["nome"]}: ")
print(f"- A idade de {trab["nome"]} é {trab["idade"]}: ")
if trab["cart_trab"] != 0:
    print(f"- O valor do CTPS é {trab["cart_trab"]}")
    print(f"- O valor do salário é igual a {trab["salario"]}")
    if (trab["ano_contrat"] + 30) < (trab["idade"] + 65):
        print(f"- {trab["nome"]} pode se aposentar em {trab["ano_contrat"] + 30 }")
    else:
        print(f"- {trab["nome"]} pode se aposentar em {trab["idade"] + 65} ou {trab["idade"] + 60}, a depender do sexo")
else:
    print(f"- {trab["nome"]} pode se aposentar com 65 ou 60, a depender do sexo")
