#Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uam mensagem com a data formatada.
import datetime
hoje = datetime.datetime.now()
hoje = int(hoje.toordinal())
dia = int(input("Insira o dia de nascimento do usuário: "))
mes = int(input("Insira o mês de nascimento do usuário: "))
ano = int(input("Insira o ano de nascimento do usuário: "))
conta = hoje - (ano*365.25 + mes*30.416 + dia)
conta = conta/365
print("O usuário tem aproximadamente %.0f anos" % conta)