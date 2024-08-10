import keyboard
from time import sleep
from datetime import datetime

with open("lag.txt", "a") as arquivo:
    a = input("Insira a tecla de registro: ")
    b = input("Insira a tecla de parada: ")
    while True:
        c = keyboard.read_key()
        if c == a:
            arquivo.write(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+":"+str(datetime.today().minute)+"\n")
            print(str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+":"+str(datetime.today().minute))
        if c == b:
            break
