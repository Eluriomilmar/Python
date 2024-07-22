"""Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method."""


from random import choice
from random import randint

def passlen():
    while True:
        try:
            len = int(input("Insira o tamanho desejado para a senha: "))
            if len < 1:
                raise ValueError
            dif = int(input("Insira a dificuldade desejada para a senha(1-3): "))
            if dif < 1 or dif > 3:
                raise ValueError
        except:
            print("Insira somente números inteiros!")
        else:
            return len, dif


def password(length, difficulty):
    vetor1 = ["A", "B", "C", "D", "E", "F", "G"]
    vetor2 = ["a", "b", "c", "d", "e", "f", "g"]
    vetor3 = ["!", "@", "#", "$", "%", "&", "*"]
    vetorTodos = [vetor1, vetor2, vetor3]
    vetorFinal = []
    a = 0
    while a < length:
        vetorFinal.append(choice(vetorTodos[randint(0, difficulty-1)]))
        a += 1
    vetorFinal = "".join(vetorFinal)
    return vetorFinal


len, dif = passlen()
print(f"A senha gerada é: {password(len, dif)}")

