jogos = [{"nome": "", "genero": "", "ano": 0, "nota": 0.0} for _ in range(100)]

n = 100
qtd = 0 # Quantidade de jogos registrados

def registrar():
    print("")
    print("")

    global qtd

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

        jogos[i]["nome"] = nome
        jogos[i]["genero"] = genero
        jogos[i]["ano"] = ano
        jogos[i]["nota"] = nota

        print(f"Jogo {i + 1} registrado com sucesso!")
        qtd = qtd + 1

def listar():
    print("")
    print("Lista de jogos registrados:")
    print("")

    for i in range(qtd):
        print("Jogo", i + 1, ":")
        print("Nome:", jogos[i]['nome'])
        print("Gênero:", jogos[i]['genero'])
        print("Ano:", jogos[i]['ano'])
        print("Nota:", jogos[i]['nota'])
        print("")

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
        case "3":
            listar()  

# Execução do programa
menu()
