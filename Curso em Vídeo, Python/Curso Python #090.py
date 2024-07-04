#Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.
resultado = dict()
resultado["Nome"] = str(input("Insira o nome do estudante: "))
resultado["Média"] = float(input(f"Insira a média de {resultado.get("Nome")}: "))
if resultado.get("Média") >= 7:
    resultado["Situação"] = "aprovado"
else:
    resultado["Situação"] = "reprovado"
print(f"{resultado.get("Nome")} foi {resultado.get("Situação")} com a média igual a {resultado.get("Média")}")