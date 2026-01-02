# Guia para Criar os Capítulos Restantes

Este documento fornece orientações para criar as apresentações dos capítulos 3-5, 7-15.

## 📋 Capítulos Pendentes

### Prioridade Alta (Fundamentos)

- [ ] **Capítulo 3: Static Network Models** (~40 slides)
  - Graph Theory Basics
  - Small-World Networks
  - Network Topology
  - Metabolic Control Analysis

- [ ] **Capítulo 4: The Mathematics of Biological Systems** (~45 slides)
  - Equações diferenciais avançadas
  - Análise de Estabilidade
  - Análise de Sensibilidade

- [ ] **Capítulo 5: Parameter Estimation** (~35 slides)
  - Grid Search
  - Gradient Methods
  - Linearization Techniques

### Prioridade Média (Sistemas Específicos)

- [ ] **Capítulo 7: Protein Systems** (~45 slides)
  - Protein Structure
  - Enzymes
  - Cell Signaling
  - Proteomics

- [ ] **Capítulo 8: Metabolic Systems** (~40 slides)
  - Metabolic Reactions
  - Rate Laws
  - Flux Analysis
  - Metabolomics

- [ ] **Capítulo 9: Signaling Systems** (~40 slides)
  - Signal Transduction Networks
  - Signaling Dynamics
  - Protein Kinase Cascades

- [ ] **Capítulo 10: Population Systems** (~38 slides)
  - Population Growth Models
  - Predator-Prey Dynamics
  - Phase-Plane Analysis

### Prioridade Baixa (Aplicações Avançadas)

- [ ] **Capítulo 11: Integrated Analysis** (~35 slides)
  - Case Study in Yeast
  - Trehalose Cycle
  - Multi-omics Integration

- [ ] **Capítulo 12: Physiological Systems - Heart** (~40 slides)
  - Heart Anatomy
  - Cardiomyocyte Modeling
  - Action Potentials

- [ ] **Capítulo 13: Systems Biology in Medicine** (~35 slides)
  - Drug Development
  - Clinical Applications
  - Personalized Medicine

- [ ] **Capítulo 14: Design of Biological Systems** (~40 slides)
  - Metabolic Engineering
  - Synthetic Biology
  - Gene Circuits

- [ ] **Capítulo 15: Emerging Topics** (~30 slides)
  - Complex Diseases
  - Multi-scale Modeling
  - Future Directions

## 🎨 Template e Estrutura

### 1. Copiar o Template

```bash
cd apresentacoes-bioinformatica/capitulos
cp ../template/beamer-template.tex capitulo03-static-networks.tex
```

### 2. Estrutura Recomendada por Slide

Cada capítulo deve ter aproximadamente:

- **1 slide**: Título
- **1 slide**: Sumário/Índice
- **2-3 slides**: Introdução e objetivos
- **30-40 slides**: Conteúdo principal dividido em seções
  - 3-5 seções principais
  - 6-8 slides por seção
- **2-3 slides**: Exercícios
- **2 slides**: Referências
- **1 slide**: Conclusão/Agradecimentos

### 3. Elementos Obrigatórios

Cada capítulo deve incluir:

#### Seções Básicas
```latex
\section{Introdução}
\section{Conceitos Fundamentais}
\section{Modelagem/Análise}
\section{Aplicações}
\section{Exercícios}
\section{Referências}
```

#### Blocos de Conteúdo

```latex
% Definições importantes
\definicao{Título}{Conteúdo}

% Exemplos práticos
\exemplo{Título}{Conteúdo}

% Alertas e destaques
\importante{Texto importante}

% Equações em destaque
\destaque{$equação$}
```

#### Código Python

Sempre que possível, inclua exemplos de código:

```latex
\begin{lstlisting}[language=Python, caption=Descrição]
import numpy as np
# código aqui
\end{lstlisting}
```

#### Diagramas TikZ

Use diagramas para visualização:

```latex
\begin{tikzpicture}
% diagrama aqui
\end{tikzpicture}
```

## 📝 Checklist por Capítulo

Antes de considerar um capítulo completo, verifique:

- [ ] Slide de título com informações corretas
- [ ] Sumário/Índice
- [ ] Introdução clara com objetivos
- [ ] Pelo menos 3-4 definições importantes usando `\definicao{}`
- [ ] Pelo menos 2-3 exemplos usando `\exemplo{}`
- [ ] Pelo menos 1 bloco de código Python funcional
- [ ] Pelo menos 2 diagramas/figuras (TikZ ou imagens)
- [ ] Seção de exercícios com 3-5 problemas
- [ ] Referências bibliográficas adequadas
- [ ] Slide de conclusão
- [ ] Revisão de português e formatação

## 🔍 Conteúdo Específico por Capítulo

### Capítulo 3: Static Network Models

**Tópicos essenciais:**
- Conceitos de teoria dos grafos (nós, arestas, grau)
- Propriedades topológicas (diâmetro, coeficiente de clustering)
- Redes de escala livre e small-world
- Representação matricial (adjacência, incidência)
- NetworkX em Python para análise de redes
- Reconstrução de redes metabólicas
- Análise de controle metabólico (MCA)

