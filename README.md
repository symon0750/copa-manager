# Copa-manager
## Atividade avaliativa do professor

O arquivo main.py é o “menu principal” do sistema. Pra executar o programa, execute o `main.py`

## 1) Cada import

- `from utils import limpar_tela, pausar_pro_menu, mostrar_status`
  - Importa funções auxiliares de utils.py:
    - `limpar_tela()`: limpa a tela do terminal.
    - `pausar_pro_menu()`: pausa a execução até o usuário apertar Enter.
    - `mostrar_status(...)`: mostra quantas seleções, jogadores e partidas existem.

- `import selecoes`
  - Importa as funções de gerenciamento de seleções de selecoes.py.

- `import jogadores`
  - Importa as funções de gerenciamento de jogadores de jogadores.py.

- `import partidas`
  - Importa as funções de gerenciamento de partidas de partidas.py.

- `from persistencia import (...)`
  - Importa funções de persistencia.py para ler e gravar dados em arquivos de texto:
    - `carregar_selecoes()`, `carregar_jogadores()`, `carregar_partidas()`
    - `salvar_selecoes()`, `salvar_jogadores()`, `salvar_partidas()`

## 2) Cada loop

### Loop principal: `while True`
Este é o loop principal do programa. Ele repete indefinidamente até que o usuário escolha a opção `0` para sair.

Em cada volta, ele:
- limpa a tela,
- mostra o menu,
- lê a opção escolhida,
- executa a ação correspondente,
- pausa ou encerra o programa.

Ou seja, ele funciona como um “menu infinito” do sistema.

### Outro “loop” implícito: a leitura da opção
A linha:
- `opcao = input("Escolha uma opção: ")`

não é um loop em si, mas é o ponto onde o programa recebe a escolha do usuário para decidir o caminho do `if/elif/else`.

## 3) O que acontece em cada `if`, `elif` e `else`

O fluxo começa com a leitura da opção do usuário e depois segue por uma estrutura de decisão.

### Opção `1` — Cadastrar seleção
- Chama `selecoes.cadastrar_selecao(selecoes_lista)`.
- Abre o fluxo de cadastro de uma nova seleção.
- Depois chama `pausar_pro_menu()` para voltar ao menu.

### Opção `2` — Listar seleções
- Chama `selecoes.listar_selecoes(selecoes_lista)`.
- Mostra as seleções cadastradas.

### Opção `3` — Buscar seleção
- Chama `selecoes.buscar_por_nome(selecoes_lista)`.
- Procura seleções cujo nome contenha parte do texto digitado.

### Opção `4` — Filtrar seleções
- Chama `selecoes.filtrar_selecoes(selecoes_lista)`.
- Permite filtrar por grupo ou confederação.

### Opção `5` — Cadastrar jogador
- Chama `jogadores.cadastrar_jogador(jogadores_lista, selecoes_lista)`.
- Cria um novo jogador e associa a uma seleção.

### Opção `6` — Listar jogadores
- Chama `jogadores.listar_jogadores(jogadores_lista, selecoes_lista)`.
- Exibe os jogadores cadastrados com a seleção correspondente.

### Opção `7` — Filtrar jogadores
- Chama `jogadores.menu_filtros(jogadores_lista)`.
- Abre opções para filtrar jogadores por posição, idade ou gols.

### Opção `8` — Estatísticas de jogadores
- Chama `jogadores.estatisticas(jogadores_lista, selecoes_lista)`.
- Mostra estatísticas como total de jogadores, gols e artilheiro.

### Opção `9` — Cadastrar partida
- Chama `partidas.cadastrar_partida(partidas_lista, selecoes_lista)`.
- Registra uma nova partida entre duas seleções.

### Opção `10` — Listar partidas
- Chama `partidas.listar_partidas(partidas_lista, selecoes_lista)`.
- Mostra todas as partidas cadastradas.

### Opção `11` — Classificação
- Chama `partidas.classificacao(partidas_lista, selecoes_lista)`.
- Monta a tabela de classificação com pontos, saldo de gols e gols pró.

### Opção `12` — Salvar dados
- Chama as funções de salvamento:
  - `salvar_selecoes(selecoes_lista)`
  - `salvar_jogadores(jogadores_lista)`
  - `salvar_partidas(partidas_lista)`
- Depois imprime “Dados salvos com sucesso!” e volta ao menu.

### Opção `0` — Sair
- Também salva tudo antes de encerrar.
- Imprime “Encerrando sistema...”.
- O `break` interrompe o `while True` e fecha o programa.

### `else` — Opção inválida
- Se o usuário digitar qualquer valor diferente das opções acima, o programa exibe:
  - “Opção inválida!”
- E depois volta ao menu.

## Resumo da lógica geral

O arquivo funciona assim:

1. Carrega os dados dos arquivos.
2. Mostra o menu.
3. Espera a escolha do usuário.
4. Direciona para a função certa.
5. Volta ao menu, salvo quando o usuário decide sair.
