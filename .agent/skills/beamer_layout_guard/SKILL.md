---
name: Beamer Layout Guard
description: Especialista em detectar e corrigir slides Beamer onde o texto é interrompido ou ultrapassa os limites da página (Overfull frames).
---

# Beamer Layout Guard 🛡️

Esta skill foi projetada para garantir que seus slides Beamer nunca tenham texto cortado ou interrompido. Ela analisa tanto o código fonte LaTeX quanto os arquivos de log gerados pela compilação.

## 1. O que ela detecta?

- **Texto Cortado Verticalmente (`Overfull \vbox`):** Quando há mais conteúdo do que cabe no slide.
- **Texto Ultrapassando as Margens (`Overfull \hbox`):** Quando uma linha ou imagem é muito larga.
- **Densidade Excessiva:** Slides com muitos parágrafos ou itens que prejudicam a legibilidade.
- **Erros de Estrutura:** Ambientes (`itemize`, `block`, `frame`) não fechados corretamente.

## 2. Ferramentas de Análise

Execute o script de guarda para obter um relatório detalhado:

```bash
python3 .agent/skills/beamer_layout_guard/scripts/beamer_guard.py <arquivo.tex>
```

## 3. Estratégias de Correção

Quando um slide for identificado como problemático, aplique estas soluções:

### A. Divisão Automática de Slides
Adicione a opção `[allowframebreaks]` ao ambiente de frame. Isso faz com que o LaTeX divida o conteúdo automaticamente se ele ultrapassar o limite.

```latex
\begin{frame}[allowframebreaks]{Título Longo}
... conteúdo extenso ...
\end{frame}
```

### B. Divisão Manual (Recomendado para melhor controle)
Divida o conteúdo em dois slides distintos, usando `(1/2)` e `(2/2)` no título.

### C. Ajuste de Tamanho de Fonte
Use o ambiente `shrink` se o excesso for pequeno:

```latex
\begin{frame}[shrink=5]{Título}
... conteúdo levemente maior ...
\end{frame}
```

### D. Uso de Colunas
Se o vertical estiver cheio mas houver espaço horizontal:

```latex
\begin{columns}
    \column{0.5\textwidth}
    ...
    \column{0.5\textwidth}
    ...
\end{columns}
```

## 4. Fluxo de Trabalho

1. **Compile o documento:** `pdflatex seu_arquivo.tex`
2. **Execute a análise:** use o script `beamer_guard.py`.
3. **Corrija:** aplique uma das estratégias acima nos slides listados.
4. **Re-compile e verifique.**
