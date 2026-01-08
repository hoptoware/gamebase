import sqlite3

# =========================
# BANCO DE DADOS
# =========================


def conectar():
    conn = sqlite3.connect("jogos.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        genero TEXT,
        ano INTEGER,
        nota REAL
    )
    """)

    conn.commit()
    return conn


# =========================
# REGISTRAR JOGO
# =========================
def registrar():
    conn = conectar()
    cursor = conn.cursor()

    print("\nRegistro de jogos (ENTER no nome para sair)\n")

    while True:
        nome = input("Nome do jogo: ")
        if nome == "":
            print("Registro encerrado.")
            conn.close()
            menu()
            break

        genero = input("Gênero do jogo: ")
        ano = int(input("Ano do jogo: "))
        nota = float(input("Nota do jogo: "))

        cursor.execute("""
        INSERT INTO jogos (nome, genero, ano, nota)
        VALUES (?, ?, ?, ?)
        """, (nome, genero, ano, nota))

        conn.commit()
        print("Jogo registrado com sucesso!\n")


# =========================
# LISTAR JOGOS
# =========================
def listar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM jogos")
    jogos = cursor.fetchall()

    print("\nLista de jogos:\n")

    if not jogos:
        print("Nenhum jogo registrado.\n")

    for jogo in jogos:
        print(f"ID: {jogo[0]}")
        print(f"Nome: {jogo[1]}")
        print(f"Gênero: {jogo[2]}")
        print(f"Ano: {jogo[3]}")
        print(f"Nota: {jogo[4]}")
        print("")


    continuar = input("Aperte Enter para continuar...")
    conn.close()


# =========================
# REMOVER JOGO
# =========================
def remover():
    conn = conectar()
    cursor = conn.cursor()

    listar()
    try:
        id_jogo = int(input("Digite o ID do jogo que deseja remover: "))

        cursor.execute("DELETE FROM jogos WHERE id = ?", (id_jogo,))
        conn.commit()

        if cursor.rowcount == 0:
            print("ID não encontrado.")
        else:
            print("Jogo removido com sucesso!")

    except ValueError:
        print("ID inválido.")

    conn.close()
    menu()


# =========================
# FILTRAR JOGOS
# =========================
def filtrar():
    conn = conectar()
    cursor = conn.cursor()

    print("\nFiltrar jogos por:")
    print("1. Gênero")
    print("2. Ano")
    print("3. Nota mínima")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        genero = input("Digite o gênero: ")
        cursor.execute("SELECT * FROM jogos WHERE genero = ?", (genero,))

    elif opcao == "2":
        ano = int(input("Digite o ano: "))
        cursor.execute("SELECT * FROM jogos WHERE ano = ?", (ano,))

    elif opcao == "3":
        nota = float(input("Nota mínima: "))
        cursor.execute("SELECT * FROM jogos WHERE nota >= ?", (nota,))

    else:
        print("Opção inválida.")
        conn.close()
        menu()
        return

    jogos = cursor.fetchall()

    print("\nResultados:\n")
    if not jogos:
        print("Nenhum jogo encontrado.")

    for jogo in jogos:
        print(f"ID: {jogo[0]}")
        print(f"Nome: {jogo[1]}")
        print(f"Gênero: {jogo[2]}")
        print(f"Ano: {jogo[3]}")
        print(f"Nota: {jogo[4]}")
        print("")

    conn.close()
    menu()


# =========================
# MENU
# =========================
def menu():
    print("\nGAME SHOP")
    print("====================")
    print("1. REGISTRAR JOGO")
    print("2. REMOVER JOGO")
    print("3. LISTAR JOGOS")
    print("4. FILTRAR JOGOS")
    print("5. SAIR")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            registrar()
        case "2":
            remover()
        case "3":
            listar()
            menu()
        case "4":
            filtrar()
        case "5":
            print("Saindo...")
            exit()
        case _:
            print("Opção inválida.")
            menu()


# =========================
# EXECUÇÃO
# =========================
menu()