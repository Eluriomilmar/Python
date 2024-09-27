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
        if e == a:
            var = 1
            if len(str(datetime.today().day)) < 2:
                var += 1
            if len(str(datetime.today().month)) < 2:
                var += 1
            if len(str(datetime.today().day)) < 2:
                var += 1
            if len(str(datetime.today().hour)) < 2:
                var += 1
            if len(str(datetime.today().minute)) < 2:
                var += 1
            arquivo.write(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m"+" "*var +"- Lag\n")
            print(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m"+" "*var +"- Lag")
            arquivo.flush()
            sleep(0.5)
        if e == b:
            var = 1
            if len(str(datetime.today().day)) < 2:
                var += 1
            if len(str(datetime.today().month)) < 2:
                var += 1
            if len(str(datetime.today().day)) < 2:
                var += 1
            if len(str(datetime.today().hour)) < 2:
                var += 1
            if len(str(datetime.today().minute)) < 2:
                var += 1
            arquivo.write(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m"+" "*var +"- Queda\n")
            print(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m"+" "*var +"- Queda")
            arquivo.flush()
            sleep(0.5)
        if e == c:
            input("Programa pausado, aperte enter para continuar.")
            print("Programa reinicializado.")
        if e == d:
            break
