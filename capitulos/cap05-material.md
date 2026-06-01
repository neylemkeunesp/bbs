# Capítulo 5: Parameter Estimation (Estimação de Parâmetros)

## Descrição

Slides e material de apoio do **Capítulo 5** do curso de Bioinformática Aplicada à Biologia de Sistemas.

Este capítulo aborda os conceitos, formulações e algoritmos para estimar parâmetros de modelos biológicos a partir de dados experimentais, bem como a análise de identificabilidade e incerteza.

---

## Conteúdo

### Parte I: Formulação do Problema Inverso
- **Problema Direto vs. Inverso** — conceitos e desafios (mal-posto, ruído, mínimos locais)
- **Função Objetivo (Cost Function)** — quantificação de discrepância
- **Mínimos Quadrados Ordinários (OLS) e Ponderados (WLS)**
- **Maximum Likelihood Estimation (MLE)** — relação com OLS sob ruído gaussiano
- **Abordagem Bayesiana** — posterior, likelihood e prior (regularização)

### Parte II: Métodos de Otimização Local
- **Busca em Grade (Grid Search)** — conceito de varredura e maldição da dimensionalidade
- **Métodos de Gradiente** — Gradient Descent (taxa de aprendizado e convergência)
- **Métodos de Segunda Ordem** — Newton-Raphson e Gauss-Newton (Hessiana vs. Jacobiana)
- **Algoritmo de Levenberg-Marquardt (LM)** — método híbrido padrão para ajuste não-linear
- **Ajuste Prático em Python** — `scipy.optimize.curve_fit` e `least_squares`

### Parte III: Métodos de Otimização Global
- **Necessidade de Métodos Globais** — escape de mínimos locais em landscapes não-convexos
- **Algoritmos Genéticos (GA)** — analogia biológica, seleção, cruzamento e mutação
- **Simulated Annealing (SA)** — física do recozimento de metais e aceitação probabilística
- **Differential Evolution (DE)** — robustez baseada em diferenças vetoriais
- **Particle Swarm Optimization (PSO)** — inteligência coletiva (enxame)

### Parte IV: Identificabilidade e Incerteza
- **Identificabilidade Estrutural** — se é matematicamente possível estimar os parâmetros
- **Identificabilidade Prática** — limitações impostas pela qualidade e quantidade dos dados
- **Matriz de Informação de Fisher (FIM)** — curvatura do erro e limites de incerteza
- **Intervalos de Confiança Assintóticos** — cálculo por meio da matriz de covariância
- **Profile Likelihood** — mapeamento de incerteza e detecção de parâmetros não-identificáveis

### Parte V: Validação de Modelos e Seleção
- **Análise de Resíduos** — testes de homocedasticidade, independência e gaussianidade
- **Coeficiente de Determinação ($R^2$ e $R^2$ ajustado)**
- **Critérios de Informação** — AIC (Akaike) e BIC (Bayesiano) para balancear ajuste e complexidade
- **Validação Cruzada (Cross-Validation)** — K-Fold e prevenção de overfitting

---

## Ferramentas Python

Abaixo, um exemplo clássico de ajuste não-linear usando `scipy.optimize.curve_fit` para estimar os parâmetros $V_{\max}$ e $K_M$ da cinética enzimática de Michaelis-Menten:

```python
from scipy.optimize import curve_fit
import numpy as np

# Modelo matemático
def michaelis_menten(S, Vmax, Km):
    return Vmax * S / (Km + S)

# Dados experimentais sintéticos
S_data = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0])
v_data = np.array([0.4, 0.7, 1.2, 1.8, 2.1, 2.3, 2.4])

# Otimização local (Gauss-Newton/LM) com chute inicial
params, cov = curve_fit(michaelis_menten, S_data, v_data, p0=[3.0, 5.0])
Vmax_fit, Km_fit = params

print(f"Vmax estimado = {Vmax_fit:.3f}")
print(f"Km estimado = {Km_fit:.3f}")
```

---

## Referências Principais
- Press W.H. et al. (2007). *Numerical Recipes: The Art of Scientific Computing*, 3rd ed. Cambridge.
- Bard Y. (1974). *Nonlinear Parameter Estimation*. Academic Press.
- Seber G.A.F., Wild C.J. (2003). *Nonlinear Regression*. Wiley.
- Gutenkunst R.N. et al. (2007). Universally sloppy parameter sensitivities in systems biology. *PLoS Computational Biology*.

---

## Exercícios Recomendados

1. **Busca em Grade 2D**: Implementar busca em grade para modelos simples de crescimento.
2. **Descida do Gradiente**: Escrever um código manual de Gradient Descent com cálculo de derivadas numéricas por diferenças finitas.
3. **Ajuste de Michaelis-Menten**: Estimar parâmetros cinéticos, extrair a matriz de covariância e calcular os intervalos de confiança assintóticos (95%).
4. **Otimização Global**: Comparar a performance de algoritmos globais (como Differential Evolution) e locais em funções com múltiplos mínimos locais.
5. **Crescimento Logístico**: Ajustar dados de crescimento bacteriano e avaliar a identificabilidade prática por correlação.
