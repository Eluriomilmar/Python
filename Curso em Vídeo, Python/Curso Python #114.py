"""Crie um código em Python que teste se o site pudim está acessível pelo computador usado."""
import requests
def checa_site(url):
    ok = requests.get(url)
    if ok.status_code == 200:
        return "online"
    else:
        return "offline"


def checa_string():
    while True:
        try:
            site = str(input("Insira url do site a ser testado: "))
        except:
            print("Erro! ")
        else:
            return site


print(checa_site(checa_string()))
