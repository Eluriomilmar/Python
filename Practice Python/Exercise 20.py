"""Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean."""


 random import randint

def cria_string(tam_string):
    n = 0
    string = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    while n < tam_string:
        if n == 0:
            string.append(randint(-10, 10))
            n += 1
        else:
            if string[n-1] == 10:
                break
            string.append(randint(string[n-1] + 1, 10))
            n += 1
    return string


def procura_num(num, lista):
    while True:
        if len(lista) > 1:
            if len(lista) == 3:
                if lista[1] == num:
                    lista = lista[1]
                    break
                if lista[0] == num:
                    lista = lista[0]
                    break
                else:
                    lista = lista[2]
                    break
            elif lista[(len(lista)//2)] < num:
                lista = lista[len(lista)//2:]
                print(lista)
            else:
                lista = lista[:len(lista)//2]
                print(lista)
    if lista == num:
        print(f"O número {num} faz parte da lista.")
    else:
        print(f"O número {num} não faz parte da lista")


procura_num(3, cria_string(10))
