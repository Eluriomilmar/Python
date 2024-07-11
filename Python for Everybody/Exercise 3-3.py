"""Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.
If the score is between 0.0 and 1.0, print a grade using the following table:"""

def checa_input():
    try:
        a = float(input("Insira número de 0 a 1: "))
        if a > 1 or a < 0:
            raise ValueError
    except:
        print("Somente números de 0 a 1 serão aceitos!")
        return checa_input()
    else:
        return a


nota = checa_input()
if nota >= 0.9:
    print("Nota A")
elif nota >= 0.8:
    print("Nota B")
elif nota >= 0.7:
    print("Nota C")
elif nota >= 0.6:
    print("Nota D")
else:
    print("Nota F")