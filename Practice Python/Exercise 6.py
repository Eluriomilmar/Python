"""Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)"""
import time

a = "asdf asdf"
def pali(a):
    a = a.replace(" ", "")
    for i in range(len(a)):
        if a[i] != a[(len(a)-1-i)]:
            return False
    return True

a = str(input("Insira a palavra ou frase para verificar se é palíndromo: "))
print(f"Verificando se '{a}', descontados os espaços, é palíndromo ...")
for i in range(50):
    time.sleep(0.05)
    print("-", end= "")
print("\n")
if pali(a) == True:
    print(f"A frase '{a}' é palíndromo.")
else:
    print(f"A frase '{a}' não é palíndromo.")

