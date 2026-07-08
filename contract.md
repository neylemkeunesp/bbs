# contract.md — Revisão da Rubric §VI nos Capítulos BBS

**Projeto:** BBS / BioSistemas (Beamer de Biofísica/Systems Biology — UNESP/IBB)
**Origem:** Aplicação da regra §VI de *LOOPS.md* (Karpathy, 2026) — "Score the subjective"
**Data de criação:** 2026-07-01 (v0.1) | **Última atualização:** 2026-07-01 (v0.2 — refinamentos pós-execução)
**Versão atual:** 0.2
**Owner:** Ney Lemke
**Harness:** profile `linus` (Hermes/Claude-Unesp) + delegações em background

---

## Changelog

**v0.2 (2026-07-01, pós-execução):**
- Adicionados **2 refinamentos à régua §2.3** descobertos durante a rodada 4 (Cap 10 e Cap 13):
  - **§2.3.1 Fronteira técnica** — quando cap-base tem `lstlisting ≥ 12`, aplicar regra de técnico também
  - **§2.3.2 Prospectivo survey-puro** — `lstlisting/frames < 5%` admite 0.5 como teto explícito
- §6 atualizado: agora explicitamente "rodadas paralelas de 3, com `max_concurrent_children=3`"
- §8 novos critérios de aceite baseados em achados reais (15 caps revisados)
- §10 lista de iteração esperada — itens 1–4 validados pela execução

**v0.1 (2026-07-01, criação):**
- Pilotagem Cap 1, 4, 15 — capturou a ideia de "régua de Originality por tipo"
- Pesos calibrados D=0.20 · O=0.20 · C=0.30 · F=0.30
- 15 defeitos derivados da pilotagem

---

## 1. Objetivo do contrato (§VI: definindo "done")

Aplicar a rubric §VI (4 eixos ponderados — Design, Originality, Craft, Functionality) aos capítulos do projeto BBS, gerando:

1. **Inventário priorizado** dos capítulos por score §VI (menor score = prioridade de retrabalho)
2. **Diagnóstico por capítulo** dos 4 eixos + gargalo §IX
3. **Critérios derivados de defeitos recorrentes** observados nas rodadas (agora 5 defeitos sistêmicos consolidados)
4. **Feature list ordenado por ROI pedagógico** (§IV — `feature_list.json`)
5. **Kanban CSV** importável em Notion/Trello/GH Projects (`kanban.csv`, `kanban_patches.csv`)

---

## 2. Pesos e threshold (calibrados)

### 2.1 Pesos dos 4 eixos

| Eixo | Peso | Definição operacional |
|---|---|---|
| **Design** | 0.20 | Composição visual, ritmo dos slides, hierarquia de informação |
| **Originality** | 0.20 | Voz autoral, analogias-âncora, atribuição histórica, exemplos próprios |
| **Craft** | 0.30 | Qualidade técnica LaTeX/Beamer: blocos semânticos, TikZ, lstlisting, equações, bibliografia |
| **Functionality** | 0.30 | Alcance pedagógico: objetivos, exercícios, progressão lógica |

### 2.2 Thresholds de Functionality

- **Passa:** ≥ 0.7 — compila, conteúdo correto, didaticamente OK
- **Bom:** ≥ 0.8 — passa + recapitulação final + objetivos explícitos
- **Excelente:** ≥ 0.9 — bom + exercícios com gabarito ou link para .ipynb validado + cobertura equilibrada de tópicos

### 2.3 Régua de Originality por tipo de capítulo (versão v0.2 — REFINADA)

| Tipo | Capítulos | Régua base | Refinamento adicional |
|---|---|---|---|
| **Base** | 1, 6, 7, 8, 9 | Mínimo **1 analogia-âncora** (10–30 palavras, conectando o tópico à vivência do aluno da UNESP). Senão: Originality ≤ 0.5 | — |
| **Técnico** | 2, 3, 4, 5 | Mínimo **1 atribuição histórica explícita** (autor seminal + ano) **+ 1 exemplo concreto do campo do biofísico**. Senão: Originality ≤ 0.6 | — |
| **Prospectivo** | 11, 12, 13, 14, 15 | **Profundidade assimétrica DECLARADA**: escolher 2 dos tópicos para ir fundo, marcar os outros como survey. Senão: Originality ≤ 0.6 | — |

#### §2.3.1 — Refinamento: Fronteira técnica (Cap 10 como caso)

**Detecção:** se cap-base tem `lstlisting ≥ 12` (alta densidade de lstlistings), aplicar a regra de Base E a regra de Técnico simultaneamente.

