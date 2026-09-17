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

# Cada linha abaixo é uma linha do labirinto. O número 1 é caminho; 0 é parede.
labirinto = [
    [1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1]
]


# O primeiro número da posição é a linha; o segundo é a coluna.
posicaoInicial = (0, 0)
posicaoFinal = (4, 4)

def obterVizinhos(posicao):
    """Recebe uma posição e devolve as casas livres ao lado dela."""
    linha, coluna = posicao

    # Vamos olhar as quatro casas ao lado: cima, baixo, esquerda e direita.
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

        # Só guardamos a casa se ela estiver dentro do mapa e não for parede.
        if (
            0 <= novaLinha < len(labirinto)
            and 0 <= novaColuna < len(labirinto[0])
            and labirinto[novaLinha][novaColuna] == 1
        ):
            vizinhos.append((novaLinha, novaColuna))

    return vizinhos


print(obterVizinhos((0, 0)))
print(obterVizinhos((1, 1)))