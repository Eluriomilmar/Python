"""Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com parênteses abertos e fechados na ordem correta."""
aberto = 0
fechado = 0
expressao = str(input("Insira expressão matemática com parênteses: "))
for i in range(len(expressao)):
    if expressao[i] == "(":
        aberto += 1
    elif expressao[i] == ")":
        fechado += 1
    if fechado > aberto:
        print("Função em algum momento possui mais parênteses fechados que abertos.")
        break
    if i == (len(expressao)-1) and (aberto > fechado):
        print("Função termina com parênteses sem fechar.")
        break
    elif i == (len(expressao)-1) and (aberto == fechado):
        print(f"A Função {expressao} é coerente com seus parênteses.")