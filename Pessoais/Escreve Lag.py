import keyboard
from time import sleep
from datetime import datetime

a = datetime.today().minute
print(a)
with open("lag.txt", "a") as arquivo:
    while True:
        a = keyboard.read_key()
        sleep(0.3)
        if a == "7":
            arquivo.write("\n"+str(datetime.today().day)+"-"+str(datetime.today().month)+"-"+
            str(datetime.today().year)+": "+str(datetime.today().hour)+":"+str(datetime.today().minute))
        if a == "9":
            break
