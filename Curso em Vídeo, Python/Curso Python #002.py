#Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uam mensagem com a data formatada.
import datetime
hoje_ano = datetime.datetime.now().year
hoje_mes = datetime.datetime.now().month
hoje_dia = datetime.datetime.now().day
dia = int(input("Insira o dia de nascimento do usuário: "))
mes = int(input("Insira o mês de nascimento do usuário: "))
ano = int(input("Insira o ano de nascimento do usuário: "))
conta = hoje_ano + hoje_mes/12 + hoje_dia/30 - ano - mes/12 - dia /30
print("O usuário tem aproximadamente %.0f anos" % conta)