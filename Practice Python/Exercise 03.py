"""and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new = []
while True:
    try:
        limite = int(input("Insira o valor máximo para se adicionar à nova lista: "))
    except:
        print("Insira número inteiro!")
    else:
        break

for i in range(len(a)):
    if a[i] < limite:
        new.append(a[i])
print(new)