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

from statistics import mean, stdev
from time import perf_counter_ns
import tracemalloc

from buscaProfundidade import buscaProfundidade
from buscaLargura import buscaLargura

# Faremos 10 amostras de tempo e 10 amostras de memória para cada busca.
quantidadeMedicoes = 10

# O labirinto é pequeno e uma execução dura muito pouco.
# Por isso, cada amostra de tempo executa a busca 1000 vezes.
execucoesPorMedicao = 1000

# Descarta o maior e o menor valor de cada métrica
def resumirValores(valores):
    # Ordena as 10 amostras e descarta a menor e a maior.
    valoresOrdenados = sorted(valores)
    valoresUsados = valoresOrdenados[1:-1]

    # Calcula média e desvio padrão das 8 amostras restantes.
    return mean(valoresUsados), stdev(valoresUsados)

def medirMetricas(busca):
    # Executa uma vez antes de medir para carregar a função e conferir o resultado.
    # Essa execução inicial não entra nas amostras.
    caminho, posicoesExploradas = busca(contar=True)
    tempos = []
    memorias = []

    # Mede o tempo sem o tracemalloc ativo, pois ele deixaria a busca mais lenta.
    for _ in range(quantidadeMedicoes):
        inicio = perf_counter_ns()

        for _ in range(execucoesPorMedicao):
            busca()

        fim = perf_counter_ns()

        # Converte nanossegundos para milissegundos e divide pelas 1000 execuções.
        # Assim, cada valor representa o tempo médio de uma execução da busca.
        tempoMs = (fim - inicio) / execucoesPorMedicao / 1_000_000
        tempos.append(tempoMs)

    # Mede a memória separadamente: uma execução da busca por amostra.
    for _ in range(quantidadeMedicoes):
        tracemalloc.start()
        busca()

        # O segundo valor retornado é o pico de memória observado durante a busca.
        picoBytes = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        # Converte bytes para KiB.
        memorias.append(picoBytes / 1024)

    return caminho, posicoesExploradas, tempos, memorias

def exibirMetricas(nome, busca):
    caminho, posicoesExploradas, tempos, memorias = medirMetricas(busca)
    mediaTempo, desvioTempo = resumirValores(tempos)
    mediaMemoria, desvioMemoria = resumirValores(memorias)

    print(f"\n{nome}")
    print("Amostras de tempo (ms por execução):", ", ".join(f"{valor:.6f}" for valor in tempos))
    print("Picos de memória (KiB):", ", ".join(f"{valor:.3f}" for valor in memorias))
    print(f"Tempo médio: {mediaTempo:.6f} ms | desvio padrão: {desvioTempo:.6f} ms")
    print(f"Memória média: {mediaMemoria:.3f} KiB | desvio padrão: {desvioMemoria:.3f} KiB")
    print("Solução encontrada:", "sim" if caminho else "não")
    print("Movimentos no caminho:", len(caminho) - 1 if caminho else "sem caminho")
    print("Posições examinadas até a saída:", posicoesExploradas)



exibirMetricas("DFS", buscaProfundidade)
exibirMetricas("BFS", buscaLargura)