from persistencia import salvar_jogadores

from utils import ler_inteiro, ler_texto, linha


def status(jogadores):
    return len(jogadores)


def buscar_por_id(jogadores, id_busca):

    for j in jogadores:
        if j["id"] == id_busca:
            return j

    return None


def proximo_id(jogadores):

    maior = 0

    for j in jogadores:
        if j["id"] > maior:
            maior = j["id"]

    return maior + 1


def achar_selecao(selecoes, id_s):

    for s in selecoes:
        if s["id"] == id_s:
            return s

    return None


def cadastrar_jogador(jogadores, selecoes):

    print("\n--- CADASTRAR JOGADOR ---\n")

    print("Seleções disponíveis:\n")

    for s in selecoes:
        print(f"{s['id']} - {s['nome']}")

    print()

    novo = {
        "id": proximo_id(jogadores),
        "nome": ler_texto("Nome: "),
        "selecao_id": ler_inteiro("ID da seleção: "),
        "posicao": escolher_posicao(),
        "idade": ler_inteiro("Idade: "),
        "gols": ler_inteiro("Gols: "),
    }

    jogadores.append(novo)

    salvar_jogadores(jogadores)

    print("\nJogador cadastrado com sucesso!")


def escolher_posicao():

    print("\nPosição:")

    print("1 - Atacante")
    print("2 - Meio-campista")
    print("3 - Defensor")
    print("4 - Goleiro")

    op = int(input("Escolha: "))

    if op == 1:
        return "Atacante"

    elif op == 2:
        return "Meio-campista"

    elif op == 3:
        return "Defensor"

    elif op == 4:
        return "Goleiro"

    else:
        print("Opção inválida. Usando 'Desconhecido'")
        return "Desconhecido"


def listar_jogadores(jogadores, selecoes):

    if len(jogadores) == 0:

        print("\nNenhum jogador cadastrado.")

        return

    print()

    for j in jogadores:

        selecao = achar_selecao(selecoes, j["selecao_id"])

        nome_selecao = selecao["nome"] if selecao else "Desconhecida"

        print(
            f"{j['id']:>2} | "
            f"{j['nome']:<20} | "
            f"{j['posicao']:<10} | "
            f"{nome_selecao:<15} | "
            f"Gols: {j['gols']}"
        )


def filtrar_posicao(jogadores):

    pos = ler_texto("Posição: ").lower()

    for j in jogadores:

        if j["posicao"].lower() == pos:
            print(j)


def filtrar_idade(jogadores):

    min_idade = ler_inteiro("Idade mínima: ")

    max_idade = ler_inteiro("Idade máxima: ")

    for j in jogadores:

        if min_idade <= j["idade"] <= max_idade:
            print(j)


def filtrar_por_selecao(jogadores, selecoes):

    termo = ler_texto("Nome da seleção: ").lower()

    for j in jogadores:

        for s in selecoes:

            if j["selecao_id"] == s["id"] and termo in s["nome"].lower():
                print(j)


def menu_filtros(jogadores):

    print("\n1 - Por posição")
    print("2 - Por idade")
    print("3 - Atacantes com mais de X gols")

    op = ler_inteiro("Escolha: ")

    if op == 1:
        filtrar_posicao(jogadores)

    elif op == 2:
        filtrar_idade(jogadores)

    elif op == 3:

        n = ler_inteiro("Mínimo de gols: ")

        res = filter_atacantes_n_gols(jogadores, n)

        for j in res:
            print(j)


def ordenar(jogadores, chave, desc=False):

    return sorted(jogadores, key=lambda x: x[chave], reverse=desc)


def ordenar_por_gols(jogadores):

    for j in ordenar(jogadores, "gols", True):
        print(j)


def ordenar_por_idade(jogadores):

    for j in ordenar(jogadores, "idade"):
        print(j)


def ordenar_por_nome(jogadores):

    for j in ordenar(jogadores, "nome"):
        print(j)


def map_nomes(jogadores):

    nomes = []

    for j in jogadores:
        nomes.append(j["nome"])

    return nomes


def filter_atacantes_n_gols(jogadores, n):

    resultado = []

    for j in jogadores:

        if j["posicao"].lower() == "atacante" and j["gols"] > n:
            resultado.append(j)

    return resultado


def reduce_total_gols(jogadores):

    total = 0

    for j in jogadores:
        total += j["gols"]

    return total


def reduce_idade(jogadores):

    total = 0

    for j in jogadores:
        total += j["idade"]

    return total


def media_idade(jogadores):

    if len(jogadores) == 0:
        return 0

    return reduce_idade(jogadores) / len(jogadores)


def ver_artilheiro(jogadores):

    if len(jogadores) == 0:
        return

    melhor = jogadores[0]

    for j in jogadores:

        if j["gols"] > melhor["gols"]:
            melhor = j

    print(f"\nArtilheiro: {melhor['nome']} - {melhor['gols']} gols")


def estatisticas(jogadores, selecoes):

    print("\n--- ESTATÍSTICAS ---\n")

    print(f"Total de jogadores: {len(jogadores)}")

    print(f"Total de gols: {reduce_total_gols(jogadores)}")

    print(f"Média de idade: {media_idade(jogadores):.1f}")

    print()

    ver_artilheiro(jogadores)
