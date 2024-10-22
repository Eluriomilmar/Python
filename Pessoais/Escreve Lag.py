import keyboard
from time import sleep
from datetime import datetime

arq = str(input("Insira mês de registro: "))
with (open(arq + ".txt", "a") as arquivo):
    a = input("Insira a tecla de registro de lag: ")
    b = input("Insira a tecla de registro de queda: ")
    c = input("Insire a tecla de pausa: ")
    d = input("Insira a tecla de parada: ")
    while True:
        e = keyboard.read_key()
        dia = 0
        mes = 0
        hora = 0
        minuto = 0
        if e == a:
            if len(str(datetime.today().day)) < 2:
                dia = 1
            if len(str(datetime.today().month)) < 2:
                mes = 1
            if len(str(datetime.today().hour)) < 2:
                hora = 1
            if len(str(datetime.today().minute)) < 2:
                minuto = 1
            arquivo.write(" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                          ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Lag\n")
            print(" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                          ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Lag")
            arquivo.flush()
            sleep(0.5)
        if e == b:
            var = 1
            if len(str(datetime.today().day)) < 2:
                dia = 1
            if len(str(datetime.today().month)) < 2:
                mes = 1
            if len(str(datetime.today().hour)) < 2:
                hora = 1
            if len(str(datetime.today().minute)) < 2:
                minuto = 1
            arquivo.write(" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                          ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Queda\n")
            print(" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                          ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Queda")
            arquivo.flush()
            sleep(0.5)
        if e == c:
            input("Programa pausado, aperte enter para continuar.")
            print("Programa reinicializado.")
        if e == d:
            break
