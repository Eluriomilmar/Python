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
            arquivo.write(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m"+" - Lag\n")
            print(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m - Lag")
            arquivo.flush()
            sleep(0.5)
        if e == b:
            arquivo.write(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m"+" - Queda\n")
            print(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m - Queda")
            arquivo.flush()
            sleep(0.5)
        if e == c:
            break
        if e == d:
            input("Programa pausado, aperte enter para continuar.")
            print("Programa reinicializado.")
