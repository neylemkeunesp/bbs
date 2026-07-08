# Ponte: Sistemas Populacionais no Contexto do Curso (Cap 10)

**Documento de integração curricular — Curso de Biologia de Sistemas (BBS/UNESP)**

O **Capítulo 10 (Population Systems)** usa o mesmo formalismo matemático dos capítulos anteriores aplicado a uma escala diferente — populações inteiras em vez de moléculas ou células. Este documento posiciona o Cap 10 na estrutura curricular do curso.

---

## Cap 10 ← Cap 4 (Mathematics): mesmo formalismo, nova escala

Todos os modelos do Cap 10 são **sistemas de EDOs não-lineares** — idênticos ao formalismo do Cap 4:

| Modelo (Cap 10) | Estrutura matemática (Cap 4) |
|---|---|
| Crescimento logístico | EDO de 1ª ordem, ponto de equilíbrio estável |
| Lotka-Volterra (predador-presa) | Sistema 2D com ciclos limite (oscilações) |
| Competição entre espécies | Sistema 2D com bifurcação sela-nó |
| SIR epidemiológico | Sistema 3D, análise de R₀ como número de bifurcação |
| Reação-difusão de Turing | EDPs — extensão espacial das EDOs do Cap 4 |

A **análise de estabilidade** (pontos de equilíbrio, autovalores da matriz Jacobiana) e as **bifurcações** (Hopf, sela-nó, pitchfork) estudadas no Cap 4 são as ferramentas para entender:
- Por que populações oscilam (Lotka-Volterra → ciclo limite de Hopf)
- Por que epidemias têm limiar (SIR → bifurcação em R₀ = 1)
- Por que padrões surgem espontaneamente (Turing → instabilidade de Turing via autovalores)

---

## Cap 10 ← Cap 3 (Static Networks): redes como substrato das populações

O Cap 3 modela a **topologia** de redes biológicas. O Cap 10 modela a **dinâmica** sobre essas redes:

- **Redes de contato** em epidemiologia: o SIR em rede heterogênea (hubs, free-scale) se comporta diferente do SIR em população homogênea — threshold R₀ depende da estrutura da rede.
- **Metapopulações**: populações em fragmentos de habitat conectados por dispersão — é um grafo com dinâmica nos nós (Cap 3 + Cap 10).
- **Redes tróficas**: cadeias alimentares (predador-presa, competição) são grafos direcionados onde Lotka-Volterra define a dinâmica.

---

## Cap 10 ← Cap 5 (Parameter Estimation): calibrar modelos populacionais

Os parâmetros dos modelos populacionais precisam ser estimados de dados reais:

- Taxa de crescimento *r*, capacidade de suporte *K* (logístico): estimados por ajuste a séries temporais de censo.
- Coeficientes de Lotka-Volterra (α, β, γ, δ): estimados via mínimos quadrados não-lineares (Levenberg-Marquardt, Cap 5).
- R₀ em surtos reais (COVID-19, dengue): estimação bayesiana a partir de dados de casos — mesmo framework do Cap 5.

---

## Cap 10 ← Cap 8 (Metabolic Systems): população de células como sistema metabólico

A escala "população" aparece também dentro de organismos:

- **Dinâmica de populações celulares** — crescimento tumoral, diferenciação, competição clonal — são Lotka-Volterra intraorganismo.
- **Modelos genome-scale em comunidades microbianas** (microbioma): extensão do FBA (Cap 8) para múltiplas espécies competindo por metabólitos.
- **Efeito Allee em culturas celulares**: populações de células cancerígenas exibem crescimento com efeito Allee (dependência de densidade) — mesmo modelo do Cap 10.

---

## Cap 10 → Cap 13 (Medicine): epidemiologia como biologia de sistemas

Os modelos populacionais têm aplicação médica direta:

- **SIR/SEIR** são a base da epidemiologia quantitativa — usados em políticas de vacinação, quarentena, R₀ de COVID-19.
- **Dinâmica tumoral**: crescimento logístico + competição imuno-tumor = modelo de Lotka-Volterra aplicado a oncologia (Cap 13).
- **Resistência a antibióticos**: competição entre cepas resistentes e sensíveis = modelo de competição de espécies (Cap 10) com implicações clínicas (Cap 13).

---

## Cap 10 → Cap 11 (Integrated Analysis): multi-escala

A biologia de sistemas integrada opera em múltiplas escalas simultaneamente:

```
Moléculas (Cap 7-8-9) → Células → Tecidos → Órgãos → Organismos → Populações (Cap 10)
```

O Cap 11 foca na integração molecular, mas o mesmo princípio se aplica verticalmente: modelos de coração (Cap 12) acoplam escala molecular (canais iônicos, proteínas) com escala de tecido (eletrофiziolоgia). Cap 10 completa a escada adicionando a escala populacional.

---

## Padrões de Turing: do Cap 10 ao Cap 6 (Sistemas Gênicos)

A **instabilidade de Turing** (reação-difusão, Cap 10) aparece também na biologia molecular:

- Padrões de manchas de leopardo, listras de zebra — Turing clássico.
- **Formação de padrões em desenvolvimento embrionário**: genes morfogênicos (Cap 6) criam gradientes de concentração via mecanismos de Turing.
- O circuito activador-inibidor de Turing é matematicamente idêntico a certos circuitos de regulação gênica (Cap 6) — dois nós com feedback positivo e negativo acoplados por difusão.

---

## Posicionamento no curso

```
Cap 3 (Redes Estáticas) ──┐
Cap 4 (Matemática) ────────┼──► Cap 10: Population Systems ──► Cap 13: Medicine
Cap 5 (Estimação) ─────────┘              │
Cap 8 (Metabólico) ────────────────────────┘
Cap 6 (Gênicos) ───────────────────────────────► (Turing/morfogênese)
```

**Posição pedagógica:** Cap 10 é o capítulo de **consolidação matemática** — onde o aluno vê que as mesmas ferramentas (EDOs, bifurcações, estimação) funcionam em escalas completamente diferentes, da molécula à população. Fortalece a ideia central do curso: *sistemas biológicos em todas as escalas compartilham princípios organizacionais comuns*.

---

*Documento gerado pelo graphify-BBS para integrar Cap 10 (Population Systems) ao grafo curricular — 2026-06-12.*
