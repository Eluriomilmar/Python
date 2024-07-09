def cria_lista():
    lista = []
    for i in range(101):
        lista.append(i)
    return lista

def valida_palpite():
    while True:
        try:
            a = str(input(f"O número é maior, menor ou igual a {numero}? ")).upper()
            if a != "MAIOR" and a!= "MENOR" and a != "IGUAL":
                raise ValueError
        except:
            print("Valores válidos são Maior, Menor e Igual.")
        else:
            return a



def jogo():
    possibilidades = cria_lista()
    tentativas = 0
    global numero
    anterior = -1
    while True:
        try:
            numero = possibilidades[len(possibilidades) // 2]
            if anterior == numero:
                raise IndexError
            palpite = valida_palpite()
            anterior = numero
            if palpite == "MAIOR":
                possibilidades = possibilidades[len(possibilidades) // 2:]
                tentativas += 1
            elif palpite == "MENOR":
                possibilidades = possibilidades[:len(possibilidades) // 2]
                tentativas += 1
            else:
                tentativas += 1
                print(f"O número que você pensou é {numero}\nForam feitas {tentativas} tentativas até acertar.")
                break
        except IndexError:
            print("Você está trapaceando! Encerrando o programa.")
            break


jogo()