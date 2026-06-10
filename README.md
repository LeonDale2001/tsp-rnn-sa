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

RNN → Solução Inicial → SA → Melhor Solução

---

## Contribuição Proposta

Adicionar um mecanismo de Reheating ao Simulated Annealing.

A ideia é aumentar temporariamente a temperatura quando o algoritmo permanecer várias iterações consecutivas sem melhorar a solução, permitindo escapar de mínimos locais.

---

## Estrutura do Projeto

```text
.
├── data/
├── docs/
├── results/
├── src/
├── pyproject.toml
└── README.md
```

## Instâncias Utilizadas

As instâncias TSP utilizadas são provenientes da TSPLIB.

Instâncias atualmente utilizadas:

- eil51
- berlin52
- st70

Fonte das instâncias:

https://github.com/mastqe/tsplib

Originalmente derivadas da TSPLIB95:

https://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/

---

## Ambiente

Python 3.12+

Gerenciamento de dependências:

- uv

Principais bibliotecas:

- numpy
- pandas
- matplotlib
- tsplib95
- tqdm

---

## Status

- [x] Definição do tema
- [x] Escolha do artigo
- [x] Definição da contribuição
- [x] Configuração do ambiente
- [ ] Leitura das instâncias TSPLIB
- [ ] Implementação do Nearest Neighbor
- [ ] Implementação do RNN
- [ ] Implementação do Simulated Annealing
- [ ] Implementação do Reheating
- [ ] Experimentos
- [ ] Relatório final


## Execução

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd tsp-rnn-sa
```

### 2. Instalar as dependências

```bash
uv sync
```

### 3. Executar o projeto

```bash
python main.py
```