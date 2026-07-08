log.md — BBS §VI Rubric Review (append-only)

## [2026-07-01] contract | v0.1 rubric review contract created
- Owner: hermes_linus
- Origem: pilotagem §VI em Cap 1, 4, 15
- Achado-chave capturado: régua de Originality por tipo de capítulo (base/técnico/prospectivo)
- Próximo passo: disparar Fase A+B em 12 capítulos remanescentes

## [2026-07-01] review_round_1 | técnicos (Cap 2, 3, 5)
- Cap 2 — Modelagem Matemática: 0.77 — Verhulst, Lotka-Volterra, Gennes 1971, Duke 1989 OK
- Cap 3 — Static Networks: 0.76 — Barabási-Albert 1999, Watts-Strogatz 1998, Kacser-Burns 1973 OK; 10/11 lstlistings sem caption + 57 shrinks
- Cap 5 — Parameter Estimation: 0.87 — Raue 2009, Voit 2015, Moles 2003, Gutenkunst 2007 OK
- Defeito recorrente (3/3): ausência de recapitulação final
- Defeito recorrente (2/3): [shrink=N] excessivo
- Defeito parcial (1/3): lstlistings sem caption (Cap 3, grave)
- Próximo: aguardar Rodada 2 (Cap 6, 7, 8 — bases)

## [2026-07-01] review_round_4 | prospectivos finais (Cap 12, 13, 14)
- Cap 12 — Heart Physiology: 0.66 — profundidade real (3 lstlistings + tabela histórica Noble→Beeler-Reuter→Luo-Rudy→ten Tusscher→O'Hara-Rudy), não declarada
- Cap 13 — Systems Medicine: 0.65 — survey puro (2 lstlistings/55 frames, 7 tópicos sem fundo demarcado); 13 bibitems fortes (Barabási, Auffray, Hood, Hanahan)
- Cap 14 — Design Systems: 0.72 — melhor da rodada: 25 TikZ, 6 lstlistings (toggle/repressilator + COBRApy/FSEOF + Gillespie/AG), 6 exemplos; Gardner 2000, Elowitz 2000
- Conformidade §2.3: nenhum prospectivo declara profundidade (mesmo Cap 14 que tem profundidade real)
- Próximo: agregação C + saída D

## [2026-07-01] aggregation_C | feature_list.json + veredito final
- feature_list.json: 22 KB, JSON válido, 15 capítulos + 5 defeitos sistêmicos + 3 modelos a seguir
- ranking_15_capitulos.md: 8 KB, tabela ascendente + estatísticas
- VEREDITO_FINAL.md: 576 palavras (no limite ≤600)
- Média: 0.717 · Mediana: 0.69 · Desvio: 0.075 · Faixa: 0.61–0.87
- Médias por tipo: Técnico 0.810 > Prospectivo 0.692 > Base 0.677
- Distribuição: Crítica (<0.65)=3 · Atenção (0.65–0.75)=7 · OK (≥0.75)=5
- Modelo a seguir: Cap 5 (template-oficial); Cap 4 (template-craft); Cap 15 (template-prospectivo)
- Roadmap ótimo: DR-1 universal → DR-2 nos 4 base → DR-4 nos 4 prospectivos → DR-3+DR-5 no Cap 3 → Cap 7
- Promessa: média ≥0.80 com esforço ~30–40h
- Encerramento: Kanban real pode usar feature_list.json como input
