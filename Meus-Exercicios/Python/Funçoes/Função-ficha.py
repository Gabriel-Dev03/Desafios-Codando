def titulo(msg):
    print("=" *(len(msg)))
    print(msg)
    print("=" *(len(msg)))

def ficha():
    nome = input("Nome do jogador: ")
    gols = input("Número de gols: ")

    if nome.strip() == "":
        nome = "<desconhecido>"
    if gols.strip() == "" or not gols.isnumeric():
        gols = 0
    else:
        gols = int(gols)

    titulo("FICHA DO JOGADOR")
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")

ficha()