**Código sugerido:**
```python
import networkx as nx

# Criar e analisar uma rede
G = nx.Graph()
G.add_edges_from([(1,2), (2,3), (3,1)])
degree = dict(G.degree())
clustering = nx.clustering(G)
```

### Capítulo 4: Mathematics of Biological Systems

**Tópicos essenciais:**
- Sistemas de EDOs não-lineares
- Pontos de equilíbrio e estabilidade
- Matriz Jacobiana e análise de autovalores
- Bifurcações (saddle-node, Hopf)
- Ciclos limite e oscilações
- Análise de sensibilidade local e global
- Teoremas de estabilidade de Lyapunov

**Código sugerido:**
```python
from scipy.integrate import odeint
import numpy as np

def system(y, t, params):
    # Sistema de EDOs
    dydt = [...]
    return dydt

# Análise de estabilidade via linearização
```

### Capítulo 5: Parameter Estimation

**Tópicos essenciais:**
- Função objetivo (least squares, maximum likelihood)
- Busca em grade (grid search)
- Métodos de gradiente (gradient descent, Newton-Raphson)
- Levenberg-Marquardt
- Algoritmos genéticos
- Identificabilidade de parâmetros
- Validação cruzada

**Código sugerido:**
```python
from scipy.optimize import curve_fit, minimize

# Ajuste de parâmetros
popt, pcov = curve_fit(model, x_data, y_data)

# Análise de confiança
perr = np.sqrt(np.diag(pcov))
```

### Capítulo 7: Protein Systems

**Tópicos essenciais:**
- Níveis de estrutura proteica (1ª, 2ª, 3ª, 4ª)
- Cinética enzimática detalhada
- Inibição enzimática (competitiva, não-competitiva)
- Cascatas de sinalização
- Modificações pós-traducionais
- Proteômica e espectrometria de massas
- Modelagem de dobramento proteico

**Código sugerido:**
```python
from Bio.PDB import PDBParser

# Análise de estrutura proteica
parser = PDBParser()
structure = parser.get_structure("protein", "file.pdb")
```

### Capítulo 8: Metabolic Systems

**Tópicos essenciais:**
- Cinéticas de reação (Michaelis-Menten, Hill)
- Leis de taxa reversíveis
- Análise de fluxo metabólico (MFA)
- Análise de balanço de fluxo (FBA)
- Modos elementares
- Metabolômica (LC-MS, GC-MS)
- Integração de dados multi-ômicos

**Código sugerido:**
```python
import cobra

# Análise de balanço de fluxo
model = cobra.io.read_sbml_model("model.xml")
solution = model.optimize()
```

## 🎯 Dicas de Criação

### 1. Comece pelo Esboço

Antes de escrever LaTeX, faça um esboço em markdown:

```markdown
# Capítulo X: Título

## Seção 1: Introdução (3 slides)
- Slide 1: Motivação
- Slide 2: Objetivos
- Slide 3: Visão geral

## Seção 2: Conceito A (8 slides)
- Slide 4: Definição
- Slide 5: Propriedades
...
```

### 2. Reutilize Estruturas

Copie e adapte estruturas dos capítulos já prontos:
- Estrutura de seções do Capítulo 2
- Estilo de diagramas do Capítulo 1
- Exemplos de código do Capítulo 6

### 3. Teste Gradualmente

Compile frequentemente para verificar erros:

```bash
pdflatex capitulo03-static-networks.tex
```

### 4. Use Recursos Externos

- **Imagens**: Procure em repositórios livres (Wikimedia Commons)
- **Dados**: Use datasets públicos (KEGG, STRING, BioGRID)
- **Código**: Adapte de tutoriais do SciPy, BioPython

## 📚 Referências Úteis

### Livros Fonte

- Klipp E. et al. (2016). *Systems Biology: A Textbook*
- Alon U. (2019). *An Introduction to Systems Biology*
- Voit E.O. (2017). *A First Course in Systems Biology*

### Recursos Online

- [Systems Biology Graphical Notation (SBGN)](https://sbgn.github.io/)
- [BioPython Tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
- [NetworkX Documentation](https://networkx.org/documentation/stable/)
- [COPASI Tutorials](http://copasi.org/Support/User_Manual/)

## 🤝 Como Contribuir

1. Escolha um capítulo da lista
2. Crie o arquivo LaTeX seguindo o template
3. Desenvolva o conteúdo seguindo a estrutura recomendada
4. Teste a compilação
5. Commit com mensagem descritiva:

```bash
git add capitulos/capitulo03-static-networks.tex
git commit -m "feat: adicionar Capítulo 3 - Static Network Models

- 42 slides cobrindo teoria dos grafos e redes biológicas
- Exemplos com NetworkX
- Exercícios de análise de redes metabólicas"
```

## 📊 Progresso

Acompanhe o progresso editando este arquivo:

```markdown
- [x] Capítulo 1: Sistemas Biológicos
- [x] Capítulo 2: Modelagem Matemática
- [ ] Capítulo 3: Static Networks
- [ ] Capítulo 4: Mathematics
...
```

---

**Boa sorte na criação dos capítulos restantes!** 🎓
