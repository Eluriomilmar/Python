"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, 
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""

def fatorial(x, show = "N"):
    total = 1
    while x > 1:
        total = total * x
        x = x - 1
        if show == "S":
            print(f"{total}x{x}")
    return (total)

coisa = fatorial(5,"S")