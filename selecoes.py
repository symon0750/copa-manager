from persistencia import salvar_selecoes

from utils import ler_inteiro, ler_texto, escolher_ordem


def status(selecoes):
    return len(selecoes)


def buscar_por_id(selecoes, id_busca):

    for selecao in selecoes:

        if selecao["id"] == id_busca:
            return selecao

    return None


def proximo_id(selecoes):

    if len(selecoes) == 0:
        return 1

    maior = selecoes[0]["id"]

    for selecao in selecoes:

        if selecao["id"] > maior:
            maior = selecao["id"]

    return maior + 1


def cadastrar_selecao(selecoes):

    print("\n--- CADASTRAR SELEÇÃO ---\n")

    nome = ler_texto("Nome: ")

    confederacao = ler_texto("Confederação: ")

    grupo = ler_texto("Grupo: ").upper()

    ranking = ler_inteiro("Ranking FIFA: ")

    titulos = ler_inteiro("Quantidade de títulos: ")

    nova = {
        "id": proximo_id(selecoes),
        "nome": nome,
        "confederacao": confederacao,
        "grupo": grupo,
        "ranking_fifa": ranking,
        "titulos": titulos,
    }

    selecoes.append(nova)

    salvar_selecoes(selecoes)

    print(f"\nSeleção '{nome}' cadastrada com sucesso!")


def imprimir_selecao(selecao):

    print(
        f"{selecao['id']:>2} | "
        f"{selecao['nome']:<20} | "
        f"{selecao['grupo']:^5} | "
        f"{selecao['confederacao']:<10} | "
        f"Ranking: {selecao['ranking_fifa']:<3} | "
        f"Títulos: {selecao['titulos']}"
    )


def listar_selecoes(selecoes):

    if len(selecoes) == 0:

        print("\nNenhuma seleção cadastrada.")

        return

    print(f"\n", "=" * 75, "SELEÇÕES CADASTRADAS".center(75), "=" * 75, f"\n", f"\n" )

    atributo = escolher_atributo()

    decrescente = escolher_ordem()

    lista = ordenar_por_atributo(selecoes, atributo, decrescente)

    for selecao in lista:

        imprimir_selecao(selecao)


def buscar_por_nome(selecoes):

    termo = ler_texto("\nDigite parte do nome da seleção: ").lower()

    encontrados = []

    for selecao in selecoes:

        if termo in selecao["nome"].lower():

            encontrados.append(selecao)

    print()

    if len(encontrados) == 0:

        print("Nenhuma seleção encontrada.")

        return

    print(f"Foram encontradas {len(encontrados)} seleção(ões).\n")

    for selecao in encontrados:

        imprimir_selecao(selecao)


def escolher_atributo():

    print("\nOrdenar por:")

    print("1 - Nome")
    print("2 - Ranking FIFA")
    print("3 - Títulos")

    opcao = ler_inteiro("Escolha: ")

    if opcao == 1:
        return "nome"

    if opcao == 2:
        return "ranking_fifa"

    if opcao == 3:
        return "titulos"

    print("Opção inválida.")
    return "nome"


def ordenar_por_atributo(lista, atributo, decrescente=False):

    return sorted(lista, key=lambda item: item[atributo], reverse=decrescente)


def filtrar_por_grupo(selecoes):

    grupo = ler_texto("Grupo: ").upper()

    encontrados = []

    for selecao in selecoes:

        if selecao["grupo"] == grupo:
            encontrados.append(selecao)

    if len(encontrados) == 0:

        print("\nNenhuma seleção encontrada.")

        return

    print()

    for selecao in encontrados:
        imprimir_selecao(selecao)


def filtrar_por_confederacao(selecoes):

    conf = ler_texto("Confederação: ").lower()

    encontrados = []

    for selecao in selecoes:

        if selecao["confederacao"].lower() == conf:
            encontrados.append(selecao)

    if len(encontrados) == 0:

        print("\nNenhuma seleção encontrada.")

        return

    print()

    for selecao in encontrados:
        imprimir_selecao(selecao)


def filtrar_selecoes(selecoes):

    print()

    print("1 - Grupo")

    print("2 - Confederação")

    opcao = ler_inteiro("Escolha: ")

    print("-" * 60)

    if opcao == 1:

        filtrar_por_grupo(selecoes)

    elif opcao == 2:

        filtrar_por_confederacao(selecoes)

    else:

        print("Opção inválida.")


def listar_menu_selecoes(selecoes):

    if len(selecoes) == 0:

        print("\nNenhuma seleção cadastrada.")

        return

    print()

    print("=" * 75)

    print("SELEÇÕES".center(75))

    print("=" * 75)

    print()

    for selecao in selecoes:

        imprimir_selecao(selecao)

    print("-" * 60)


def nomes_das_selecoes(selecoes):

    nomes = []

    for selecao in selecoes:

        nomes.append(selecao["nome"])

    return nomes


def quantidade_por_grupo(selecoes, grupo):

    total = 0

    for selecao in selecoes:

        if selecao["grupo"] == grupo.upper():

            total += 1

    return total
