# Bioinformática para Biologia de Sistemas

Material didático em LaTeX cobrindo Bioinformática, Biologia de Sistemas e
Modelagem Matemática. O repositório contém **duas pipelines paralelas**:

1. **Slides Beamer** (`capitulos/*.tex`) — apresentação modular por capítulo
2. **Livro completo** (`livro2/`) — texto em prosa fluida com figuras TikZ e listagens Python

---

## 📚 Estrutura do Repositório

```
bbs/
├── README.md                          # Este arquivo
├── RESUMO_CAPITULOS.md                # Lista dos 15 capítulos com sumário
├── VEREDITO_FINAL.md                  # Histórico de decisões editoriais
├── AGENTS.md                          # Guia para WARP/agentes de IA
│
├── capitulos/                         # 📽️ Slides Beamer (pipeline 1)
│   ├── capitulo01-sistemas-biologicos.tex
│   ├── capitulo02-modelagem-matematica.tex
│   ├── capitulo03-static-networks.tex
│   ├── capitulo04-mathematics.tex
│   ├── ...                            # 15 capítulos no total
│   └── capitulo15-emerging-topics.tex
│
├── livro2/                            # 📘 Livro completo (pipeline 2)
│   ├── main.tex                       # Arquivo mestre (compile a partir daqui)
│   ├── prefacio.tex                   # Prefácio do livro
│   ├── capitulos/                     # 15 capítulos em prosa fluida
│   │   ├── cap01.tex
│   │   ├── cap02.tex
│   │   └── ... cap15.tex
│   ├── extracted/                     # JSONs intermediários (gerado)
│   ├── images/                        # Imagens e TikZ
│   ├── extract.py                     # Beamer → JSON
│   ├── prose_writer.py                # JSON → prosa fluida
│   ├── build_all.py                   # Construtor centralizado
│   ├── compile.py                     # 3-pass compile driver
│   ├── gerar_capitulos.py             # Alternativa ao build_all.py
│   └── fix_orphan_dollars.py          # Limpa $$ órfãos do extractor
│
├── codigos/                           # 🐍 Notebooks e scripts Python
│   ├── capitulo02_exemplos.ipynb
│   ├── capitulo03-exemplos.ipynb
│   ├── capitulo04-mathematics.ipynb
│   ├── generate_notebook.py           # Script que gera cap04
│   └── ...                            # Notebooks cap 05-06
│
├── template/                          # Templates Beamer e TikZ
├── images/                            # Imagens globais
├── graphs/                            # Outputs de graphify-out (não versionado)
│
├── Dockerfile.warp-env                # Ambiente isolado Docker
├── compile_all.sh                     # Script batch para slides
├── injeta_atividade.py                # Injeta atividades no Classroom
├── injeta_classroom.py                # Classroom API helper
├── credentials.json                   # ⚠️ Não versionado (gitignored)
└── token.json                         # ⚠️ Não versionado (gitignored)
```

---

## 🎯 Capítulos Disponíveis (15 total)

| # | Título | Tópico |
|---|---|---|
| 01 | Sistemas Biológicos | Dogma central, hierarquia celular |
| 02 | Modelagem Matemática | EDOs, estabilidade, métodos numéricos |
| 03 | Redes Estáticas | Grafos, clustering, scale-free, motifs |
| 04 | Matemática de Sistemas | EDOs não-lineares, bifurcações, oscilações |
| 05 | Estimação de Parâmetros | OLS, gradiente, GA, identificabilidade |
| 06 | Sistemas Gênicos | Regulação transcricional, RNA-seq |
| 07 | Sistemas de Proteínas | Cinética, alostério, fosforilação, proteômica |
| 08 | Sistemas Metabólicos | FBA, GEMs, metabolômica |
| 09 | Sinalização Celular | Cascatas MAPK, PI3K, oscilações Ca²⁺ |
| 10 | Sistemas Populacionais | LV, SIR, Turing, metapopulações |
| 11 | Análise Multi-Ômica | Correlação, enriquecimento, modelos híbridos |
| 12 | Fisiologia Cardíaca | Modelo cardíaco, arritmias, EC-coupling |
| 13 | Medicina | Network pharmacology, digital twins, precisão |
| 14 | Biologia Sintética | Biobricks, circuitos, xenobiologia |
| 15 | Tópicos Emergentes | IA, células CAR-T, vacinas de design |

Para sumário detalhado de cada capítulo, consulte [RESUMO_CAPITULOS.md](RESUMO_CAPITULOS.md).

---

## 🚀 Como Usar

### Pré-requisitos

