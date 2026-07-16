#!/usr/bin/env python3
"""
fix_orphan_dollars.py — Corrige $$ órfãos comuns extraídos do Beamer.

Após extração dos arquivos Beamer, alguns placeholders %%DEST: e macros
foram convertidos em $$ (sem nada entre eles). Estes quebram o LaTeX
como 'Missing $ inserted' ou 'Display math should end with $$'.

Estratégia: padrões órfãos são substituídos por sentinelas legítimas
($\lambda$, $\beta$, $\mu$, etc.) ou removidos quando não há contexto.

Uso: python3 fix_orphan_dollars.py [arquivo.tex ...]
"""
import sys, re
from pathlib import Path

# Padrões órfãos comuns: (regex, substituição, descrição)
FIXES = [
    # "campo elétrico $$" → "campo elétrico $E$"
    (r'campo elétrico \$\$', r'campo elétrico $E$', 'campo elétrico → E'),
    # "matriz Jacobiana:" após $$
    (r'onde \$\$ é a matriz Jacobiana',
     r'onde $\\mathbf{J}(\\vect{x}^*)$ é a matriz Jacobiana',
     'Jacobiana'),
    # "$$ instável" / "$$ estável" → \Rightarrow
    (r'\$ \$([a-záéíóú]+)\.', r'$\\Rightarrow$ \1.', '$$ → \\Rightarrow'),
    # Variável de estado: $N_0$ = ... $$ = vetor ...
    (r'\$\$ = vetor de variáveis de estado, \$t = tempo, \$\$ = vetor de parâmetros e \$\$ = função',
     r'$\\vect{x} = $ vetor de variáveis de estado, $t = $ tempo, $\\vect{p} = $ vetor de parâmetros e $\\vect{f} = $ função',
     'EDO blocos'),
    # "Taxa de predação $$ encontros"
    (r'Taxa de predação \$\$ encontros', r'Taxa de predação $\\beta$ encontros', 'predação'),
    # "é a constante de decaimento"
    (r'onde \$N_0 = N\(0\)\$ é a condição inicial e \$\$ é a constante',
     r'onde $N_0 = N(0)$ é a condição inicial e $\\lambda$ é a constante',
     'constante decaimento'),
    # "Determine $$ necessária para controle"
    (r'Determine \$\$ necessária para controle',
     r'Determine $\\nu$ necessária para controle',
     'nu vacinação'),
]

def fix_file(path: Path) -> int:
    text = path.read_text(encoding='utf-8')
    original = text
    fixes_applied = []
    for pattern, replacement, desc in FIXES:
        new_text = re.sub(pattern, replacement, text)
        if new_text != text:
            count = text.count('$$') - new_text.count('$$')  # approximate
            text = new_text
            fixes_applied.append(desc)
    if text != original:
        path.write_text(text, encoding='utf-8')
        return len(fixes_applied)
    return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        cap_dir = Path(__file__).parent / 'capitulos'
        files = sorted(cap_dir.glob('cap*.tex'))
    else:
        files = [Path(f) for f in sys.argv[1:]]
    total_fixed = 0
    for f in files:
        n = fix_file(f)
        if n:
            print(f"  {f.name}: {n} fix(es)")
            total_fixed += n
    print(f"Total: {total_fixed} fix(es)")