**Justificativa (achado 2026-07-01):** Cap 10 (Population Systems) tem 7 lstlistings cobrindo Lotka-Volterra, Fisher-KPP, Turing 1952, SIR com COVID-19, etc. É classificado como "Base (fronteira técnica)" porque cobre epidemiologia com SIR (prospectivo). A régua de base sozinha penalizaria Originality severamente, mas a presença de lstlisting denso + atribuições históricas (Lotka-Volterra, Turing 1952, Allee) mostra intenção técnica.

**Aplicação:** se detectar `lstlisting ≥ 12` E presença de ≥3 atribuições históricas com ano, considerar o cap como **fronteira técnica** e aceitar ambas as regras (analogia OU atribuição+exemplo). Cap 10 atingiu 0.65 com este refinamento.

#### §2.3.2 — Refinamento: Prospectivo survey-puro (Cap 13 como caso)

**Detecção:** se cap-prospectivo tem `lstlisting/frames < 5%` (lstlistings raros em relação ao total), admitir 0.5 como teto explícito (não penalizar até 0.6).

**Justificativa (achado 2026-07-01):** Cap 13 (Systems Medicine) cobre 7 tópicos amplos com só 2 lstlistings (3,6% de 55 frames). É survey por design — não cabem 10 lstlistings sem descaracterizar o cap. Mas a falta de DECLARAÇÃO "neste cap: survey" significa que o aluno não sabe.

**Aplicação:** prospectivos survey-puros podem ter Originality até 0.5 com o patching mínimo: 1 slide-inicial declarando "neste cap: tópicos A e B a fundo (com lstlisting), demais são survey". Sem essa declaração, a nota cai ao teto de 0.5 mesmo que conteúdo seja bom.

---

## 3. Definição de "Done" (checklist binário pass/fail)

### 3.1 Por capítulo analisado, o output deve conter:

- [ ] **Estado do disco** (§IV): confirmação `.tex` existe, `.pdf` existe com tamanho em MB, `.log` lido com número de erros e warnings
- [ ] **Amostragem real**: ≥3 seções lidas por capítulo (intro + seção densa + exercícios/referências), com linhas citadas
- [ ] **Score por eixo**: 4 notas 0.0–1.0, cada uma com evidência concreta do `.tex` (cite `\definicao`, `\exemplo`, `begin{tikzpicture}`, etc.)
- [ ] **Score final ponderado**: calculado pela fórmula `D×0.20 + O×0.20 + C×0.30 + F×0.30`
- [ ] **Gargalo §IX**: 1 elo fraco identificado por capítulo
- [ ] **Veredito acionável**: 1-2 patches concretos (cite linhas, estime +0.1 em qual eixo)
- [ ] **Verificação da régua §2.3** (incluindo refinamentos §2.3.1 e §2.3.2)

### 3.2 Para o relatório agregado (todos os caps):

- [ ] **Tabela ranking**: capítulos ordenados por score §VI (asc = prioridade de retrabalho)
- [ ] **Defeitos recorrentes consolidados** (com incidência e ROI)
- [ ] **feature_list.json** (§IV): 15 capítulos + defeitos + modelos a seguir
- [ ] **kanban.csv** + **kanban_patches.csv** (input direto para Kanban real)
- [ ] **ranking_N_caps.md**: tabela PT-BR com estatísticas
- [ ] **VEREDITO_FINAL.md**: ≤600 palavras em PT-BR

---

## 4. Critérios derivados dos defeitos encontrados (5 SISTÊMICOS, validados)

Aplicar como **checklist** em todos os capítulos novos durante a revisão:

### 4.1 Craft — defeitos de produção LaTeX

- [ ] **Nenhum bloco TikZ comentado no source** (achado no Cap 1 piloto, linhas 689–700)
- [ ] **Todo lstlisting tem**: `caption=` descritivo + frase introdutória `"O que este código faz"` acima
  - ⚠️ **Atenção v0.2:** "intro_present=1" via título do frame NÃO substitui frase explícita (confirmado por DR-4b no Cap 10)
- [ ] **Equações em ambiente `equation*`/`align*`**, nunca inline cru para fórmulas longas
- [ ] **Bibliografía com ≥5 entradas**, cada `\bibitem` deve ter autor + ano + título/editora
- [ ] **Warnings do `pdflatex` revisados**: `overfull \hbox` em >10 ocorrências = problema de ritmo

### 4.2 Functionality — defeitos pedagógicos

- [ ] **Objetivos de aprendizagem explícitos** no início (4–7 bullets específicos, não genéricos)
- [ ] **≥5 questões de exercício** OU 1 projeto prático integrador (achado em Cap 15: 3 questões é pouco para 6 tópicos)
- [ ] **Recapitulação final** com 5 bullets-síntese (NUNCA slide `{\Huge Obrigado!}` — defeito DR-1 universal 15/15)
- [ ] **Progressão lógica**: intro → desenvolvimento → síntese → exercícios → referências (sem "saltos" temáticos)

