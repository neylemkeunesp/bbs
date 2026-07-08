# Ranking dos 15 capítulos BBS — Revisão §VI (Rubric LOOPS.md)

**Data:** 2026-07-01
**Contrato:** `contract.md` v0.1 + pilotagem 3 caps (1, 4, 15)
**Pesos §VI:** D=0.20 · O=0.20 · C=0.30 · F=0.30
**Ordem da tabela:** score §VI **ascendente** (rank 1 = prioridade máxima de retrabalho).

---

## Tabela completa

| Rank | Cap | Nome | Tipo | Score §VI | Eixos (D / O / C / F) | Gargalo §IX | Patch #1 |
|:---:|:---:|---|---|:---:|:---:|:---|:---|
| 1 | 9 | Signaling Systems | base | **0.61** | 0.50 / 0.40 / 0.70 / 0.70 | Originality + Design | Escrever 1 analogia-âncora (cascade MAPK = amplificadores em série) |
| 2 | 11 | Integrated Analysis | prospectivo | **0.65** | 0.70 / 0.50 / 0.75 / 0.70 | Originality (sem declaração profundidade/survey) | Adicionar slide "neste cap: Multi-Ômica + Trealose (fundo); Redes (survey)" |
| 3 | 13 | Systems Medicine | prospectivo | **0.65** | 0.65 / 0.55 / 0.70 / 0.70 | Originality (survey puro: 2 lstlistings / 55 frames) | Marcar slide-inicial: "Medicina Personalizada + Ensaios (fundo); Demais (survey)" |
| 4 | 12 | Heart Physiology | prospectivo | **0.66** | 0.65 / 0.55 / 0.75 / 0.75 | Originality (8 seções sem declaração) | Slide "neste cap: Eletrofisiologia + Acoplamento (fundo); Anatomia + Propagação (survey)" |
| 5 | 8 | Metabolic Systems | base | **0.67** | 0.60 / 0.50 / 0.75 / 0.70 | Functionality (3 Q / 56 frames) + Originality | Adicionar ≥5 questões práticas cobrindo FBA + regulação alostérica |
| 6 | 6 | Sistemas Gênicos | base | **0.67** | 0.60 / 0.50 / 0.70 / 0.85 | Originality (zero analogia-âncora — viola §2.3) | Inserir analogia-âncora (regulação gênica = switches elétricos) |
| 7 | 10 | Population Systems | base | **0.68** | 0.60 / 0.55 / 0.70 / 0.80 | Design (34 shrinks) + Originality (fronteira técnica) | Quebrar lstlistings em ≤2 por slide + atribuição Lotka-Volterra 1925 |
| 8 | 7 | Protein Systems | base | **0.69** | 0.50 / 0.50 / 0.80 / 0.85 | Design (66% dos frames com shrink) | Reduzir 46 shrinks para ≤15 (cortar conteúdo redundante) |
| 9 | 14 | Design Systems | prospectivo | **0.72** | 0.65 / 0.60 / 0.80 / 0.80 | Originality (sem declaração) + Design (41 shrinks) | Slide de abertura: "Circuitos sintéticos + Biocomputação (fundo); Demais (survey)" |
| 10 | 1 | Sistemas Biológicos | base | **0.74** | 0.70 / 0.60 / 0.70 / 0.90 | Originality (zero analogia-âncora; TikZ comentado nas linhas 689–700) | Inserir analogia-âncora na Introdução (10–30 palavras) |
| 11 | 3 | Static Networks | técnico | **0.76** | 0.50 / 0.85 / 0.65 / 0.85 | Craft (57 shrinks + 10/11 lstlistings sem caption) | Adicionar "caption=…" + frase "O que este código faz" a cada lstlisting |
| 12 | 2 | Modelagem Matemática | técnico | **0.77** | 0.60 / 0.85 / 0.75 / 0.85 | Design (21 shrinks) + Functionality (sem recap) | Substituir "\Huge Obrigado!" por recapitulação com 5 bullets-síntese |
| 13 | 15 | Emerging Topics | prospectivo | **0.78** | 0.70 / 0.70 / 0.80 / 0.85 | Design (100% TikZ cria monocromia + 31 shrinks) | Substituir ≥3 TikZ por `\includegraphics` (curvas Cryo-EM, redes ML) |
| 14 | 4 | Mathematics | técnico | **0.84** | 0.80 / 0.80 / 0.90 / 0.90 | Design (sem resumos intermediários) | Inserir 2–3 slides-síntese entre as 4 seções principais |
| 15 | 5 | Parameter Estimation | técnico | **0.87** | 0.80 / 0.90 / 0.90 / 0.90 | Functionality (sem recap final; único defeito real) | Adicionar slide de recapitulação com 5 bullets + 1 mapa dos 4 métodos |

---

## Estatísticas agregadas (n=15)

| Métrica | Valor |
|---|:---:|
| **Média geral** | 0.717 |
| **Mediana** | 0.69 |
| **Desvio padrão** | 0.075 |
| **Mínimo** | 0.61 (Cap 9) |
| **Máximo** | 0.87 (Cap 5) |
| **Faixa** | 0.26 (rubric §VI discrimina bem) |

