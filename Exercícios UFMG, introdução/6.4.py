#progrma de verificação de palíndromo

while True:
    try:
        palindromo = str(input("Insira string a ser verificada se é palíndromo: "))
        break
    except ValueError:
        print("Alguma coisa deu errado, oxe, achei que isso seria impossível aqui, só escrevi esse código pra fixar na minha cabeça socorro")

def pali_check(palavra):
    i = 0
    while i < len(palavra):
        if (palavra[i:i+1:]) != (palavra[-i-1:-i-2:-1]): #As operações verificam caractere por caractere em sentidos opostos
            print("A palavra %s não é palíndromo" % palavra)
            break
        elif i >= len(palavra)/2:
                print("A palavra %s é palíndromo" % palavra)
                break
        i = i + 1

pali_check(palindromo)

#também é possível fazer o mesmo exercício usando somente operações de string, definindo len(palavra)
#e comparando palavra[0:len(palavra)/2-1:0] com palavra[len(palavra)*-1:len(palavra)*-1:-1] ou operação similar.