### 4.3 Originality — defeitos de voz autoral

- [ ] **1 analogia-âncora** para capítulos-base (ver §2.3) — defeito DR-2 em 4/6 bases
- [ ] **1 atribuição histórica** com autor+ano para capítulos-técnicos — citações tipo "Lotka-Volterra" sem ano quebram §2.3
- [ ] **Cobertura declarada** para capítulos-prospectivos (marcar "neste cap: X (profundo), Y, Z (survey)")

### 4.4 Design — defeitos visuais

- [ ] **Slides não devem depender de `[shrink=N]`** ≥ 20 em mais de 50% dos frames (defeito DR-3 em 12/15 caps)
- [ ] **Mix TikZ + `\includegraphics`** — risco de monocromia visual se 100% TikZ (defeito em 13/15 caps consecutivos)
- [ ] **Hierarquia de blocos diferenciada** — não usar todos os blocos da mesma cor

### 4.5 Prospectivo-specific (refinamentos §2.3.2)

- [ ] **Declaração explícita de cobertura** obrigatória em prospectivos — defeito DR-4 em 4/4 prospectivos
- [ ] Se cap é survey-puro (lstlisting/frames < 5%), admitir Originality 0.5 com patching mínimo de 1 slide

---

## 5. Escopo da execução

### 5.1 Capítulos BBS (15 caps base)

| # | Arquivo | Tipo (regra §2.3) |
|---|---|---|
| 1 | `capitulo01-sistemas-biologicos.tex` | Base |
| 2 | `capitulo02-modelagem-matematica.tex` | Técnico |
| 3 | `capitulo03-static-networks.tex` | Técnico |
| 4 | `capitulo04-mathematics.tex` | Técnico |
| 5 | `capitulo05-parameter-estimation.tex` | Técnico (modelo-ouro) |
| 6 | `capitulo06-sistemas-genicos.tex` | Base |
| 7 | `capitulo07-protein-systems.tex` | Base |
| 8 | `capitulo08-metabolic-systems.tex` | Base |
| 9 | `capitulo09-signaling-systems.tex` | Base (parcialmente patchado) |
| 10 | `capitulo10-population-systems.tex` | Base (fronteira técnica, §2.3.1) |
| 11 | `capitulo11-integrated-analysis.tex` | Prospectivo |
| 12 | `capitulo12-heart-physiology.tex` | Prospectivo |
| 13 | `capitulo13-medicine.tex` | Prospectivo (survey-puro, §2.3.2) |
| 14 | `capitulo14-design-systems.tex` | Prospectivo |
| 15 | `capitulo15-emerging-topics.tex` | Prospectivo (modelo-recap) |

**Total: 15 capítulos**

### 5.2 Capítulos bonus (fora do escopo principal)

- `capitulo01-historia-filosofia.tex`
- `capitulo02-ferramentas-computacionais.tex`
- `capitulo02-ferramentas-ia.tex`
- `capitulo02-metodos-otimizacao.tex`

Avaliar separadamente se desejado — não bloqueiam o resultado principal.

---

## 6. Plano de execução por fases (REFINADO v0.2)

### Fase A — Inventário bruto (delegação leaf, ~2 min/cap)

Para cada capítulo:
1. Confirmar `.tex` + `.pdf` + `.log` no disco
2. Contar: `begin{frame}`, `begin{tikzpicture}`, `begin{lstlisting}`, `\definicao`, `\exemplo`, `\bibitem`, `\includegraphics`, `Questão`, `Projeto Prático`, linhas totais
3. Ler `.log` para extrair: número de erros, warnings, overfull hboxes, páginas do PDF
4. Amostrar ≥3 seções distintas (intro + densa + final de exercícios/refs)

### Fase B — Rubric & gargalo (delegação leaf, ~5 min/cap)

Para cada capítulo:
1. Atribuir notas 0.0–1.0 nos 4 eixos com evidência concreta
2. Calcular score final ponderado
3. Identificar gargalo §IX
4. Veredito acionável (1–2 patches concretos)
5. **Verificar conformidade com §2.3** + refinamentos §2.3.1/.2

### Fase C — Agregação (delegação orchestrator, uma só)

1. Tabela ranking de todos os capítulos
2. Defeitos recorrentes (lista com frequência, ROI)
3. Geração do `feature_list.json` (§IV)
4. Geração do `kanban.csv` + `kanban_patches.csv`
5. Geração do `ranking_N_caps.md` + `VEREDITO_FINAL.md`

