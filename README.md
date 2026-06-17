# TSP-RNN-SA

Projeto desenvolvido para a disciplina de Pesquisa Operacional.

## Objetivo

Reproduzir e avaliar o algoritmo proposto no artigo:

> Repetitive Nearest Neighbor Based Simulated Annealing Search Optimization Algorithm for Traveling Salesman Problem (2021)

e propor uma melhoria baseada em um mecanismo de Reheating para o Simulated Annealing.

---

## Problema

O Problema do Caixeiro Viajante (Traveling Salesman Problem - TSP) consiste em determinar uma rota de menor custo que visite todas as cidades exatamente uma vez e retorne à cidade de origem.

O TSP é um dos problemas clássicos NP-Hard da otimização combinatória.

---

## Algoritmo Base

O algoritmo estudado combina:

1. Repetitive Nearest Neighbor (RNN)
2. Simulated Annealing (SA)

Fluxo geral:

```
RNN → Solução Inicial → SA → Melhor Solução
```

---

## Contribuição Proposta

Adicionar um mecanismo de **Reheating** ao Simulated Annealing.

A ideia é aumentar temporariamente a temperatura quando o algoritmo permanecer várias iterações consecutivas sem melhorar a solução, permitindo escapar de mínimos locais.

Parâmetros do Reheating:
- `stagnation_limit`: número de iterações sem melhora que dispara o reheating
- `reheating_factor`: fator multiplicativo aplicado à temperatura atual

---

## Estrutura do Projeto

```text
.
├── data/
│   ├── eil51.tsp
│   ├── berlin52.tsp
│   ├── st70.tsp
│   └── kroA100.tsp
├── docs/
│   └── rnn-sa.pdf
├── results/
│   ├── raw_results.csv
│   ├── summary.csv
│   └── figures/
├── src/
│   ├── config.py       # parâmetros e instâncias
│   ├── tsp.py          # carregamento TSPLIB
│   ├── rnn.py          # Nearest Neighbor e RNN
│   ├── operators.py    # operadores de vizinhança
│   ├── sa.py           # Simulated Annealing + Reheating
│   ├── experiments.py  # runner multi-instância / multi-rodada
│   └── visualization.py
├── main.py             # demo rápido (uma instância)
├── run_experiments.py  # experimento completo
├── pyproject.toml
└── README.md
```

---

## Instâncias Utilizadas

Instâncias da TSPLIB com soluções ótimas conhecidas:

| Instância | Cidades | Ótimo |
|-----------|---------|-------|
| eil51     | 51      | 426   |
| berlin52  | 52      | 7542  |
| st70      | 70      | 675   |
| kroA100   | 100     | 21282 |

Fonte: <https://github.com/mastqe/tsplib>  
Originalmente derivadas da TSPLIB95: <https://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/>

---

## Ambiente

Python 3.12+ com gerenciamento de dependências via `uv`.

Principais bibliotecas: `numpy`, `pandas`, `matplotlib`, `tsplib95`, `tqdm`

---

## Execução

### 1. Instalar as dependências

```bash
uv sync
```

### 2. Demo rápido (uma instância, uma rodada)

```bash
python main.py
```

### 3. Experimento completo (4 instâncias, 30 rodadas cada)

```bash
python run_experiments.py
```

Os resultados são salvos em `results/`:
- `raw_results.csv` — todas as rodadas individuais
- `summary.csv` — estatísticas por algoritmo/instância (best, mean, std, gap%)
- `figures/` — gráficos prontos para o relatório

---

## Status

- [x] Definição do tema e escolha do artigo
- [x] Configuração do ambiente
- [x] Implementação do Nearest Neighbor e RNN
- [x] Implementação do Simulated Annealing
- [x] Implementação do Reheating (contribuição)
- [x] Framework experimental multi-instância / multi-rodada
- [x] Geração de figuras (boxplots, convergência, comparação)
- [ ] Relatório final
