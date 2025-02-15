from datetime import datetime
from time import sleep
import re
import subprocess

mes = str(input("Insira mês de registro: "))
ano = str(input("Insira ano de registro: "))
tolerancia = int(input("Insira valor numérico para a tolerância de lag, em ms: "))
print(f"Tolerância de lag de {tolerancia}ms")
with (open(mes + " de " + ano + ".txt", "a") as arquivo):
    vetor = [0, 0, 0, 0, 0]
    indice = 0
    timeout = 0
    preenchido = False
    queda = 0
    while True:
        sleep(0.1)
        try:
            dia = 0
            mes = 0
            hora = 0
            minuto = 0
            a = subprocess.check_output("ping google.com -n 1",timeout=1, shell=True)
            a = str(a)
            a = (re.search(r"Average = (\d+)", a, re.MULTILINE).group(1))
            a = float(a)
            if a == 1000:
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
            queda += 1
            if queda == 2:
                arquivo.write(" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                            ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Timeout.\n")
                print(f" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                            ": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Timeout.")
                arquivo.flush()
                queda = 0
                sleep(60)
            indice = 0
            preenchido = False
        if preenchido:
            queda = 0
            timeout = 0
            media = 0
            for i in range(5):
                media += vetor[i]
            media = media/5
            if a > media + tolerancia:
                if len(str(datetime.today().day)) < 2:
                    dia = 1
                if len(str(datetime.today().month)) < 2:
                    mes = 1
                if len(str(datetime.today().hour)) < 2:
                    hora = 1
                if len(str(datetime.today().minute)) < 2:
                    minuto = 1
                arquivo.write(f" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+
                              str(datetime.today().year)+": "+" "*hora+str(datetime.today().hour)+"h"+
                              " "*minuto+str(datetime.today().minute)+"m"+" - Lag de " + str(a) +"ms, " +
                              (str(a - (tolerancia + media)))[:5:] + "ms acima da tolerância.\n")
                print(f" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+
                      str(datetime.today().year)+": "+" "*hora+str(datetime.today().hour)+"h"+
                      " "*minuto+str(datetime.today().minute)+"m"+" - Lag de " + str(a) +"ms, "+
                      str(a - (tolerancia + media))[:5:] + "ms acima da tolerância.")
                arquivo.flush()
        if indice == 4:
            preenchido = True
            vetor[indice] = a
            indice = 0
        else:
            vetor[indice] = a
            indice += 1
