""" Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade."""


def leiaInt():
    while True:
        try:
            a = int(input("Insira valor numérico: "))
        except ValueError:
            print("Valor inválido.")
        except AttributeError:
            print("Valor inválido.")
        except KeyboardInterrupt:
            print("Usuário interrompeu a execução do programa.")
        else:
            return a


def leiaFloat():
    while True:
        try:
            a = float(input("Insira valor Real: "))
        except ValueError:
            print("Valor digitado não é um número Real.")
        except AttributeError:
            print("Valor inválido")
        except KeyboardInterrupt:
            print("Usuário interrompeu a execução do programa. ")
        else:
            return a


f1 = leiaFloat()
i1 = leiaInt()
print(f"O valor do número Inteiro digitado foi {i1}\nO valor do número Real digitado foi {f1}")