### Média por tipo (validação da régua §2.3)

| Tipo | n | Média | Comentário |
|---|:---:|:---:|:---|
| **Técnico** | 4 | **0.810** | Tipo mais alto — base pedagógica + lstlistings densos + atribuições históricas cumpridas |
| **Prospectivo** | 5 | **0.692** | Média próxima dos base; Cap 13 puxa pra baixo por survey puro |
| **Base** | 6 | **0.677** | Menor média; Originality penalizada por 4 caps sem analogia-âncora |

### Distribuição por faixas de score

| Faixa | Caps | Conta |
|---|---|:---:|
| **Crítica** (<0.65) | 9, 11, 13 | 3 |
| **Atenção** (0.65–0.75) | 1, 6, 7, 8, 10, 12, 14 | 7 |
| **OK** (≥0.75) | 2, 3, 4, 5, 15 | 5 |

---

## 🛠 Top-3 a retrabalhar (prioridade máxima)

### 1. **Cap 9 — Signaling Systems** (0.61)
Pior do projeto porque combina **dois defeitos sistemáticos no mesmo cap**: (a) Originality colapsada por zero analogia-âncora — viola §2.3 para tipo base; (b) Design comprometido por 37 shrinks e densidade visual monotemática (52 TikZ / 49 frames). Pior, é um capítulo central (signal transduction) que conecta Cap 7 (proteínas) e Cap 11 (integrated). **Patch decisivo:** escrever 1 analogia-âncora forte sobre cascatas MAPK + reduzir shrinks.

### 2. **Cap 11 — Integrated Analysis** (0.65)
Prospectivo que **não declara sua profundidade** — aluno não sabe qual seção vale a pena ir fundo. Resultado: lstlistings distribuídos sem hierarquia, e a régua §2.3 penaliza pesado o Originality. **Patch decisivo:** slide de abertura declarando 2 seções "fundo" vs demais "survey" + redistribuir lstlistings para que ≥3 estejam nas seções profundas.

### 3. **Cap 13 — Systems Medicine** (0.65)
O caso mais óbvio de **survey puro**: 4 lstlistings em 55 frames (0,07 lst/frame — 5× abaixo da Cap 14). Cabe ao cap declarar isso explicitamente, ou elevar o Fundo adicionando 2 lstlistings na seção de Medicina Personalizada + aumentar lstlistings na Ensaios Clínicos. É o prospectivo com mais bibitem (13) — bibliografia forte, maslstlisting fraco.

---

## 🏆 Top-3 já bons (modelos a seguir)

### 1. **Cap 5 — Parameter Estimation** (0.87) ⭐ modelo-ouro
**Único com originalidade 0.9 e Functionality 0.9**. Atende §2.3 (Raue 2009, Voit 2015, Moles 2003, Gutenkunst 2007 — 4 atribuições históricas em cap técnico). 6 questões + 3 Projetos Práticos. **Zero `shrink=`**. Único defeito: slide "\Huge Obrigado!" sem recap — defeito universal do projeto, patch de 2 minutos. **TEMPLATE para todos os caps técnicos.**

### 2. **Cap 4 — Mathematics** (0.84)
Equilíbrio notável entre os 4 eixos (mín 0.8). Único cap com 12 questões + 2 Projetos Práticos em 71 frames sem precisar de **nenhum** `[shrink=N]`. Demonstra que matemática densa **não precisa** de overflow crônico se bem dosada. Gargalo é puramente Design (sem pause visual). Bom **TEMPLATE para Craft** (lstlisting + matemática).

### 3. **Cap 15 — Emerging Topics** (0.78)
Prospectivo que já tem **recapitulação final** (slide síntese pedido na §4.2) e 4 Projetos Práticos — demonstra que "é possível" fazer prospectivo bem. Única mancha crítica: monocromia TikZ (sem `\includegraphics`). **TEMPLATE para prospectivos**, desde que receba diversidade visual.

---

## Conformidade à régua §2.3 (Originality)

| Tipo | Critério §2.3 | Cumprem? | Notas |
|---|---|:---:|:---|
| **Base** | ≥1 analogia-âncora | 1 de 6 (Cap 1 tem analogia histórica; demais violam) | Cap 6/7/8/9 sem analogia → Originality ≤0.5 cada |
| **Técnico** | atribuição histórica + exemplo campo | 4 de 4 | Cap 2/3/4/5 todos cumprem |
| **Prospectivo** | declarar profundidade/survey | 0 de 4 | Cap 11/12/13/14 violam; Cap 15 borderline |

---

## Próximos passos sugeridos

1. **Patch DR-1 universal** (recap final) → +0.05–0.10 em todos
2. **DR-2** para Cap 6/7/8/9 (analogia-âncora) → +0.20–0.30 em Originality
3. **DR-4** para Cap 11/12/13/14 (declaração de cobertura) → +0.20 em Originality
4. **DR-3** para Cap 3 primeiro (57 shrinks) e depois Cap 7 (46) → cortar legibilidade

---

*Fonte: `feature_list.json` (artefato gerado pelo agregador §VI). Patch templates completos em `feature_list.json` → `defeitos_sistemicos[].patch_template`.*
