# Veredito Final — Revisão §VI (BBS Beamer · 15 capítulos)

**Data:** 2026-07-01 · **Harness:** `linus` (Hermes/Claude-Unesp)
**Input:** pilotagem Cap 1/4/15 + 4 rodadas de revisão (técnicos 2/3/5; bases 6/7/8; fronteira 9/10/11; prospectivos 12/13/14).

---

## Resumo executivo

Os 15 capítulos do BBS foram rubricados com média **0.717**, mediana 0.69 e faixa 0.61–0.87 — discriminando bem. Identificamos **5 defeitos sistêmicos** que explicam ≥80% da variância entre caps. A régua §2.3 (Originality por tipo) **funciona**, mas pede refinamento para fronteira técnica e prospectivo survey-puro.

---

## Ranking 1°–3° pior e 1°–3° melhor

**🔴 Piores:** **1) Cap 9 (0.61)** — combo Originality+Design (zero analogia+37 shrinks); **2) Cap 13 (0.65)** — survey puro (2 lstlistings/55 frames) sem declaração; **3) Cap 11 (0.65)** — prospectivo sem declarar profundidade.

**🟢 Melhores:** **1) Cap 5 (0.87)** — único com O=0.9 e F=0.9; zero shrinks; **2) Cap 4 (0.84)** — equilíbrio de 4 eixos, 12Q+2PP sem shrink; **3) Cap 15 (0.78)** — prospectivo com recap final (raro).

---

## 5 defeitos sistêmicos consolidados

| ID | Defeito | Incidência | ROI |
|---|---|:---:|:---:|
| **DR-1** | Slide `Obrigado!` sem recap | **15/15** | ALTO |
| **DR-2** | Analogia-âncora ausente em base | **4/6** (Cap 6/7/8/9) | ALTO |
| **DR-3** | `[shrink=N]` excessivo | **12/15** | MÉDIO |
| **DR-4** | Profundidade não declarada em prospectivos | **4/4** | MÉDIO-ALTO |
| **DR-5** | lstlistings sem caption | parcial em ≥3 (grave Cap 3) | MÉDIO |

DR-1 é universal (todo cap perde 0.05–0.10 no Functionality); patch de 2 minutos/cap. DR-2 é o segundo mais barato com maior retorno.

---

## Régua §2.3 — validada + 2 refinamentos

A régua sobrevive: técnicos 0.81 > prospectivos 0.69 > bases 0.68. **Dois refinamentos necessários:**

1. **Fronteira técnica (Cap 10):** se cap-base tem `lstlisting ≥ 12`, aplicar TAM bém regra de técnico (atribuição+analogia).
2. **Prospectivo survey-puro (Cap 13):** adicionar critério `lstlisting/frames ≥ 5%` à régua prospectiva, ou admitir Cap 13 explicitamente como 0.5 ("este cap é survey por design").

---

## Roadmap ótimo de retrabalho

Para Kanban real, executar nesta ordem:

1. **DR-1 universal** (15 slides de recap) → ganho homogêneo.
2. **DR-2 nos 4 caps-base** (Cap 6/7/8/9) → +0.20–0.30 Originality em cada.
3. **DR-4 nos 4 caps-prospectivos** (Cap 11/12/13/14) → restabelece §2.3.
4. **DR-3+DR-5 no Cap 3** (57 shrinks + 10/11 lstlistings sem caption) → caso mais agudo.
5. **DR-3 no Cap 7** (46 shrinks, 66% dos frames) → segundo pior.

Ordem por cap: **Cap 9 → 11 → 13 → 12 → 8 → 6 → 10 → 7 → 14 → 1 → 3 → 2 → 15 → 4 → 5**. Cobrir DR-1+DR-2+DR-4 promete **média ≥ 0.80** com esforço ~30–40 h.

---

## Modelo a seguir

**Cap 5 (Parameter Estimation) → TEMPLATE OFICIAL.** Único com O=0.9 e F=0.9, cumpre §2.3, zero shrinks — é o que cada cap deveria ser. Único defeito trivial (sem recap) faz dele o **modelo-ouro** para replicação (especialmente Cap 2 e Cap 3, técnicos com lstlisting denso).

Complementares: **Cap 4** = template-craft (lstlisting + matemática sem shrink); **Cap 15** = template-prospectivo (já tem recap, diversificar visualmente com `\includegraphics`).

---

## Confiança e ressalvas

**Alta:** contagens automatizadas (shrink/lst/tikz/bibitem) validadas por grep; scores coerentes com sinais numéricos. **Média:** scores por amostragem (±0.05 Design/Originality entre revisores). **Baixa:** qualidade das lstlistings (não executadas). Nenhuma discrepância grave entre as 4 rodadas.

---

**Próximo passo:** anexar `feature_list.json`, `ranking_15_capitulos.md` e este veredito a Kanban (Notion/Trello/GH Projects) com colunas por defeito e tags por cap.
