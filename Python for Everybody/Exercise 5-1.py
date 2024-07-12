"""Exercise 1: Write a program which repeatedly reads numbers until the user enters "done".
Once "done" is entered, print out the total, count, and average of the numbers.
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number."""
import numbers

def checa_num(total = 0, count = 0):
    try:
        a = input("Insira número, SAIR para sair: ").upper()
        if a == "SAIR":
            average = total/count
            return total, count, average
    except:
        print("Não sei como você chegou até aqui, parabéns.")
    else:
        return checa_num((total + float(a)), (count + 1))


total, contagem, media = checa_num()
print(f"Total: {total}\nContagem: {contagem}\nMédia: {media}")