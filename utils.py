import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausar_pro_menu():
    input("\nPressione ENTER para continuar...")


def mostrar_status(qtd_selecoes, qtd_jogadores, qtd_partidas):
    print(
        f"Status: {qtd_selecoes} seleções | "
        f"{qtd_jogadores} jogadores | "
        f"{qtd_partidas} partidas cadastradas"
    )
    print("-" * 60)


def ler_inteiro(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_texto(msg):
    while True:
        texto = input(msg).strip()

        if texto != "":
            return texto

        print("Campo obrigatório.")


def confirmar(msg):
    while True:
        op = input(f"{msg} (S/N): ").strip().upper()

        if op in ("S", "N"):
            return op == "S"

        print("Digite S ou N.")


def escolher_ordem():
    print()

    print("1 - Crescente")
    print("2 - Decrescente")

    op = ler_inteiro("Escolha: ")

    return op == 2


def linha():
    print("-" * 60)
