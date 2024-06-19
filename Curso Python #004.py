#Faça um programa que leia algo pelo teclado e mostra na tela o seu tipo primitivo e todas as informações possíveis sobre ela

def v_ou_f(vf):
    if vf == True:
        return "Verdadeiro"
    else:
        return "Falso"

leitura = input("Insira o input desejado: ")
numerico = leitura.isnumeric()
letra = leitura.isalpha()
alnum = leitura.isalnum()
caixa_baixa = leitura.islower()
caixa_alta = leitura.isupper()
tam = len(leitura)
print (f"O valor `{leitura}` possui os seguintes atributos")
print(f"Numérico: {v_ou_f(numerico)}")
print(f"Alfabético: {v_ou_f(letra)}")
print(f"Alfanumérico: {v_ou_f(alnum)}")
print(f"Possui caracteres somente em caixa alta: {v_ou_f(caixa_baixa)}")
print(f"Possui caracteres somente em caixa baixa: {v_ou_f(caixa_alta)}")
print(f"Foram digitados {tam} caracteres")
