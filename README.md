# Apresentações em Beamer: Bioinformática para Biologia de Sistemas

Coleção completa de apresentações em LaTeX/Beamer baseadas no livro "Systems Biológicos e Modelagem Matemática".

## 📚 Estrutura do Repositório

```
apresentacoes-bioinformatica/
├── template/
│   └── beamer-template.tex       # Template base reutilizável
├── capitulos/
│   ├── capitulo01-sistemas-biologicos.tex
│   ├── capitulo02-modelagem-matematica.tex
│   ├── capitulo06-sistemas-genicos.tex
│   └── ... (outros capítulos)
├── figuras/                      # Diretório para imagens
├── codigos/                      # Scripts de exemplo
└── README.md
```

## 🎯 Capítulos Disponíveis

### ✅ Completos

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

3. **Capítulo 6: Sistemas Gênicos** (50 slides)
   - Dogma central da biologia molecular
   - Regulação gênica
   - Tipos de RNA
   - Medição de expressão gênica
   - GenBank e bancos de dados

### 🔄 Em Desenvolvimento

- Capítulos 3-5, 7-15 (use o template fornecido)

## 🚀 Como Usar

### Pré-requisitos

Você precisa ter instalado:
- **TeX Live** (Linux) ou **MiKTeX** (Windows) ou **MacTeX** (macOS)
- Pacotes LaTeX necessários (geralmente incluídos nas distribuições completas):
  - `beamer`
  - `tikz`
  - `listings`
  - `babel` (com suporte a português)

### Instalação no Linux

```bash
# Ubuntu/Debian
sudo apt-get install texlive-full

# Fedora
sudo dnf install texlive-scheme-full

# Arch Linux
sudo pacman -S texlive-most
```

### Compilação

#### Compilar um capítulo específico

```bash
cd apresentacoes-bioinformatica/capitulos
pdflatex capitulo01-sistemas-biologicos.tex

# Para referências completas, compile 2x
pdflatex capitulo01-sistemas-biologicos.tex
pdflatex capitulo01-sistemas-biologicos.tex
```

#### Usando latexmk (recomendado)

```bash
# Compila automaticamente quantas vezes necessário
latexmk -pdf capitulo01-sistemas-biologicos.tex

# Modo watch (recompila ao salvar)
latexmk -pdf -pvc capitulo01-sistemas-biologicos.tex
```

#### Script de compilação em lote

```bash
#!/bin/bash
# compile_all.sh

cd capitulos
for file in capitulo*.tex; do
    echo "Compilando $file..."
    pdflatex -interaction=nonstopmode "$file"
    pdflatex -interaction=nonstopmode "$file"
done

echo "Limpando arquivos auxiliares..."
rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb

echo "Concluído! PDFs gerados:"
ls -lh *.pdf
```

## 🎨 Personalização

### Modificar Cores do Tema

Edite o arquivo `template/beamer-template.tex`:

```latex
% Definir suas próprias cores
\definecolor{azulescuro}{RGB}{0, 51, 102}      % Cor principal
\definecolor{azulclaro}{RGB}{51, 153, 255}     % Cor secundária
\definecolor{verdeacido}{RGB}{102, 204, 0}     % Destaques
```

### Alterar Informações do Autor

Em cada capítulo, modifique:

```latex
\title[Título Curto]{Título Completo}
\author{Seu Nome}
\institute{Sua Instituição}
\date{\today}  % ou data específica
```

### Adicionar Logo da Instituição

No template ou em cada capítulo:

```latex
\logo{\includegraphics[height=1cm]{logo-instituicao.png}}
```

## 📝 Criando Novos Capítulos

### 1. Copie o Template

```bash
cp template/beamer-template.tex capitulos/capitulo03-novo-capitulo.tex
```

### 2. Estrutura Básica

```latex
\input{../template/beamer-template.tex}

\title[Cap. 3: Título]{Capítulo 3: Título Completo}
\author{Seu Nome}
\institute{Sua Instituição}
\date{\today}

\begin{document}

\begin{frame}
\titlepage
\end{frame}

\begin{frame}{Sumário}
\tableofcontents
\end{frame}

\section{Primeira Seção}

\begin{frame}{Título do Slide}
Conteúdo aqui...
\end{frame}

\end{document}
```

## 🛠️ Comandos Personalizados Disponíveis

### Blocos Especiais

```latex
% Definição
\definicao{Título}{Conteúdo da definição}

% Exemplo
\exemplo{Título}{Conteúdo do exemplo}

% Destaque importante
\importante{Texto importante}

% Equação em destaque
\destaque{$E = mc^2$}
```

