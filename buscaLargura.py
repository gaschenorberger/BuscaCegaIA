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

from collections import deque
from labirinto import posicaoInicial, posicaoFinal, obterVizinhos

def buscaLargura(mostrarOrdem=False, contar=False):
    """Procura a saída olhando primeiro as casas mais perto do início."""
    # mostrarOrdem mostra cada casa visitada; contar devolve quantas casas foram vistas.
    # A fila guarda as casas que ainda vamos testar e o caminho feito até cada uma.
    fila = deque([(posicaoInicial, [posicaoInicial])])
    # Já colocamos o início na fila; marcamos para não colocá-lo de novo.
    visitados = {posicaoInicial}
    posicoesExploradas = 0

    while fila:
        # Pegamos a primeira casa da fila, como a primeira pessoa de uma fila.
        posicaoAtual, caminho = fila.popleft()
        # Somamos uma à contagem de casas testadas.
        posicoesExploradas += 1

        if mostrarOrdem:
            print(f"{posicoesExploradas}. {posicaoAtual}")

        # Chegamos à saída: entregamos o caminho e, se pedido, a contagem.
        if posicaoAtual == posicaoFinal:
            return (caminho, posicoesExploradas) if contar else caminho

        # Colocamos no fim da fila cada casa ao lado que ainda não apareceu.
        for vizinho in obterVizinhos(posicaoAtual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    # Acabaram as casas para testar, então não encontramos a saída.
    return (None, posicoesExploradas) if contar else None


# Mostra o resultado na tela quando executamos este arquivo.
if __name__ == "__main__":
    print("Ordem de exploração da BFS:")
    resultado = buscaLargura(True)

    print("Caminho encontrado pela Busca em Largura:")
    if resultado:
        for posicao in resultado:
            print(posicao)
    else:
        print("Nenhum caminho encontrado")