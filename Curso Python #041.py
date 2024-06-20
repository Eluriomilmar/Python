#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: Mirim
#Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 20 anos: Sênior
#Acima de 20 anos: Master
from datetime import datetime
ano = datetime.now().year
nascimento = int(input("Insira o ano de nascimento do atleta: "))
idade = ano - nascimento
if idade <= 9:
    print("O atleta pertence à categoria mirim.")
elif idade <= 14:
    print("O atleta pertence à categoria infantil.")
elif idade <= 19:
    print("O atleta pertence à categoria junior.")
elif idade == 20:
    print("O atleta pertence à categoria sênior.")
else:
    print("O Atleta pertence à categoria master.")