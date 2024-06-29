"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."""
def escreva(a):
    print("~"*len(a))
    print(a)
    print("~"*len(a))


msg = str(input("Insira a mensagem aqui: "))
escreva(msg)