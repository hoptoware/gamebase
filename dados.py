

jogos = [{"nome": "", "genero": "", "ano": 0, "nota": 0.0} for _ in range(100)]

n = 100


def registrar():
    print("")
    print("")

    print("Registro de jogos: Apenas aperte enter em Nome do jogo para terminar.")
    print("")

    for i in range(n):
        nome = input("Nome do jogo: ")

        # Sair do registro
        if nome == "":
            print("Registro encerrado.")
            menu()
            break

        genero = input("Gênero do jogo: ")
        ano = input("Ano do jogo: ")
        nota = input("Nota do jogo: ")
        print("")


        # Eu não sei o que isso faz
        """
        try:
            ano = int(ano)
        except ValueError:
            ano = 0

        try:
            nota = float(nota)
        except ValueError:
            nota = 0.0
        """

        jogos[i]["nome"] = nome
        jogos[i]["genero"] = genero
        jogos[i]["ano"] = ano
        jogos[i]["nota"] = nota

        print(f"Jogo {i + 1} registrado com sucesso!")


def menu():    
    print("")
    print("")
    print("GAME SHOP")
    print("====================")

    print("1. REGISTRAR JOGO")
    print("2. REMOVER JOGO")
    print("3. LISTAR JOGOS")
    print("4. FILTRAR JOGOS")
    print("5. SAIR")

    função = input("Escolha uma opção: ")


    match função:
        case "1":
            registrar()    

# Execução do programa
menu()
