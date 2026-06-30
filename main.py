from utils import limpar_tela, pausar_pro_menu, mostrar_status

import selecoes
import jogadores
import partidas

from persistencia import (
    carregar_selecoes,
    carregar_jogadores,
    carregar_partidas,
    salvar_selecoes,
    salvar_jogadores,
    salvar_partidas,
)

selecoes_lista = carregar_selecoes()
jogadores_lista = carregar_jogadores()
partidas_lista = carregar_partidas()


while True:

    limpar_tela()

    print("=" * 60, "⚽ COPA MANAGER 2026 - FIFA ⚽", "=" * 60)

    mostrar_status(
        selecoes.status(selecoes_lista),
        jogadores.status(jogadores_lista),
        partidas.status(partidas_lista),
    )

    print()
    print("----------- SELEÇÕES -----------")
    print("1 - Cadastrar seleção")
    print("2 - Listar seleções")
    print("3 - Buscar seleção")
    print("4 - Filtrar seleções")

    print()
    print("----------- JOGADORES ----------")
    print("5 - Cadastrar jogador")
    print("6 - Listar jogadores")
    print("7 - Filtrar jogadores")
    print("8 - Estatísticas jogadores")

    print()
    print("----------- PARTIDAS -----------")
    print("9 - Cadastrar partida")
    print("10 - Listar partidas")
    print("11 - Classificação")

    print()
    print("----------- SISTEMA ------------")
    print("12 - Salvar dados")
    print("0 - Sair")

    print()

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        selecoes.cadastrar_selecao(selecoes_lista)
        pausar_pro_menu()

    elif opcao == "2":
        selecoes.listar_selecoes(selecoes_lista)
        pausar_pro_menu()

    elif opcao == "3":
        selecoes.buscar_por_nome(selecoes_lista)
        pausar_pro_menu()

    elif opcao == "4":
        selecoes.filtrar_selecoes(selecoes_lista)
        pausar_pro_menu()

    elif opcao == "5":
        jogadores.cadastrar_jogador(jogadores_lista, selecoes_lista)
        pausar_pro_menu()

    elif opcao == "6":
        jogadores.listar_jogadores(jogadores_lista, selecoes_lista)
        pausar_pro_menu()

    elif opcao == "7":
        jogadores.menu_filtros(jogadores_lista)
        pausar_pro_menu()

    elif opcao == "8":
        jogadores.estatisticas(jogadores_lista, selecoes_lista)
        pausar_pro_menu()

    elif opcao == "9":
        partidas.cadastrar_partida(partidas_lista, selecoes_lista)
        pausar_pro_menu()

    elif opcao == "10":
        partidas.listar_partidas(partidas_lista, selecoes_lista)
        pausar_pro_menu()

    elif opcao == "11":
        partidas.classificacao(partidas_lista, selecoes_lista)
        pausar_pro_menu()

    elif opcao == "12":
        salvar_selecoes(selecoes_lista)
        salvar_jogadores(jogadores_lista)
        salvar_partidas(partidas_lista)

        print("\nDados salvos com sucesso!")
        pausar_pro_menu()

    elif opcao == "0":

        salvar_selecoes(selecoes_lista)
        salvar_jogadores(jogadores_lista)
        salvar_partidas(partidas_lista)

        print("\nEncerrando sistema...")
        break

    else:
        print("Opção inválida!")
        pausar_pro_menu()
