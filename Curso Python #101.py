"""Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições."""
import datetime

def validaVoto(ano):
    atual = datetime.date.today().year
    if (atual - ano < 16):
        return ("NEGADO")
    elif (atual - ano < 19):
        return ("OPCIONAL")
    elif (atual - ano < 70):
        return ("OBRIGATÓRIO")
    else:
        return ("OPCIONAL")

print(validaVoto(int(input("Insira o ano de nascimento do votante: "))))