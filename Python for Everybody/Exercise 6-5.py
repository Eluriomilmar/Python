"""Exercise 5: Take the following Python code that stores a string:`

str = 'X-DSPAM-Confidence:0.8475'

Use find and string slicing to extract the portion of the string after the colon character and then use the float function to
convert the extracted string into a floating point number."""

def extrair(frase):
    inicio = frase.find(':')
    fim = frase.find('"', inicio)
    return frase[inicio+1:fim]




str = "X-DSPAM-Confidence:0.8475"
numero = float(extrair(str))
print(f"O número é igual a {numero}")