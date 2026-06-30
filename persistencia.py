SEPARADOR = ";"


def carregar_arquivo(caminho, montar_objeto):
    lista = []

    try:
        arquivo = open(caminho, "r", encoding="utf-8")

        for linha in arquivo:

            linha = linha.strip()

            if linha == "":
                continue

            lista.append(montar_objeto(linha))

        arquivo.close()

    except FileNotFoundError:
        print(f"Arquivo '{caminho}' ainda não existe.")

    return lista


def salvar_arquivo(caminho, lista, montar_linha):
    arquivo = open(caminho, "w", encoding="utf-8")

    for item in lista:
        arquivo.write(montar_linha(item) + "\n")

    arquivo.close()


def montar_linha_selecao(selecao):

    return SEPARADOR.join(
        [
            str(selecao["id"]),
            selecao["nome"],
            selecao["confederacao"],
            selecao["grupo"],
            str(selecao["ranking_fifa"]),
            str(selecao["titulos"]),
        ]
    )


def montar_selecao(linha):

    dados = linha.split(SEPARADOR)

    return {
        "id": int(dados[0]),
        "nome": dados[1],
        "confederacao": dados[2],
        "grupo": dados[3],
        "ranking_fifa": int(dados[4]),
        "titulos": int(dados[5]),
    }


def montar_linha_jogador(j):

    return SEPARADOR.join(
        [
            str(j["id"]),
            j["nome"],
            str(j["selecao_id"]),
            j["posicao"],
            str(j["idade"]),
            str(j["gols"]),
        ]
    )


def montar_jogador(linha):

    dados = linha.split(SEPARADOR)

    return {
        "id": int(dados[0]),
        "nome": dados[1],
        "selecao_id": int(dados[2]),
        "posicao": dados[3],
        "idade": int(dados[4]),
        "gols": int(dados[5]),
    }


def montar_linha_partida(p):

    return SEPARADOR.join(
        [
            str(p["id"]),
            str(p["selecao_casa_id"]),
            str(p["selecao_fora_id"]),
            str(p["gols_casa"]),
            str(p["gols_fora"]),
            p["fase"],
        ]
    )


def montar_partida(linha):

    dados = linha.split(SEPARADOR)

    return {
        "id": int(dados[0]),
        "selecao_casa_id": int(dados[1]),
        "selecao_fora_id": int(dados[2]),
        "gols_casa": int(dados[3]),
        "gols_fora": int(dados[4]),
        "fase": dados[5],
    }


def carregar_selecoes():
    return carregar_arquivo("selecoes.txt", montar_selecao)


def carregar_jogadores():
    return carregar_arquivo("jogadores.txt", montar_jogador)


def carregar_partidas():
    return carregar_arquivo("partidas.txt", montar_partida)


def salvar_selecoes(lista):
    salvar_arquivo("selecoes.txt", lista, montar_linha_selecao)


def salvar_jogadores(lista):
    salvar_arquivo("jogadores.txt", lista, montar_linha_jogador)


def salvar_partidas(lista):
    salvar_arquivo("partidas.txt", lista, montar_linha_partida)


def salvar_tudo(selecoes, jogadores, partidas):

    salvar_selecoes(selecoes)

    salvar_jogadores(jogadores)

    salvar_partidas(partidas)

    print("\nDados salvos com sucesso!")
