def escolha():
    with open("nomes.txt", "a") as f:
        f.write("")
        print("Arquivo criado com sucesso.")
        while True:
            try:
                print("Escolha o que deseja fazer\n")
                print("1: Cadastrar nova pessoa\n2: Listar pessoas cadastradas\n3: Sair do programa")
                opcao = str(input("Digite opção desejada: "))
            except:
                print("Como você fez isso dar errado???")
            else:
                if opcao == "1":
                    escrever()
                elif opcao == "2":
                    abrir()
                elif opcao == "3":
                    break
                else:
                    return escolha()

def abrir():
    with open("nomes.txt", "r") as f:
        print(f.read())


def escrever():
    with open("nomes.txt", "a") as f:
        f.write(str(input("Insira nome e idade a serem cadastrados: ")))
        f.write("\n")