- **TeX Live** (Linux) ou **MiKTeX** (Windows) ou **MacTeX** (macOS)
- Pacotes LaTeX: `beamer`, `tikz`, `listings`, `babel` (com suporte a português)
- **Python 3.8+** com `numpy`, `scipy`, `matplotlib`, `sympy`, `networkx`

#### Linux

```bash
sudo apt-get install texlive-full texlive-lang-portuguese
pip install numpy scipy matplotlib sympy networkx biopython
```

#### macOS (testado 2026-07)

```bash
brew install --cask mactex
pip install numpy scipy matplotlib sympy networkx biopython
```

### Compilação

#### Pipeline 1: Slides Beamer

```bash
# Capítulo único (2 passadas para cross-refs)
cd capitulos
pdflatex -interaction=nonstopmode -halt-on-error capitulo01-sistemas-biologicos.tex
pdflatex -interaction=nonstopmode -halt-on-error capitulo01-sistemas-biologicos.tex

# Watch mode (auto-recompila ao salvar)
latexmk -pdf -pvc capitulos/capitulo01-sistemas-biologicos.tex

# Batch (todos os 15 capítulos)
./compile_all.sh
```

#### Pipeline 2: Livro completo

```bash
# Workflow padrão: extrair Beamer → escrever prosa → compilar livro
python3 livro2/extract.py                          # Beamer → JSON (15 caps)
python3 livro2/build_all.py                        # JSON → prosa fluida (15 .tex)
python3 livro2/compile.py                         # 3-pass pdflatex → main.pdf

# Output: livro2/main.pdf (~416 páginas)
```

O pipeline 2 é **portável** — todos os scripts usam `Path(__file__).resolve()`
em vez de caminhos absolutos, funcionando em WSL/macOS/Linux/CI.

#### Notebooks Jupyter

```bash
# Gera cap04-exemplos.ipynb (corrigido em 2026-07-16, ver dbf2c9a)
python3 codigos/generate_notebook.py

# Notebooks existentes podem ser executados diretamente
jupyter notebook codigos/
```

---

## 🎨 Personalização

### Modificar Cores do Tema

Edite o arquivo de cores no template:

```latex
\definecolor{azulescuro}{RGB}{0, 51, 102}      % Cor principal
\definecolor{azulclaro}{RGB}{51, 153, 255}     % Cor secundária
\definecolor{verdeacido}{RGB}{102, 204, 0}     % Destaques
\definecolor{verdebio}{RGB}{0, 128, 64}        % Biologia
\definecolor{laranjacel}{RGB}{255, 153, 51}    % Otimização
\definecolor{roxodna}{RGB}{153, 51, 255}       % Genômica
\definecolor{cinzafundo}{RGB}{248, 248, 248}   % Fundo
```

### Comandos Personalizados Disponíveis

```latex
% Matemática
\derivada{f}{x}              % df/dx
\parcial{f}{x}               % ∂f/∂x
\vect{v}                     % vetor em negrito

% Genética
\gene{lacZ}                  % gene em itálico
\proteina{LacZ}              % proteína em small caps
\especie{E. coli}            % espécie em itálico

% Blocos pedagógicos
\begin{definicaoenv}[título]  ... \end{definicaoenv}
\begin{exemploenumv}[título] ... \end{exemploenumv}
```

### Diagramas TikZ

Diagramas seguem o padrão **0.08 gap, 1pt line width** com cores do tema.
Veja exemplos em `livro2/capitulos/cap02.tex` (Figuras 2.1 a 2.5).

---

## 🛠️ Boas Práticas

### Antes de Editar um Capítulo Grande

```bash
# Backup automático antes de edições pesadas
cp capitulos/capituloXX.tex capitulos/capituloXX.tex.auto.beforeMinhaMudanca
```

(Todos os `*.tex.auto.before*` estão no `.gitignore` e não serão commitados.)

### Workflow para Corrigir `$$` Órfãos

Se aparecerem placeholders `$$` órfãos no livro2 (vindos do extractor JSON),
use:

```bash
python3 livro2/fix_orphan_dollars.py capitulos/capXX.tex
```

Atualmente o script cobre 7 padrões para o cap02. Para outros capítulos,
adicione novos pares `(regex, replacement)` em `livro2/fix_orphan_dollars.py`.

### Validação de Build

```bash
# Limpar todos os arquivos auxiliares antes de build limpo
rm -f livro2/main.aux livro2/main.log livro2/main.toc livro2/main.out
rm -f livro2/capitulos/*.aux livro2/capitulos/*.log livro2/capitulos/*.toc

# Reconstruir
python3 livro2/compile.py
```

---

## 🐍 Exemplos de Código Incluídos

Todos os capítulos incluem exemplos práticos em Python:

