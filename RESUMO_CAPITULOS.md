# Resumo Completo dos Capítulos

## Status do Projeto

**✅ PROJETO COMPLETO — 15 capítulos prontos para uso!**

Este repositório mantém **duas pipelines paralelas** para o mesmo conteúdo:

| Pipeline | Diretório | Saída | Tamanho |
|---|---|---|---|
| **Slides Beamer** | `capitulos/*.tex` | PDF por capítulo | ~50 slides/cap |
| **Livro prosa fluida** | `livro2/capitulos/cap*.tex` | `livro2/main.pdf` | 416 pp, 2.1 MB |

A conversão entre pipelines é feita por `livro2/extract.py` (Beamer → JSON)
e `livro2/build_all.py` (JSON → prosa fluida). Ver `README.md` para detalhes.

---

Total de capítulos disponíveis: **15 capítulos**

---

## Lista Completa de Capítulos

### ✅ Capítulos Existentes (Originais)

1. **Capítulo 1: Sistemas Biológicos** (48 slides)
   - Componentes biológicos fundamentais
   - Estrutura de DNA, RNA e proteínas
   - Processos metabólicos
   - Organização celular

2. **Capítulo 2: Introdução à Modelagem Matemática** (52 slides)
   - Tipos de modelos matemáticos
   - Equações diferenciais em biologia
   - Métodos numéricos
   - Análise de sensibilidade e ajuste de modelos

6. **Capítulo 6: Sistemas Gênicos** (50 slides)
   - Dogma central da biologia molecular
   - Regulação gênica
   - Tipos de RNA
   - Medição de expressão gênica
   - GenBank e bancos de dados

---

### ✨ Capítulos Novos (Recém-Criados)

3. **Capítulo 3: Static Network Models** (~50 slides)
   - Fundamentos de teoria dos grafos
   - Propriedades topológicas de redes
   - Redes biológicas (PPI, metabólicas, regulatórias)
   - Análise de controle metabólico (MCA)
   - NetworkX e análise computacional

4. **Capítulo 4: The Mathematics of Biological Systems** (~55 slides)
   - Sistemas de EDOs não-lineares
   - Análise de estabilidade e pontos de equilíbrio
   - Bifurcações (saddle-node, Hopf, pitchfork)
   - Oscilações e ciclos limite
   - Análise de sensibilidade
   - SciPy e modelagem avançada

5. **Capítulo 5: Parameter Estimation** (~54 slides)
   - Formulação do problema inverso
   - Busca em grade (grid search)
   - Métodos de gradiente (Levenberg-Marquardt, Newton-Raphson)
   - Algoritmos globais (genetic algorithms, differential evolution)
   - Análise de identificabilidade
   - Validação e critérios de ajuste (AIC, BIC)

7. **Capítulo 7: Protein Systems** (~47 slides)
   - Estrutura de proteínas detalhada
   - Cinética enzimática avançada (Hill, alosterismo)
   - Inibição enzimática (competitiva, não-competitiva)
   - Cascatas de sinalização celular
   - Modificações pós-traducionais (PTMs)
   - Proteômica e espectrometria de massas
   - BioPython para análise estrutural

8. **Capítulo 8: Metabolic Systems** (~55 slides)
   - Cinéticas de reação metabólica
   - Análise de fluxo metabólico (MFA com ¹³C)
   - Análise de balanço de fluxo (FBA)
   - Modos elementares e vias extremas
   - Metabolômica (LC-MS, GC-MS)
   - COBRApy e modelos genome-scale

9. **Capítulo 9: Signaling Systems** (~42 slides)
   - Receptores (GPCRs, RTKs, ion channels)
   - Redes de transdução (MAPK, PI3K/Akt, JAK-STAT)
   - Cascatas de proteínas quinases
   - Ultrasensibilidade (Goldbeter-Koshland)
   - Segundos mensageiros (cAMP, Ca²⁺, IP3/DAG)
   - Dinâmica e propriedades emergentes

