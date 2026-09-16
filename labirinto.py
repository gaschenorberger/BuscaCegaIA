"""
Trabalho de Inteligência Artificial - Algoritmos de Busca

Integrantes:
Gabriel Alvise Schenorberger
Gustavo Augusto
João Gabriel Gnoatto Arataque
Pedro Henrique Honório

Algoritmos:
- Busca em Profundidade
- Busca em Largura

Problema:
- Problema do Labirinto
"""

labirinto = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1]
]


posicaoInicial = (0, 0)
posicaoFinal = (4, 4)

def obterVizinhos(posicao):
    linha, coluna = posicao

    movimentos = [
        (-1, 0),  # Cima
        (1, 0),   # Baixo
        (0, -1),  # Esquerda
        (0, 1)    # Direita
    ]

    vizinhos = []

    for movimentoLinha, movimentoColuna in movimentos:
        novaLinha = linha + movimentoLinha
        novaColuna = coluna + movimentoColuna

        if (
            0 <= novaLinha < len(labirinto)
            and 0 <= novaColuna < len(labirinto[0])
            and labirinto[novaLinha][novaColuna] == 1
        ):
            vizinhos.append((novaLinha, novaColuna))

    return vizinhos


print(obterVizinhos((0, 0)))
print(obterVizinhos((1, 1)))