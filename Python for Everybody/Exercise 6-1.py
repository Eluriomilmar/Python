"""Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards."""


def print_reverso(palavra):
    palavra_len = len(palavra)-1
    while palavra_len >= 0:
        print(palavra[palavra_len])
        palavra_len -= 1


print_reverso("paralelepipedo")