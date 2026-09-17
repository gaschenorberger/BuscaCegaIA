from collections import deque
from labirinto import posicaoInicial, posicaoFinal, obterVizinhos

def buscaLargura(mostrarOrdem=False, contar=False):
    fila = deque([(posicaoInicial, [posicaoInicial])])
    visitados = {posicaoInicial}
    posicoesExploradas = 0

    while fila:
        posicaoAtual, caminho = fila.popleft()
        posicoesExploradas += 1

        if mostrarOrdem:
            print(f"{posicoesExploradas}. {posicaoAtual}")

        if posicaoAtual == posicaoFinal:
            return (caminho, posicoesExploradas) if contar else caminho

        for vizinho in obterVizinhos(posicaoAtual):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return (None, posicoesExploradas) if contar else None

if __name__ == "__main__":
    print("Ordem de exploração da BFS:")
    resultado = buscaLargura(True)

    print("Caminho encontrado pela Busca em Largura:")
    if resultado:
        for posicao in resultado:
            print(posicao)
    else:
        print("Nenhum caminho encontrado")