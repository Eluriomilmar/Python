"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below."""

def numero():
    while True:
        try:
            primo = int(input("Insira número a ser verificado se é primo: "))
            if primo < 1:
                raise ValueError
        except:
            print("Insira número inteiro maior que 0!")
        else:
            return primo


def checagem(n):
    if n == 1 or n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primo(valor):
    if valor == True:
        print("O número inserido é primo.")
    else:
        print("O número inserido não é primo")


primo(checagem(numero()))
