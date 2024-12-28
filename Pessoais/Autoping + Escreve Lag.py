from datetime import datetime
from time import sleep
import re
import subprocess

mes = str(input("Insira mês de registro: "))
ano = str(input("Insira ano de registro: "))
tolerancia = int(input("Insira valor numérico para a tolerância de lag, em ms: "))
print(f"Tolerância de lag de {tolerancia}ms")
with (open(mes + " de " + ano + ".txt", "a") as arquivo):
    vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    indice = 0
    preenchido = False
    while True:
        sleep(0.1)
        try:
            dia = 0
            mes = 0
            hora = 0
            minuto = 0
            a = subprocess.check_output("ping google.com -n 1", shell=True)
            a = str(a)
            a = (re.search(r"Average = (\d+)", a, re.MULTILINE).group(1))
            a = float(a)
        except:
            if len(str(datetime.today().day)) < 2:
                dia = 1
            if len(str(datetime.today().month)) < 2:
                mes = 1
            if len(str(datetime.today().hour)) < 2:
                hora = 1
            if len(str(datetime.today().minute)) < 2:
                minuto = 1
            #arquivo.write(" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                        #": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Timeout.\n")
            #print(f" "*dia+str(datetime.today().day)+"-"+" "*mes+str(datetime.today().month)+"-"+str(datetime.today().year)+
                        #": "+" "*hora+str(datetime.today().hour)+"h"+" "*minuto+str(datetime.today().minute)+"m"+" - Timeout.")
            indice = 0
            #arquivo.flush()
            preenchido = False
        if preenchido:
            media = 0
            for i in range(10):
                media += vetor[i]
            media = media/10
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
                      (str(a - (tolerancia + media)))[:5:] + "ms acima da tolerância.")
                arquivo.flush()
        if indice == 9:
            preenchido = True
            vetor[indice] = a
            indice = 0
        else:
            vetor[indice] = a
            indice += 1
