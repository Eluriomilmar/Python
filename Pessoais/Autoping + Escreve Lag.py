from pythonping import ping
from datetime import datetime
from time import sleep

mes = str(input("Insira mês de registro: "))
ano = str(input("Insira ano de registro: "))
tolerancia = int(input("Insira valor numérico para a tolerância de lag, em ms: "))
print(f"Tolerância de lag de {tolerancia}ms")
with (open(mes + " de " + ano + ".txt", "a") as arquivo):
    vetor = [0, 0, 0, 0]
    indice = 0
    preenchido = False
    while True:
        try:
            dia = 0
            mes = 0
            hora = 0
            minuto = 0
            a = ping("google.com", timeout=1, count=1, interval=1)
            if a.success == False:
                raise Exception
        except:
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
            print(f" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                        ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Queda")
            indice = 0
            arquivo.flush()
            preenchido = False
            sleep(30)
        if preenchido:
            media = (vetor[0] + vetor[1] + vetor[2] + vetor[3])/4
            if a.rtt_avg_ms > media + tolerancia:
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
                        datetime.today().minute) + "m" + " - Lag de " + str(a.rtt_avg_ms) + "ms, " + (str(a.rtt_avg_ms - (tolerancia + media)))[:6:]
                      + "ms acima da tolerância\n")
                print(" " * dia + str(datetime.today().day) + "-" + " " * mes + str(datetime.today().month) + "-" + str(
                    datetime.today().year) +
                        ": " + " " * hora + str(datetime.today().hour) + "h" + " " * minuto + str(
                    datetime.today().minute) + "m" + " - Lag de " + str(a.rtt_avg_ms) + "ms, " + (str(a.rtt_avg_ms - (tolerancia + media)))[:6:]
                      + "ms acima da tolerância")
                arquivo.flush()
        if indice == 3:
            preenchido = True
            vetor[indice] = a.rtt_avg_ms
            indice = 0
        else:
            vetor[indice] = a.rtt_avg_ms
            indice += 1
