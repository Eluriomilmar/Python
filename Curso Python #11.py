#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la. Considere que cada L de tinta pinta uma área de 2m²
altura = float(input("Insira a altura da parede: "))
largura = float(input("Insira a largura da parede: "))
print(f"A parede possui uma área de {altura*largura:.2f}m², e para pinta-la serão gastos {(altura*largura)/2:.2f}L de tinta")