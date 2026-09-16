from labirinto import labirinto, posicaoInicial, posicaoFinal, obterVizinhos

def buscaProfundidade():
    pilha = [(posicaoInicial, [posicaoInicial])]
    visitados = set()