### Fase D — Saída executiva

- 6 artefatos finalizados:
  - `contract.md` (este, atualizado)
  - `feature_list.json`
  - `kanban.csv` + `kanban_patches.csv`
  - `ranking_15_capitulos.md` ou similar
  - `VEREDITO_FINAL.md`
  - `progress.md` + `log.md` (estado do harness)

### Paralelização (v0.2 — explícito)

- `max_concurrent_children=3` no harness Hermes/Claude-Unesp
- Rodadas de **3 capítulos por vez** (técnicos / bases / fronteira / prospectivos)
- Validado: 4 rodadas paralelas processaram 12 caps em ~10 min total

---

## 7. Restrições e princípios

### 7.1 Invioláveis

- **Zero fabricação**: subagents não inventam conteúdo. Se a leitura do `.tex` falhar, o subagent reporta o blocker, não infere.
- **Não modificar `.tex` durante revisão** (exceção: Fase pós-revisão, fase separada, com novo contrato): tarefa é *ler e diagnosticar*, não patchar.
- **Limite de leitura**: ~50KB por capítulo (não ler arquivo inteiro, só amostras representativas)
- **Validar artefatos finais** (§VII — "read the traces"): JSON válido, contagem de palavras, contagem de linhas
- **PT-BR** em toda comunicação e output

### 7.2 Trade-offs aceitos

- **Cobertura sobre profundidade absoluta**: prefere-se rubricar todos os caps com notas decentes (>0.5 de confiança) a fazer 3 com análise exaustiva.
- **Velocidade > perfeição**: cada capítulo recebe ~5 min de análise, não 30.
- **Confiança marcada como `medium/baixa` em subjetividade**: eixos Design/Originality podem variar ±0.05 entre revisores — documentar no JSON.

---

## 8. Critérios de aceite final (REFINADO v0.2)

### 8.1 Entrega está **completa** quando:

- [ ] 15 capítulos revisados com scores + evidências (ou N se escopo menor)
- [ ] Tabela agregada dos 15 capítulos (ou N) em markdown
- [ ] `feature_list.json` gerado + validado com `python -m json.tool`
- [ ] `kanban.csv` + `kanban_patches.csv` gerados
- [ ] `ranking_N_caps.md` gerado
- [ ] `VEREDITO_FINAL.md` com ≤600 palavras (validar com `wc -w`)

### 8.2 Entrega está **bem-sucedida** quando, além do acima:

- [ ] O Ney consegue usar o `feature_list.json` como Kanban real (não só olhar)
- [ ] **Ao menos 1 defeito recorrente novo é descoberto** (não estava na pilotagem 3 caps)
- [ ] A régua §2.3 (incluindo refinamentos v0.2) produz scores discriminantes — ou seja, diferenciar Base vs Técnico vs Prospectivo consistentemente
- [ ] Modelo a seguir fica explícito (Cap 5 para técnico, Cap 15 para prospectivo)
- [ ] Média geral fica entre 0.65–0.75 (esperado pelo piloto + refinamento)

---

## 9. Fora de escopo

- Reescrita real dos capítulos (analogias escritas completas, slides novos, TikZ refeito) — vem em **fase separada**, **depois** da revisão
- Patch no template Beamer do BBS
- Atualização do `AGENTS.md` do projeto
- Tradução ou revisão ortográfica
- Geração de figuras/imagens externas
- Compilação final + verificação visual dos PDFs gerados (cada cap pode ter output diferente)

---

## 10. Iteração esperada

Esta é a **versão 0.2** do contrato. Para v0.3, considerar:

1. **Pesos dos eixos se algum discriminou mal** (ex: baixou Craft para 0.25 e subiu Functionality para 0.35?)
2. **Refinar a régua §2.3** se aparecer nova categoria de capítulo (ex: "experimental" ou "computacional-only")
3. **Adicionar defeitos novos** achados em ≥3 capítulos à lista §4 (de 5 para 6+)
4. **Pesos por tipo diferentes** (ex: prospectivos podem ter Design mais alto, bases Craft mais alto)
5. **Subir para `v1.0`** quando ≥30 caps revisados e 0 defeitos sistêmicos genéricos novos (só específicos)

---

## 11. Conexão com a skill `bbs-rubric-review`

Este contrato é a fonte de verdade para a skill `~/.hermes/profiles/linus/skills/productivity/bbs-rubric-review/SKILL.md`. Se a skill divergir deste contrato no futuro, **contrato vence** — atualizar a skill depois.

---

**Próximo passo:** se quiser iterar para v0.3, aplicar este contrato nos 4 capítulos bonus do escopo §5.2 ou em uma nova geração de caps BBS.
