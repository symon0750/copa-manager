from persistencia import salvar_partidas

from utils import ler_inteiro, ler_texto


def status(partidas):
    return len(partidas)


def proximo_id(partidas):

    maior = 0

    for p in partidas:
        if p["id"] > maior:
            maior = p["id"]

    return maior + 1


def achar_selecao(selecoes, id_s):

    for s in selecoes:
        if s["id"] == id_s:
            return s

    return None


def cadastrar_partida(partidas, selecoes):

    print("\n--- CADASTRAR PARTIDA ---\n")

    print("Seleções disponíveis:\n")

    for s in selecoes:
        print(f"{s['id']} - {s['nome']}")

    print()

    nova = {
        "id": proximo_id(partidas),
        "selecao_casa_id": ler_inteiro("ID seleção casa: "),
        "selecao_fora_id": ler_inteiro("ID seleção fora: "),
        "gols_casa": ler_inteiro("Gols casa: "),
        "gols_fora": ler_inteiro("Gols fora: "),
        "fase": ler_texto("Fase: "),
    }

    partidas.append(nova)

    salvar_partidas(partidas)

    print("\nPartida cadastrada com sucesso!")


def listar_partidas(partidas, selecoes):

    print()

    for p in partidas:

        casa = achar_selecao(selecoes, p["selecao_casa_id"])

        fora = achar_selecao(selecoes, p["selecao_fora_id"])

        nome_casa = casa["nome"] if casa else "Desconhecida"

        nome_fora = fora["nome"] if fora else "Desconhecida"

        print(
            f"{nome_casa} {p['gols_casa']} x {p['gols_fora']} {nome_fora} ({p['fase']})"
        )


def filtrar_por_fase(partidas):

    fase = ler_texto("Fase: ").lower()

    print()

    for p in partidas:

        if fase in p["fase"].lower():
            print(p)


def total_gols(partidas):

    total = 0

    for p in partidas:

        total += p["gols_casa"] + p["gols_fora"]

    return total


def media_gols(partidas):

    if len(partidas) == 0:
        return 0

    return total_gols(partidas) / len(partidas)


def calcular_estatisticas(selecao, partidas):

    id_s = selecao["id"]

    pontos = 0
    gols_pro = 0
    gols_contra = 0

    for p in partidas:

        # casa
        if p["selecao_casa_id"] == id_s:

            gols_pro += p["gols_casa"]
            gols_contra += p["gols_fora"]

            if p["gols_casa"] > p["gols_fora"]:
                pontos += 3

            elif p["gols_casa"] == p["gols_fora"]:
                pontos += 1

        # fora
        if p["selecao_fora_id"] == id_s:

            gols_pro += p["gols_fora"]
            gols_contra += p["gols_casa"]

            if p["gols_fora"] > p["gols_casa"]:
                pontos += 3

            elif p["gols_fora"] == p["gols_casa"]:
                pontos += 1

    return {
        "selecao_id": id_s,
        "pontos": pontos,
        "saldo": gols_pro - gols_contra,
        "gols_pro": gols_pro,
    }


def classificacao(partidas, selecoes):

    tabela = []

    for s in selecoes:
        tabela.append(calcular_estatisticas(s, partidas))

    tabela = sorted(tabela, key=lambda x: (x["pontos"], x["saldo"]), reverse=True)

    print("\n--- CLASSIFICAÇÃO ---\n")

    pos = 1

    for t in tabela:

        selecao = achar_selecao(selecoes, t["selecao_id"])

        nome = selecao["nome"] if selecao else "Desconhecida"

        print(
            f"{pos}º {nome} - "
            f"{t['pontos']} pts | "
            f"SG: {t['saldo']} | "
            f"GP: {t['gols_pro']}"
        )

        pos += 1
