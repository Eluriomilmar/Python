import keyboard
from time import sleep
from datetime import datetime

with (open("lag.txt", "a") as arquivo):
    a = input("Insira a tecla de registro: ")
    b = input("Insira a tecla de parada: ")
    c = input("Insire a tecla de pausa: ")
    while True:
        d = keyboard.read_key()
        if d == a:
            arquivo.write(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m"+"\n")
            print(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+"h"+str(datetime.today().minute)+"m")
            sleep(0.5)
        if d == b:
            break
        if d == c:
            input("Programa pausado, aperte enter para continuar.")
            print("Programa reinicializado.")