10. **Capítulo 10: Population Systems** (~40 slides)
    - Modelos de crescimento populacional (exponencial, logístico, Allee)
    - Interações entre espécies (Lotka-Volterra, competição, mutualismo)
    - Modelos epidemiológicos (SIR, SEIR, R₀)
    - Dinâmica espacial e metapopulações
    - Reação-difusão e padrões de Turing

11. **Capítulo 11: Integrated Analysis** (~49 slides)
    - Integração multi-ômica (genomics, transcriptomics, proteomics, metabolomics)
    - Caso de estudo: Ciclo da trealose em levedura
    - Análise de vias e redes integradas
    - Modelagem de sistemas integrados
    - Constraint-based modeling com dados de expressão

12. **Capítulo 12: Physiological Systems - Heart** (~42 slides)
    - Anatomia e fisiologia cardíaca
    - Eletrofisiologia do cardiomiócito
    - Modelos de células cardíacas (Noble, Luo-Rudy, ten Tusscher)
    - Acoplamento excitação-contração
    - Propagação e arritmias
    - Teoria do cabo e ondas espirais

13. **Capítulo 13: Systems Biology in Medicine** (~55 slides)
    - Descoberta e desenvolvimento de fármacos
    - Farmacocinética/farmacodinâmica (PK/PD)
    - Doenças complexas (câncer, diabetes, neurodegeneração)
    - Medicina personalizada e farmacogenômica
    - Aplicações clínicas (HER2+, imunoterapia, CAR-T)

14. **Capítulo 14: Design of Biological Systems** (~59 slides)
    - Circuitos genéticos sintéticos (toggle switch, repressilator)
    - Engenharia metabólica
    - Ferramentas de design (CAD, SBOL)
    - Algoritmo de Gillespie
    - Células mínimas e biologia sintética
    - OptKnock e otimização de vias

15. **Capítulo 15: Emerging Topics** (~33 slides)
    - Modelagem multi-escala
    - Biologia de sistemas de célula única (scRNA-seq, spatial transcriptomics)
    - Inteligência artificial e deep learning
    - Doenças complexas e envelhecimento
    - Direções futuras (digital twins, quantum computing, IA)

---

## Estatísticas do Projeto

### Slides por Capítulo
- **Total estimado**: ~750+ slides
- **Média por capítulo**: ~50 slides
- **Menor capítulo**: Cap. 15 (33 slides)
- **Maior capítulo**: Cap. 14 (59 slides)

### Características Técnicas

#### 📊 Diagramas TikZ
- Mais de **150 diagramas** personalizados
- Redes biológicas, grafos, circuitos genéticos
- Retratos de fase, diagramas de bifurcação
- Estruturas moleculares, vias metabólicas
- Diagramas de sinalização celular

#### 🐍 Código Python
- Mais de **100 exemplos de código**
- Bibliotecas: NumPy, SciPy, Matplotlib, NetworkX, BioPython, COBRApy, scanpy, PyTorch
- Simulações de EDOs, otimização, análise de redes
- Análise de dados ômicos
- Machine learning e deep learning

#### 📐 Equações Matemáticas
- Centenas de equações formatadas em LaTeX
- EDOs, sistemas dinâmicos, bifurcações
- Cinética enzimática, farmacocinética
- Teoria dos grafos, análise de redes
- Machine learning e otimização

#### 🎨 Elementos Visuais
- Blocos coloridos: `\definicao`, `\exemplo`, `\importante`, `\destaque`
- Cores do template: azulescuro, azulclaro, verdeacido, laranjacel, roxodna
- Tabelas formatadas com booktabs
- Listas estruturadas e enumerações

---

## Como Compilar

### Compilar um capítulo individual:
```bash
cd /home/lemke/bbs/capitulos
pdflatex capitulo03-static-networks.tex
pdflatex capitulo03-static-networks.tex  # Segunda vez para referências
```

### Compilar todos os capítulos:
```bash
cd /home/lemke/bbs
bash compile_all.sh
```

### Usando latexmk (recomendado):
```bash
cd /home/lemke/bbs/capitulos
latexmk -pdf capitulo03-static-networks.tex
```

---

## Conteúdo por Seção

