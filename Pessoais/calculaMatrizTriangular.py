def check_S_or_N():
    erro = True
    n = input()
    if (n != 'S') and (n != 's') and (n != 'N') and (n != 'n'):
        print("Somente são aceitos input 'S' e 'N'!")
        return check_S_or_N()
    return n


def check_if_float():
    erro = True
    while erro:
        try:
            n = float(input())
            erro = False
        except ValueError:
            print("Insira número!", end=" ")
    return n


def check_if_int():
    erro = True
    while erro:
        try:
            n = int(input())
            erro = False
        except ValueError:
            print("Insira número inteiro!", end=" ")
    return n


def casas_decimais():
    print("Qual a precisão desejada(Max: 11)?", end=" ")
    n = check_if_int()
    if (n > 11) or (n < 1):
        print("Insira número entre 1 e 11!")
        return casas_decimais()
    return n


def Chama_Preenche_Linha_Coeficiente():
    print("Deseja inserir linha(S/N)?", end=" ")
    Sentinela = check_S_or_N()
    if Sentinela == 's' or Sentinela == 'S':
        Termos = []
        Coeficientes = []
        Contador = 0
        while Sentinela == 's' or Sentinela == 'S':
            Contador += 1
            Termos.append(Preenche_linha(Contador))
            Coeficientes.append(preenche_coeficiente(Contador))
            print("Deseja inserir nova linha(S/N)?", end=" ")
            Sentinela = check_S_or_N()
        return Termos, Coeficientes
    else:
        print("Nenhum dado inserido, encerrando programa.")
        return 0, 0


def Preenche_linha(total_colunas):
    linha = []
    for x in range(total_colunas):
        print("Insira valor do coeficiente a%i%i:" % (total_colunas, x + 1), end=" ")
        linha.append(check_if_float())
    return linha


def preenche_coeficiente(marcador):
    print("Insira o valor do termo b%i:" % (marcador), end=" ")
    coeficiente = check_if_float()
    return coeficiente


def tp1(Coeficientes, Termos):
    Incognitas = []
    for i in range(len(Coeficientes)):
        Acum = 0
        for j in range(i):
            Acum += Coeficientes[i][j] * Incognitas[j]
        if i == 0:
            if Coeficientes[0][0] == 0:
                Acum = float("inf")
            else:
                Acum = Termos[0] / Coeficientes[0][0]
        else:
            Acum = (Termos[i] - Acum)
            if Acum != 0 and Coeficientes[i][i] != 0:
                Acum = Acum / Coeficientes[i][i]
            elif Acum == 0 and Coeficientes[i][i] != 0:
                Acum = 0
            elif Acum != 0 and Coeficientes[i][i] == 0:
                Acum = float("inf")
            else:  # Acum == 0 and Coeficientes[i][i] == 0:
                Acum = None
        Incognitas.append(Acum)
    return Incognitas


def Exibe_Sistema(Coeficientes, Termos, Incognitas):
    Precisao = casas_decimais()
    for i in range(len(Coeficientes)):
        if i > 0:
            for j in range(len(Coeficientes[i])):
                print("{:+.{}f}".format(Incognitas[j] * Coeficientes[i][j], Precisao), end=" ")
                if j == i:
                    print("     " * Precisao * (len(Coeficientes) - len(Coeficientes[i])), end="  ")
        else:
            print("{:+.{}f}".format(Incognitas[i] * Coeficientes[i][i], Precisao), end=" ")
            print("     " * Precisao * (len(Coeficientes) - len(Coeficientes[i])), end="  ")
        print("=  {:.{}f}".format(Termos[i], Precisao))
    for i in range(len(Incognitas)):
        print("O valor da incógnita X%i é: " % (i + 1), "{:.{}f}".format(Incognitas[i], Precisao))


Termos, Coeficientes = Chama_Preenche_Linha_Coeficiente()
if Termos != 0:
    Incognitas = tp1(Termos, Coeficientes)
    Exibe_Sistema(Termos, Coeficientes, Incognitas)
    for i in range(len(Incognitas)):
        if Incognitas[i] == float("inf") or Incognitas[i] == None:
            print(
                "Aviso: O valor da incógnita X%i é indeterminado. \nIsso deve causar problemas no cálculo ou exibição dos resultados mas resolvi deixar assim à titulo de curiosidade\nMinha primeira opção era usar 'exit()'" % (
                    i))