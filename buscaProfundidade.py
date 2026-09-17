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

from labirinto import posicaoInicial, posicaoFinal, obterVizinhos

def buscaProfundidade(mostrarOrdem=False, contar=False):
    """Procura a saída seguindo um caminho até onde der antes de tentar outro."""
    # mostrarOrdem mostra cada casa visitada; contar devolve quantas casas foram vistas.
    # A pilha guarda as casas que ainda vamos testar e o caminho feito até cada uma.
    pilha = [(posicaoInicial, [posicaoInicial])]
    visitados = set()
    posicoesExploradas = 0

    while pilha:
        # Pegamos a última casa colocada na pilha, como o prato do topo de uma pilha.
        posicaoAtual, caminho = pilha.pop()

        # Se já passamos por esta casa, vamos para a próxima.
        if posicaoAtual in visitados:
            continue

        # Marcamos esta casa como visitada e somamos uma à contagem.
        visitados.add(posicaoAtual)
        posicoesExploradas += 1

        if mostrarOrdem:
            print(f"{posicoesExploradas}. {posicaoAtual}")

        # Chegamos à saída: entregamos o caminho e, se pedido, a contagem.
        if posicaoAtual == posicaoFinal:
            return (caminho, posicoesExploradas) if contar else caminho

        # Colocamos as casas ao lado na pilha para tentar depois.
        for vizinho in obterVizinhos(posicaoAtual):
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho]))

    # Acabaram as casas para testar, então não encontramos a saída.
    return (None, posicoesExploradas) if contar else None


# Mostra o resultado na tela quando executamos este arquivo.
print("Ordem de exploração da DFS:")
resultado = buscaProfundidade(True)

print("Caminho encontrado pela Busca em Profundidade:")
if resultado:
    for posicao in resultado:
        print(posicao)
else:
    print("Nenhum caminho encontrado")