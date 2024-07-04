#Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#-À vista/dinheiro/cheque: 10% de desconto
#-À vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
preco = float(input("Insira o preço do produto: "))
pagamento = int(input("Selecione a condição de pagamento\n1: À vista no dinheiro ou cheque.\n2: À vista no cartão.\n3: Em até 2x no cartão.\n4: Parcelado em 3x ou mais no cartão.\nMétodo de pagamento: "))
if pagamento == 1:
    preco = preco * 0.9
    print(f"O valor a ser pago no produto é igual a {preco:.2f}")
elif pagamento == 2:
    preco = preco * 0.95
    print(f"O valor a ser pago no produto é igual a {preco:.2f}")
elif pagamento == 3:
    preco = preco
    print(f"O valor a ser pago no produto é igual a {preco:.2f}")
elif pagamento == 4:
    preco = preco * 1.2
    print(f"O valor a ser pago no produto é igual a {preco:.2f}")
else:
    print("Método de pagamento inválido, reinicie o programa.")