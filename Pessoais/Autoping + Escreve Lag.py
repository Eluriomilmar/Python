from pythonping import ping
from datetime import datetime
from time import sleep

mes = str(input("Insira mês de registro: "))
ano = str(input("Insira ano de registro: "))
lag = int(input("Insira valor numérico para a tolerância de lag, em ms: "))
queda = int(input("Insira valor numérico para a tolerância de queda, em ms: "))
print(f"Tolerância de lag de {lag}ms")
with (open(mes + " de " + ano + ".txt", "a") as arquivo):
    dia = 0
    mes = 0
    hora = 0
    minuto = 0
    vetor = [0, 0, 0, 0]
    indice = 0
    preenchido = False
    while True:
        try:
            a = ping("google.com", interval=1, count=1)
        except:
            arquivo.write(" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                        ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Queda\n")
            print(" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                        ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Queda")
            indice = 0
            arquivo.flush()
            preenchido = False
            sleep(30)
        if preenchido:
            media = (vetor[0] + vetor[1] + vetor[2] + vetor[3])/4
            if a.rtt_avg > media + lag / 1000:
                if len(str(datetime.today().day)) < 2:
                    dia = 1
                if len(str(datetime.today().month)) < 2:
                    mes = 1
                if len(str(datetime.today().hour)) < 2:
                    hora = 1
                if len(str(datetime.today().minute)) < 2:
                    minuto = 1
                arquivo.write(
                    " " * dia + str(datetime.today().day) + "-" + " " * mes + str(datetime.today().month) + "-" + str(
                        datetime.today().year) +
                    ": " + " " * hora + str(datetime.today().hour) + "h" + " " * minuto + str(
                        datetime.today().minute) + "m" + " - Lag\n")
                print(" " * dia + str(datetime.today().day) + "-" + " " * mes + str(datetime.today().month) + "-" + str(
                    datetime.today().year) +
                        ": " + " " * hora + str(datetime.today().hour) + "h" + " " * minuto + str(
                    datetime.today().minute) + "m" + " - Lag")
                arquivo.flush()
        if indice == 3:
            preenchido = True
            indice = 0
        else:
            indice += 1