### Notação Matemática

```latex
\derivada{f}{x}              % df/dx
\parcial{f}{x}               % ∂f/∂x
\vect{v}                     % vetor em negrito

% Comandos para genes e proteínas
\gene{lacZ}                  % gene em itálico
\proteina{LacZ}              % proteína em small caps
\especie{E. coli}            % espécie em itálico
```

### Diagramas TikZ

```latex
\begin{tikzpicture}
\node[draw, circle, fill=azulclaro!30] at (0,0) {Nó};
\node[draw, rectangle, fill=verdeacido!30] at (3,0) {Retângulo};
\draw[->, thick] (0.5,0) -- (2.5,0);
\end{tikzpicture}
```

### Código Python

```latex
\begin{lstlisting}[language=Python, caption=Exemplo]
import numpy as np

def funcao(x):
    return x**2

resultado = funcao(10)
print(resultado)
\end{lstlisting}
```

## 📊 Elementos Visuais Incluídos

### Tipos de Blocos

- `\begin{block}` - Bloco padrão (azul)
- `\begin{alertblock}` - Alerta/atenção (vermelho)
- `\begin{exampleblock}` - Exemplo (verde)

### Listas e Enumerações

```latex
% Lista não-ordenada
\begin{itemize}
    \item Primeiro item
    \item Segundo item
\end{itemize}

% Lista ordenada
\begin{enumerate}
    \item Primeiro
    \item Segundo
\end{enumerate}
```

### Tabelas

```latex
\begin{tabular}{lcc}
\toprule
\textbf{Header 1} & \textbf{Header 2} & \textbf{Header 3} \\
\midrule
Dado 1 & Dado 2 & Dado 3 \\
Dado 4 & Dado 5 & Dado 6 \\
\bottomrule
\end{tabular}
```

## 🐍 Exemplos de Código Incluídos

Todos os capítulos incluem exemplos práticos em Python:

- **Capítulo 1**: Simulação de cinética enzimática (Michaelis-Menten)
- **Capítulo 2**: Resolução de EDOs, modelos populacionais, ajuste de parâmetros
- **Capítulo 6**: BioPython para GenBank, análise de RNA-seq, busca de ORFs

## 📚 Referências e Recursos

### Documentação LaTeX/Beamer

- [Beamer User Guide](https://tug.ctan.org/macros/latex/contrib/beamer/doc/beameruserguide.pdf)
- [TikZ & PGF Manual](https://tikz.dev/)
- [LaTeX Wikibook](https://en.wikibooks.org/wiki/LaTeX)

### Recursos de Bioinformática

- [BioPython Tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
- [NCBI Education](https://www.ncbi.nlm.nih.gov/guide/)
- [EBI Training](https://www.ebi.ac.uk/training)

## 🤝 Contribuindo

Para adicionar novos capítulos ou melhorar os existentes:

1. Use o template fornecido
2. Mantenha a estrutura consistente
3. Inclua exemplos práticos
4. Adicione exercícios ao final
5. Documente referências

## 📄 Licença

Este material é disponibilizado para fins educacionais. Cite adequadamente ao usar.

## ✉️ Contato

Para dúvidas ou sugestões sobre as apresentações, entre em contato através do repositório.

---

## 🔧 Troubleshooting

### Problema: "Package babel Error"

```bash
# Instale o suporte para português
sudo apt-get install texlive-lang-portuguese
```

### Problema: "Package tikz Error"

```bash
# Instale pacotes gráficos
sudo apt-get install texlive-pictures
```

### Problema: Fontes não encontradas

```bash
# Atualize o banco de dados de fontes
sudo texhash
sudo updmap-sys
```

### Problema: Compilação lenta

Use `pdflatex` com opções de otimização:

```bash
pdflatex -interaction=nonstopmode -halt-on-error arquivo.tex
```

## 📈 Status do Projeto

- ✅ Template base criado
- ✅ 3 capítulos completos (1, 2, 6)
- 🔄 12 capítulos restantes
- 📊 ~150 slides por capítulo (média)
- 🎯 Total estimado: ~750 slides quando completo

## 🎓 Uso Educacional

Estas apresentações foram desenvolvidas para:

- Cursos de graduação em Bioinformática
- Pós-graduação em Biologia de Sistemas
- Disciplinas de Modelagem Matemática aplicada à Biologia
- Workshops e seminários

---

**Última atualização**: 2026-01-01
