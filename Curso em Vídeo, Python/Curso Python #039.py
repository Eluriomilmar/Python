#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#-Se ele ainda vai se alistar ao serviço militar.
#-Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
from datetime import datetime
ano = datetime.now().year
nascimento = int(input("Insira o ano de nascimento: "))
if ano - nascimento > 18:
    print(f"Já passaram {ano - nascimento - 18} ano(s) do alistamento obrigatório.")
elif ano - nascimento < 18:
    print(f"Faltam {18 - (ano - nascimento)} ano(s) para o alistamento obrigatório.")
else:
    print("O ano corrente é o ano do alistamento obrigatório.")