### 🧬 Fundamentos (Capítulos 1-2)
- Sistemas biológicos básicos
- Modelagem matemática introdutória

### 📊 Métodos Matemáticos (Capítulos 3-5)
- Teoria dos grafos e redes
- Matemática avançada de sistemas dinâmicos
- Estimação de parâmetros

### 🔬 Sistemas Moleculares (Capítulos 6-9)
- Sistemas gênicos
- Sistemas proteicos
- Metabolismo
- Sinalização celular

### 🌍 Sistemas Populacionais e Integrados (Capítulos 10-12)
- Dinâmica populacional e epidemiologia
- Análise integrada multi-ômica
- Fisiologia cardíaca

### 🏥 Aplicações e Futuro (Capítulos 13-15)
- Medicina de sistemas
- Biologia sintética
- Tópicos emergentes e IA

---

## Referências Principais

### Livros Citados
- Klipp E. et al. - *Systems Biology: A Textbook*
- Alon U. - *An Introduction to Systems Biology*
- Palsson B.O. - *Systems Biology: Constraint-based Reconstruction and Analysis*
- Murray J.D. - *Mathematical Biology*
- Strogatz S.H. - *Nonlinear Dynamics and Chaos*
- Berg J.M. et al. - *Biochemistry*
- Keener J. & Sneyd J. - *Mathematical Physiology*

### Ferramentas Computacionais
- Python: NumPy, SciPy, Matplotlib
- NetworkX: análise de redes
- BioPython: bioinformática
- COBRApy: modelos metabólicos
- scanpy: single-cell analysis
- PyTorch/TensorFlow: deep learning

### Bancos de Dados
- PDB, UniProt, KEGG, Reactome
- STRING, BioGRID, IntAct
- TCGA, UK Biobank, DrugBank
- GenBank, RefSeq, Ensembl

---

## Características Pedagógicas

### ✅ Cada capítulo inclui:
1. **Slide de título** com informações completas
2. **Sumário** (table of contents)
3. **Introdução** com objetivos de aprendizagem
4. **Conteúdo principal** dividido em seções lógicas
5. **Exemplos práticos** com código Python
6. **Diagramas explicativos** em TikZ
7. **Exercícios** (2-5 slides)
8. **Referências** bibliográficas
9. **Slide final** de agradecimento

### 🎯 Público-Alvo
- Graduação em Bioinformática
- Pós-graduação em Biologia de Sistemas
- Disciplinas de Modelagem Matemática aplicada à Biologia
- Cursos de Biologia Computacional

---

## Próximos Passos Sugeridos

1. **Compilar todos os PDFs** usando o script `compile_all.sh`
2. **Revisar os slides** para verificar formatação
3. **Testar os códigos Python** para garantir que funcionam
4. **Adicionar figuras externas** se disponíveis (opcional)
5. **Customizar** informações do autor/instituição em cada capítulo
6. **Criar PDFs combinados** se desejar (usando `pdfunite` ou similar)

---

## Customização

Para personalizar as apresentações, edite:

1. **Autor e Instituição** (em cada capítulo):
```latex
\author{Seu Nome}
\institute{Sua Instituição}
\date{\today}
```

2. **Cores do tema** (no template):
```latex
\definecolor{azulescuro}{RGB}{0, 51, 102}
\definecolor{azulclaro}{RGB}{51, 153, 255}
```

3. **Logo da instituição** (opcional):
```latex
\logo{\includegraphics[height=1cm]{logo.png}}
```

---

## Licença e Uso

Este material foi desenvolvido para fins educacionais. Ao usar:
- Cite adequadamente
- Mantenha os créditos aos autores originais das referências
- Compartilhe com a comunidade acadêmica

---

## Contato e Contribuições

Para dúvidas, sugestões ou melhorias:
- Abra um issue no repositório
- Contribua com novos exemplos ou correções
- Compartilhe feedback sobre o uso em sala de aula

---

**Última atualização**: 2026-07-16 (atualizado para refletir pipeline livro2/)

**Status**: ✅ PROJETO COMPLETO - 15 capítulos prontos, dupla pipeline (slides + livro)!
