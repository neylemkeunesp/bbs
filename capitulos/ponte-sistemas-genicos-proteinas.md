# Ponte: Sistemas Gênicos → Proteínas (Caps 6–7)

**Documento de integração curricular — Curso de Biologia de Sistemas (BBS/UNESP)**

Este documento explicita a conexão entre o **Capítulo 6 (Sistemas Gênicos)** e o **Capítulo 7 (Protein Systems)**, que no curso são tratados sequencialmente mas raramente citados um pelo outro. A conexão é o **Dogma Central da Biologia Molecular**.

---

## O elo perdido: do gene à proteína funcional

O Capítulo 6 modela redes de regulação gênica (*Gene Regulatory Networks*, GRNs) como grafos — nós são genes/fatores de transcrição, arestas são relações de ativação ou repressão. O Capítulo 7 analisa proteínas em sua estrutura tridimensional e cinética enzimática. O que liga os dois?

> **Toda proteína estudada no Cap 7 é produto de um gene regulado pelas redes do Cap 6.**

Mais precisamente:

- Os **fatores de transcrição** que formam os nós centrais das GRNs (Cap 6) *são* proteínas — com estrutura 3D, domínios de ligação a DNA, e cinética de associação/dissociação que pode ser modelada com Hill (Cap 7).
- A **expressão gênica** quantificada por RNA-seq (Cap 6) é o upstream direto da **abundância de enzimas** nos modelos metabólicos (Cap 8) e das cascatas de sinalização (Cap 9).
- A **regulação pós-traducional** por modificações como fosforilação (Cap 7, PTMs) retroalimenta a expressão gênica — criando loops que conectam Cap 7 de volta ao Cap 6.

---

## Conexões específicas no currículo

### Cap 6 → Cap 7: GRNs produzem proteínas

| Conceito no Cap 6 | Conceito correspondente no Cap 7 |
|---|---|
| Fator de transcrição (nó da GRN) | Proteína com domínio de ligação a DNA (estrutura 3D) |
| Ativação/repressão gênica | Cinética de Hill — cooperatividade e limiar de ativação |
| RNA mensageiro como saída da rede | Precursor da proteína enzimática (tradução) |
| Medição por RNA-seq (expressão) | Medição por proteômica/espectrometria de massas |
| GenBank — sequência nucleotídica | PDB (Protein Data Bank) — estrutura 3D |
| Modelo ODE da GRN (mRNA + proteína) | Cinética enzimática de Michaelis-Menten/Hill |

### Cap 7 → Cap 6: proteínas regulam genes (feedback)

A **fosforilação** (PTM, Cap 7) é o mecanismo molecular mais comum de regulação de fatores de transcrição:

- Receptores de superfície (Cap 9) ativam quinases → quinases fosforilam fatores de transcrição → fatores entram no núcleo e alteram a rede gênica (Cap 6).
- Exemplo clássico: via **MAPK/ERK** (Cap 9) fosforila o fator de transcrição **ELK1**, que ativa genes de crescimento celular (Cap 6).

Este é o loop de feedback que conecta os três capítulos da trinca molecular:

```
Gene (Cap 6) → mRNA → Proteína/Enzima (Cap 7)
                              ↓
                    Sinalização (Cap 9)
                              ↓
                Fosforilação de TFs → Gene (Cap 6)
```

---

## Por que Sistemas Gênicos e Proteínas ficam em comunidades separadas

No grafo de conhecimento do curso, Cap 6 está na comunidade de **Redes & Matemática** (junto com Caps 3, 4, 5) enquanto Cap 7 está na comunidade de **Sistemas Moleculares** (junto com Caps 8, 9). Isso reflete como o conteúdo está escrito:

- Cap 6 usa a linguagem de **teoria dos grafos e EDOs** (vinda dos Caps 3 e 4) para modelar redes gênicas.
- Cap 7 usa a linguagem de **cinética enzimática e estrutura molecular** para modelar proteínas.

A ponte conceitual — que o produto de uma GRN é sempre uma proteína, e que proteínas regulam GRNs via PTMs — precisa ser explicitada em aula como **fio condutor** entre os dois blocos temáticos.

---

## Ponto de integração para o Capítulo 11 (Integrated Analysis)

O Capítulo 11 (Multi-ômica) é justamente onde essa ponte se fecha formalmente:

- **Transcriptômica** (RNA-seq, Cap 6) + **Proteômica** (espectrometria, Cap 7) + **Metabolômica** (Cap 8) = análise integrada.
- O caso de estudo do ciclo da trealose em levedura (Cap 11) conecta regulação gênica, enzimas e metabólitos num único modelo.

**Sugestão pedagógica:** usar o Cap 11 como "capítulo de chegada" que amarra os Caps 6, 7, 8 e 9 num único sistema biológico concreto.

---

## Referências cruzadas no curso

- **Cap 3** (Static Networks): redes PPI (protein-protein interaction) são o interatoma — a visão estrutural das proteínas do Cap 7 como nós de uma rede.
- **Cap 4** (Mathematics): os modelos ODE de GRNs (Cap 6) usam o mesmo formalismo de bifurcação e estabilidade do Cap 4; as enzimas do Cap 7 geram não-linearidades (Hill) que produzem biestabilidade.
- **Cap 5** (Parameter Estimation): estimar parâmetros cinéticos de enzimas (Cap 7) e de redes gênicas (Cap 6) usa os mesmos algoritmos (Levenberg-Marquardt, algoritmos evolutivos).

---

*Documento gerado pelo graphify-BBS para fechar gap de documentação identificado na análise de grafo de conhecimento do curso (2026-06-12).*
