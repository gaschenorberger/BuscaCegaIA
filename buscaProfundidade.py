from labirinto import labirinto, posicaoInicial, posicaoFinal, obterVizinhos

def buscaProfundidade():
    pilha = [(posicaoInicial, [posicaoInicial])]
    visitados = set()

    while pilha:
        posicaoAtual, caminho = pilha.pop()

        if posicaoAtual == posicaoFinal:
            return caminho

        if posicaoAtual in visitados:
            continue

        visitados.add(posicaoAtual)

        vizinhos = obterVizinhos(posicaoAtual)

        for vizinho in vizinhos:
            if vizinho not in visitados:
                novoCaminho = caminho + [vizinho]
                pilha.append((vizinho, novoCaminho))

    return None