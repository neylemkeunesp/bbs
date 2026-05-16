# Capítulo 4: The Mathematics of Biological Systems

## Descrição

Slides e material de apoio do **Capítulo 4** do curso de Bioinformática Aplicada à Biologia de Sistemas.

Este capítulo cobre as ferramentas matemáticas fundamentais para modelar e analisar sistemas biológicos dinâmicos.

---

## Conteúdo

### Parte I: Dinâmica
- **Sistemas de EDOs** — forma geral e vetorial, sistemas autônomos
- **Retratos de fase** — campos vetoriais, nulclinas, campos de direção
- **Modelo Lotka-Volterra** — sistema predador-presa, órbitas fechadas
- **Implementação em Python** — `scipy.integrate.odeint`

### Parte II: Análise de Estabilidade
- **Pontos de equilíbrio** — interpretação biológica (homeostase)
- **Linearização e Jacobiana** — análise local
- **Autovalores e estabilidade** — nós, espirais, selas, centros
- **Teorema de Lyapunov** — funções de energia

### Parte III: Bifurcações
- **Saddle-node** — aparecimento/desaparecimento de equilíbrios
- **Transcrítica** — troca de estabilidade
- **Pitchfork** — supercrítica (suave) vs subcrítica (abrupta)
- **Hopf** — surgimento de oscilações (ciclos limite)

### Parte IV: Oscilações e Ciclos Limite
- **Soluções periódicas** e ciclos limite
- **Teorema de Poincaré-Bendixson**
- **Oscilador de Van der Pol** — paradigma de osciladores biológicos
- **Osciladores biológicos**: ritmos circadianos, cálcio, glicolíticos, ciclo celular

### Parte V: Análise de Sensibilidade
- **Sensibilidade local** — coeficientes normalizados
- **Equações de sensibilidade**
- **Métodos globais**: Morris, índices de Sobol (SALib)
- **Latin Hypercube Sampling** e sequências de Sobol

---

## Ferramentas Python

```python
# Resolver sistema de EDOs
from scipy.integrate import odeint
import numpy as np

def lotka_volterra(X, t, alpha, beta, delta, gamma):
    x, y = X
    return [alpha*x - beta*x*y,
            delta*x*y - gamma*y]

sol = odeint(lotka_volterra, [2.0, 1.0],
             np.linspace(0, 50, 1000),
             args=(1.0, 0.5, 0.5, 1.0))
```

---

## Referências Principais
- Strogatz, S.H. (2015). *Nonlinear Dynamics and Chaos*. Westview Press.
- Murray, J.D. (2002). *Mathematical Biology I*. Springer.
- Alon, U. (2019). *An Introduction to Systems Biology*, 2nd ed. CRC Press.

---

## Exercícios

Os exercícios do capítulo cobrem:
1. Sistemas lineares e retratos de fase
2. Análise de estabilidade (Jacobiano e autovalores)
3. Diagramas de bifurcação computacionais
4. Simulação do oscilador de Van der Pol
5. Análise de sensibilidade local e global (Sobol)

**Projeto prático:** Implementar e analisar um modelo de rede regulatória (toggle switch ou repressilator) com análise completa de estabilidade, bifurcações e sensibilidade.
