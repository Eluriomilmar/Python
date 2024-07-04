"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)"""

def lista():
    notas = list()
    cont = 0
    while cont >= 0:
        cont = float(input("Insira o valor da nota: "))
        if cont < 0:
            return notas
        else:
            notas.append(cont)

def dicionario(notas):
    turma = dict()
    maior = -1
    menor = -1
    total = 0
    qtd = 0
    turma["notas"] = notas
    for i in turma["notas"]:
        if maior == -1:
            maior = i
            menor = i
            total += i
            qtd += 1
        else:
            if maior < i:
                maior = 1
            if menor > i:
                menor = i
            total += i
            qtd += 1
    turma["maior"] = maior
    turma["menor"] = menor
    turma["media"] = total/qtd
    return turma


notas = lista()
turma = dicionario(notas)
print(f"Notas da turma: {turma["notas"]}\nMaior nota: {turma["maior"]}\nMenor nota: {turma["menor"]}\nMédia: {turma["media"]}")