"""Exercício Python 109: Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108."""


import moeda


preco = 1000
a = 20
format = True

moeda.aumentar(preco, a, format)
moeda.diminuir(preco, a, format)
moeda.dobro(preco, format)
moeda.metade(preco, format)