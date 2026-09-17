# Busca em Profundidade e Busca em Largura em um Labirinto

Trabalho de Inteligência Artificial que compara dois algoritmos de busca: **Busca em Profundidade (DFS)** e **Busca em Largura (BFS)**. Os dois procuram um caminho entre o início e a saída do mesmo labirinto.

## Integrantes

- Gabriel Alvise Schenorberger
- Gustavo Augusto
- João Gabriel Gnoatto Arataque
- Pedro Henrique Honório

## Arquivos do projeto

- `labirinto.py`: contém o mapa, as posições inicial e final e a função que encontra as casas livres ao lado de uma posição.
- `buscaProfundidade.py`: executa a DFS, que segue um caminho até onde puder antes de tentar outro.
- `buscaLargura.py`: executa a BFS, que examina primeiro as casas mais próximas do início.
- `benchmark.py`: mede o tempo, o pico de memória e a quantidade de posições examinadas pelas duas buscas.

**Mantenha os quatro arquivos `.py` na mesma pasta.** Todos são necessários para executar o benchmark.

## Requisitos

- Python 3.12

O projeto usa apenas módulos que vêm com o Python. Não é necessário instalar bibliotecas com `pip`.

## Como executar

Abra o PowerShell na pasta do projeto. Para conferir se o Python está disponível, execute:

```powershell
python --version
```

Para ver a ordem em que a DFS examina as posições e o caminho encontrado:

```powershell
python .\buscaProfundidade.py
```

Para ver a ordem em que a BFS examina as posições e o caminho encontrado:

```powershell
python .\buscaLargura.py
```

Para comparar as duas buscas:

```powershell
python .\benchmark.py
```

Ao executar o benchmark, as posições vizinhas e os resultados das buscas aparecem antes das medidas. Isso acontece porque os arquivos das buscas também imprimem informações quando são importados.

## Como ler os resultados

No mapa, `1` representa uma casa livre e `0` representa uma parede. Cada posição é escrita como `(linha, coluna)`. O início é `(0, 0)` e a saída é `(4, 4)`.

- **Movimentos no caminho:** quantidade de passos do início até a saída.
- **Posições examinadas:** quantidade de casas que o algoritmo verificou até encontrar a saída.
- **Tempo:** duração média de uma execução, em milissegundos.
- **Pico de memória:** maior quantidade de memória acompanhada durante uma execução, em KiB.

Com o labirinto atual, as duas buscas encontram um caminho de **8 movimentos**. A DFS examina **9 posições** e a BFS examina **11 posições**. Os valores de tempo podem variar entre execuções e computadores.

## Como o benchmark mede

Para cada busca, o programa faz 10 amostras de tempo. Em cada amostra, executa a busca 1.000 vezes e calcula o tempo médio de uma execução. A memória é medida separadamente, com uma execução por amostra.

Para calcular as médias e os desvios padrão apresentados, o programa descarta o maior e o menor valor de cada conjunto de 10 amostras.