#Melhore o desafio 061 perguntando para o usuário se ele quer mostrar mais alguns termos. O programa deve encerrar quando ele disser que quer mostrar 0 termos.
termo = float(input("Insira o primeiro termo da progressão: "))
razao = float(input("Insira a razão da PA: "))
i = int(input("Quantos termos deseja exibir?"))
acum = 0
while i > acum:
    print(f"O termo {acum+1} é igual a {termo + razao * acum}")
    acum += 1
    if i == acum:
        resposta = input("Deseja exibir mais resultados? (S/N) ")
        if resposta == "S":
            i += int(input("Insira quantas mais iterações deseja exibir: "))
        else:
            print("Programa finalizado com sucesso.")

