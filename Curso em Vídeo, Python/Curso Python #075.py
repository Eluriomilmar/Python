#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) QUais foram os números pares.
tupla = (int(input("Insira o primeiro valor: ")), int(input("Insira o segundo valor: ")), int(input("Insira o terceiro valor: ")), int(input("Insira o quarto valor: ")))
print(f"O número 9 apareceu {tupla.count(9)}\nO primeiro número 3 foi digitado na posição {tupla.index(3)+1}\nOs números pares digitados foram: ", end = "")
for i in tupla:
    if i%2 == 0:
        print(f"{i} ", end="")