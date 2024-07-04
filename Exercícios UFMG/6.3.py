#progrma de verificação de palíndromo

while True:
    try:
        palindromo = str(input("Insira string a ser verificada se é palíndromo: "))
        break
    except ValueError:
        print("Alguma coisa deu errado, oxe, achei que isso seria impossível aqui, só escrevi esse código pra fixar na minha cabeça socorro")

def pali_check(palavra):
    if len(palavra)%2 == 0:
        tamanho = len(palavra)/2
        tamanho = int(tamanho)
        if palavra[:tamanho:] == palavra[:tamanho-1:-1]:
            print("Palavra é palíndromo!")
        else:
            print("Palavra não é palíndromo!")
    else:
        tamanho = (int(len(palavra)/2))
        if palavra[:tamanho:] == palavra[:tamanho:-1]:
            print("Palavra é palíndromo!")
        else:
            print("Palavra não é palíndromo!")

pali_check(palindromo)