- **Cap 1**: Cinética enzimática (Michaelis-Menten)
- **Cap 2**: Resolução de EDOs, modelos SIR, ajuste de parâmetros
- **Cap 3**: NetworkX para análise de redes biológicas
- **Cap 4**: SymPy para Jacobianos analíticos, SciPy para autovalores
- **Cap 5**: Grid search, Levenberg-Marquardt, GA, análise de Fisher
- **Cap 6**: BioPython para GenBank, análise de RNA-seq
- **Cap 7**: PyMOL para visualização de estruturas
- **Cap 8**: COBRApy para FBA, análise de fluxos
- **Cap 11**: Clustering, enriquecimento GO, FBA integrado
- **Cap 13**: PK/PD, machine learning para medicina personalizada

---

## 📚 Referências e Recursos

### LaTeX/Beamer/TikZ

- [Beamer User Guide](https://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf)
- [TikZ & PGF Manual](https://tikz.dev/)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)

### Bioinformática

- [BioPython Tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
- [NCBI Education](https://www.ncbi.nlm.nih.gov/guide/)
- [EBI Training](https://www.ebi.ac.uk/training)

### Referências Bibliográficas Citadas no Livro

Livros-texto clássicos:
- Alon, U. (2019). *An Introduction to Systems Biology*
- Barabási, A. (2016). *Network Science* (CC-BY, networksciencebook.com)
- Klipp, E. et al. (2016). *Systems Biology: A Textbook*
- Newman, M. (2018). *Networks* (2ª ed)
- Murray, J. (2002). *Mathematical Biology*
- Strogatz, S. (2015). *Nonlinear Dynamics and Chaos*

---

## 🤝 Contribuindo

1. Use o template e mantenha consistência visual
2. Inclua exemplos práticos em Python (executáveis)
3. Adicione diagramas TikZ com cores do tema
4. Inclua exercícios (2-5 slides/capítulo)
5. Documente referências no padrão `\bibitem{YYYY}`
6. Valide compilação ANTES de submeter:
   ```bash
   pdflatex -interaction=nonstopmode -halt-on-error capitulos/capituloXX.tex
   ```

---

## 🐛 Troubleshooting

### "Package babel Error"

```bash
sudo apt-get install texlive-lang-portuguese
```

### "Package tikz Error"

```bash
sudo apt-get install texlive-pictures
```

### Caracteres Acentuados em Math Mode Disparam Warnings

**Causa**: `\mathrm{transcrição}` em math mode gera `Command \c invalid`.
**Correção**: usar `\text{transcrição}` que aceita acentuação. Veja commit `7108423`.

### `$$` Órfãos do Extractor

**Sintoma**: `! Display math should end with $$` ou `Missing $ inserted`.
**Causa**: O extractor substitui macros Beamer por `$$` em vez de preservar.
**Correção**: substituir manualmente ou usar `livro2/fix_orphan_dollars.py`.

### Fontes não Encontradas

```bash
sudo texhash
sudo updmap-sys
```

### Compilação Lenta

```bash
pdflatex -interaction=nonstopmode -halt-on-error arquivo.tex
```

---

## 📈 Status do Projeto

| Pipeline | Status | Tamanho | Última atualização |
|---|---|---|---|
| 📽️ Slides Beamer | ✅ 15 capítulos completos | ~50 slides/cap | 2026-01-02 |
| 📘 Livro prosa completa | ✅ 15 capítulos convertidos | 416 pp, 2.1 MB | 2026-07-16 |
| 🐍 Notebooks Python | ✅ 7 notebooks | 5 MB | 2026-07-16 |

### Última Sessão de Desenvolvimento (2026-07-08 a 2026-07-16)

- **Enriquecimento cap02**: +3 seções, Figura 2.2 (convergência contínuo/discreta), labels corrigidos em Figuras 2.5
- **Pipeline 2 portabilizado**: scripts `extract.py`, `compile.py`, `build_all.py`, `gerar_capitulos.py` agora funcionam em qualquer plataforma
- **Sintaxe Python corrigida**: `generate_notebook.py:228` (string sem aspas)
- **Casa aos `$$` órfãos**: 8+ correções manuais em cap01, cap02, cap09
- **Arquitetura finalizada**: `livro2/main.pdf` e `*.tex.auto.before*` saíram do versionamento (3.7 MB liberados)

Para detalhes de cada commit, ver `git log --oneline -10`.

---

## 🎓 Uso Educacional

Material desenvolvido para:

- Cursos de graduação em Bioinformática
- Pós-graduação em Biologia de Sistemas
- Disciplinas de Modelagem Matemática aplicada à Biologia
- Workshops e seminários

---

## 📄 Licença

Este material é disponibilizado para fins educacionais. Cite adequadamente ao usar.

---

**Última atualização**: 2026-07-16 (após enriquecimento do cap02 + pipeline 2)
