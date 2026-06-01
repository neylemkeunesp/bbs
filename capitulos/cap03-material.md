# Capítulo 3: Modelos de Redes Estáticas

## Descrição

Slides e material de apoio do **Capítulo 3** do curso de Bioinformática Aplicada à Biologia de Sistemas.

Este capítulo aborda os fundamentos de análise e modelagem de redes em biologia (grafos, topologia, centralidade) e a implementação usando NetworkX.

---

## Conteúdo

### Parte I: Fundamentos de Redes
- **O que são Redes Biológicas** — PPIs, Redes Metabólicas e Regulatórias Gênicas
- **Teoria dos Grafos** — representação formal, grafos direcionados e não direcionados
- **Matriz de Adjacência e Incidência**
- **Caminhos e Ciclos**

### Parte II: Propriedades de Rede
- **Grau do Vértice** ($k_i$) e Grau Médio ($\langle k \rangle$)
- **Coeficiente de Clusterização**
- **Menor Caminho e Diâmetro**
- **Modularidade e Motivos de Rede (Motifs)**

### Parte III: Medidas de Centralidade
- **Grau (Degree Centrality)** — hubs locais
- **Intermediação (Betweenness)** — gargalos e controle de fluxo
- **Proximidade (Closeness)** — propagação de sinal rápida
- **Autovetor (Eigenvector) e PageRank** — influência global

### Parte IV: Modelos Clássicos
- **Redes Aleatórias (Erdős–Rényi)**
- **Redes Mundo-Pequeno (Watts-Strogatz)**
- **Redes Livres de Escala (Scale-Free / Barabási-Albert)** e Hubs
- **Resiliência e Vulnerabilidade** — falhas aleatórias vs ataques direcionados

---

## Ferramentas Python (NetworkX)

```python
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Criar e visualizar um grafo
G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (2,4), (3,4)])

nx.draw(G, with_labels=True, node_color='lightblue')
plt.show()

# Propriedades
degree_centrality = nx.degree_centrality(G)
betweenness = nx.betweenness_centrality(G)
```

---

## Referências Principais
- Barabási, A.-L. (2016). *Network Science*. Cambridge University Press.
- Newman, M. (2018). *Networks*, 2nd ed. Oxford University Press.
- Alon, U. (2019). *An Introduction to Systems Biology*, 2nd ed. CRC Press.

---

## Exercícios e Projetos

Os exercícios propostos no material envolvem:
1. Representação matricial de grafos simples.
2. Cálculo de métricas de centralidade.
3. Análise do efeito de ataques em hubs.
4. Uso prático da biblioteca `networkx` para analisar o dataset *Karate Club* e redes de interação de proteínas (PPI) reais.
