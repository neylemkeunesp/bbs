# Ponte: Sistemas Moleculares → Análise Integrada (Caps 7-9 → Caps 11-14)

**Documento de integração curricular — Curso de Biologia de Sistemas (BBS/UNESP)**

Este documento explicita as conexões entre o bloco de **Sistemas Moleculares** (Caps 7, 8, 9) e o bloco de **Aplicações Integradas** (Caps 11, 12, 13, 14). O Cap 11 (Integrated Analysis) é o nó de chegada que amarra os três sistemas moleculares num único framework multi-ômico.

---

## O elo: multi-ômica como convergência dos sistemas moleculares

| Sistema (origem) | Ômica correspondente | Papel no Cap 11 |
|---|---|---|
| Protein Systems (Cap 7) | Proteômica (LC-MS, espectrometria) | Camada de proteínas no modelo integrado |
| Metabolic Systems (Cap 8) | Metabolômica (GC-MS, FBA) | Camada de metabólitos e fluxos |
| Signaling Systems (Cap 9) | Fosfoproteômica / Transcriptômica | Camada de regulação e cascatas |
| Sistemas Gênicos (Cap 6) | Transcriptômica (RNA-seq) | Camada de expressão gênica |

O **caso de estudo do ciclo da trealose em levedura** (Cap 11) usa simultaneamente:
- Enzimas com cinética de Hill (Cap 7)
- Balanço de fluxo metabólico — FBA (Cap 8)
- Cascatas de sinalização por cAMP/PKA (Cap 9)
- Expressão gênica dos genes de trealose (Cap 6)

---

## Cap 11 (Integrated Analysis) ← Caps 7, 8, 9

### Do Cap 7 para o Cap 11
- As **proteínas enzimáticas** com parâmetros cinéticos estimados (Vmax, Km, Hill) são os agentes dos modelos integrados de levedura e de coração.
- A **proteômica quantitativa** (Cap 7) fornece abundância de proteínas como dado de entrada para modelos genome-scale (Cap 11).
- **Modificações pós-traducionais** (fosforilação, ubiquitinação — Cap 7) são lidas pela fosfoproteômica integrada no Cap 11.

### Do Cap 8 para o Cap 11
- **COBRApy e modelos genome-scale** (Cap 8) são o motor computacional central do Cap 11.
- A **análise de fluxo metabólico com ¹³C** (Cap 8) é o método experimental que valida os modelos integrados.
- Modos elementares e FBA (Cap 8) são reutilizados diretamente na análise integrada da levedura.

### Do Cap 9 para o Cap 11
- As **vias MAPK, PI3K/Akt e JAK-STAT** (Cap 9) aparecem como reguladores da expressão gênica nos modelos integrados de câncer (Cap 13) e de design sintético (Cap 14).
- A **ultrasensibilidade de Goldbeter-Koshland** (Cap 9) é mecanismo chave no modelo de ciclo celular integrado (Cap 11).

---

## Cap 12 (Heart Physiology) ← Caps 7, 8, 9

O coração como sistema biológico usa os três níveis moleculares simultaneamente:

- **Proteínas contráteis** — actina, miosina, troponina (Cap 7: estrutura e cinética)
- **Metabolismo cardíaco** — oxidação de ácidos graxos, glicólise (Cap 8: FBA e MFA)
- **Sinalização β-adrenérgica** — receptores GPCRs → cAMP → PKA → fosforilação de canais iônicos (Cap 9: cascatas de sinalização)

O modelo de **Hodgkin-Huxley** do potencial de ação cardíaco requer:
- Cinética de canais iônicos (proteínas — Cap 7)
- EDOs não-lineares com bifurcações (Cap 4)
- Estimação de parâmetros de condutância (Cap 5)

---

## Cap 13 (Medicine) ← Caps 7, 8, 9

Aplicações médicas de biologia de sistemas usam o framework molecular completo:

- **Alvos farmacológicos** são proteínas (receptores, enzimas — Cap 7); a seletividade de droga depende da estrutura 3D (PDB, Cap 7).
- **Reprogramação metabólica do câncer** (efeito Warburg) é modelada com FBA e COBRApy (Cap 8).
- **Resistência a imunoterapia** envolve vias de sinalização PI3K/Akt e PD-L1 (Cap 9).
- A **medicina de precisão** usa dados multi-ômicos integrados (Cap 11) para estratificação de pacientes.

---

## Cap 14 (Design Systems / Biologia Sintética) ← Caps 6, 7, 8, 9

O design de circuitos biológicos sintéticos requer controle sobre todos os níveis:

- **Promotores e reguladores** — design de GRNs sintéticas (Cap 6)
- **Enzimas designer** — engenharia de proteínas (Cap 7: estrutura + cinética)
- **Vias metabólicas ortogonais** — design de rotas biossintéticas (Cap 8: FBA)
- **Switches e osciladores** — circuitos de sinalização sintéticos (Cap 9: ultrasensibilidade)

O **repressilator** (Elowitz & Leibler, 2000) — oscilador gênico sintético clássico — conecta Cap 6 (rede gênica), Cap 4 (EDOs/ciclos limite) e Cap 9 (cascatas de repressão).

---

## Fluxo pedagógico dos caps 7-9 → 11-14

```
Cap 6: Sistemas Gênicos ──────────────────────────────────────┐
Cap 7: Protein Systems ──────┬────────────────────────────────┤
Cap 8: Metabolic Systems ────┼── Cap 11: Integrated Analysis ─┤
Cap 9: Signaling Systems ────┘         (trealose/levedura)    │
                                                               ▼
                                          Cap 12: Heart Physiology
                                          Cap 13: Medicine (câncer)
                                          Cap 14: Design Systems
```

O Cap 11 funciona como **hub de integração**: é onde o aluno percebe que os três sistemas moleculares estudados separadamente (proteínas, metabolismo, sinalização) são na verdade camadas acopladas de um único sistema biológico.

---

## Sugestão pedagógica

Usar o **ciclo da trealose em levedura** como fio condutor já no início do curso:
1. Introduzir o sistema completo no Cap 1 (visão geral)
2. Modelar componentes isolados nos Caps 6-9
3. Re-integrar o sistema completo no Cap 11

Isso evita que os alunos percam o contexto integrador enquanto estudam cada camada molecular separadamente.

---

*Documento gerado pelo graphify-BBS para fechar gap de documentação entre o bloco molecular (Caps 7-9) e o bloco de aplicações integradas (Caps 11-14) — 2026-06-12.*
