#!/usr/bin/env python3
"""
build_all.py — Gera todos os capítulos do livro2 em LaTeX prosa limpo.
Lê os JSONs extraídos por prose_writer.py e produz arquivos .tex 
usando prosa fluida, sem caixas, com equações/tikz/código intactos.
"""
import json, re, subprocess, sys
from pathlib import Path

CAPS_DIR  = Path('/home/lemke/bbs/capitulos')
OUT_DIR   = Path('/home/lemke/bbs/livro2/capitulos')
WRITER    = Path('/home/lemke/bbs/livro2/prose_writer.py')
OUT_DIR.mkdir(parents=True, exist_ok=True)

METAS = {
    '02': 'Modelagem Matemática',
    '03': 'Redes Estáticas e Teoria de Grafos',
    '05': 'Estimação de Parâmetros',
    '06': 'Sistemas Gênicos',
    '07': 'Sistemas de Proteínas',
    '08': 'Sistemas Metabólicos',
    '09': 'Sistemas de Sinalização Celular',
    '10': 'Sistemas Populacionais e Epidemiologia',
    '11': 'Análise Integrada Multi-Ômica',
    '12': 'Fisiologia Cardíaca como Sistema de Controle',
    '13': 'Medicina de Sistemas',
    '14': 'Design de Sistemas Biológicos',
    '15': 'Tópicos Emergentes em Biologia de Sistemas',
}

SRCS = {
    '02': 'capitulo02-modelagem-matematica.tex',
    '03': 'capitulo03-static-networks.tex',
    '05': 'capitulo05-parameter-estimation.tex',
    '06': 'capitulo06-sistemas-genicos.tex',
    '07': 'capitulo07-protein-systems.tex',
    '08': 'capitulo08-metabolic-systems.tex',
    '09': 'capitulo09-signaling-systems.tex',
    '10': 'capitulo10-population-systems.tex',
    '11': 'capitulo11-integrated-analysis.tex',
    '12': 'capitulo12-heart-physiology.tex',
    '13': 'capitulo13-medicine.tex',
    '14': 'capitulo14-design-systems.tex',
    '15': 'capitulo15-emerging-topics.tex',
}


def items_to_prose(text: str) -> str:
    """
    Converte linhas de bullet "- item" em prosa fluida.
    Conecta os itens com vírgulas/pontos e vírgulas.
    """
    lines = text.split('\n')
    bullets, prose_lines = [], []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('- '):
            bullets.append(stripped[2:].strip().rstrip('.').rstrip(';'))
        else:
            if bullets:
                if len(bullets) == 1:
                    prose_lines.append(bullets[0] + '.')
                elif len(bullets) == 2:
                    prose_lines.append(bullets[0] + ' e ' + bullets[1] + '.')
                else:
                    joined = ', '.join(bullets[:-1]) + ' e ' + bullets[-1] + '.'
                    prose_lines.append(joined)
                bullets = []
            if stripped:
                prose_lines.append(line)
    
    if bullets:
        if len(bullets) == 1:
            prose_lines.append(bullets[0] + '.')
        else:
            prose_lines.append(', '.join(bullets[:-1]) + ' e ' + bullets[-1] + '.')
    
    return '\n\n'.join(p for p in prose_lines if p.strip())


def clean_section_text(raw: str) -> str:
    """Limpa marcadores residuais e formata como prosa."""
    # Marcadores estruturais viram separadores de parágrafo
    raw = re.sub(r'=== ([^=\n]+) ===', r'\n\n\\textbf{\1.}', raw)
    raw = re.sub(r'--- DEF: ([^\n-]+) ---', r'\n\n\\textbf{Definição (\1).}', raw)
    raw = re.sub(r'--- IMP: ([^\n]+)---', r'\n\nImportante: \1', raw)
    raw = re.sub(r'--- DEST: ([^\n]+)', r'\n\n\1', raw)
    raw = re.sub(r'--- ([^\n-]+) ---', r'\n\n\1', raw)
    
    # Limpar artefatos
    raw = re.sub(r'\bHOLD_[A-Z]_\d+\b', lambda m: f'%{m.group(0)}%', raw)  # preservar
    raw = re.sub(r'TABELA|FIGURA', '', raw)
    
    # Converter bullets em prosa
    raw = items_to_prose(raw)
    
    # Limpeza final
    raw = re.sub(r'\n{3,}', '\n\n', raw)
    raw = re.sub(r'[ \t]+', ' ', raw)
    return raw.strip()


def restore_specials(text: str, eq: dict, tikz: dict, lst: dict) -> str:
    """Reinsere equações, TikZ e listagens com envoltura de livro."""
    # Restaurar equações
    for k, v in eq.items():
        if k in text:
            text = text.replace(k, f'\n{v}\n')
    
    # Restaurar tikz em figure
    fig_n = [0]
    for k, v in tikz.items():
        if k in text:
            fig_n[0] += 1
            # Extrair apenas o corpo do tikzpicture
            inner = re.sub(r'^\\begin\{tikzpicture\}[^\n]*\n?', '', v)
            inner = re.sub(r'\\end\{tikzpicture\}\s*$', '', inner)
            wrapped = (
                '\n\\begin{figure}[htbp]\n'
                '\\centering\n'
                '\\begin{tikzpicture}\n'
                + inner.strip() +
                '\n\\end{tikzpicture}\n'
                '\\caption{Diagrama esquemático.}\n'
                '\\end{figure}\n'
            )
            text = text.replace(k, wrapped)
    
    # Restaurar lstlisting
    for k, v in lst.items():
        if k in text:
            text = text.replace(k, f'\n{v}\n')
    
    # Remover placeholders não restaurados
    text = re.sub(r'%HOLD_[A-Z]_\d+%', '', text)
    return text


def build_chapter(num: str, title: str, src_name: str) -> str:
    """Pipeline completo: TEX bruto → LaTeX de livro."""
    src = CAPS_DIR / src_name
    if not src.exists():
        return f'\\chapter{{{title}}}\n\\label{{cap:{num}}}\n\nCapítulo em preparação.\n'
    
    # Extrair dados via prose_writer
    r = subprocess.run(
        ['python3', str(WRITER), str(src)],
        capture_output=True, text=True, timeout=30
    )
    if r.returncode != 0 or not r.stdout.strip():
        return f'\\chapter{{{title}}}\n\\label{{cap:{num}}}\n\nErro na extração.\n'
    
    data = json.loads(r.stdout)
    sections = data['sections']
    eq   = data['eq']
    tikz = data['tikz']
    lst  = data['lst']
    
    lines = [f'\\chapter{{{title}}}', f'\\label{{cap:{num}}}', '']
    
    for sec in sections:
        sec_title = sec.get('title')
        raw = sec.get('raw', '')
        
        if not raw.strip():
            continue
        
        if sec_title and sec_title not in ('Referências', 'Exercícios'):
            lines.append(f'\n\\section{{{sec_title}}}\n')
        elif sec_title == 'Exercícios':
            lines.append('\n\\section{Exercícios}\n')
        elif sec_title == 'Referências':
            lines.append('\n\\section{Notas Bibliográficas}\n')
        
        prose = clean_section_text(raw)
        prose = restore_specials(prose, eq, tikz, lst)
        lines.append(prose)
    
    # Garantir seção de exercícios
    content = '\n'.join(lines)
    if '\\section{Exercícios}' not in content:
        content += (
            '\n\n\\section{Exercícios}\n\n'
            '\\begin{exercicio}\n'
            f'Discuta os principais conceitos de \\emph{{{title.lower()}}} '
            'apresentados neste capítulo e suas conexões com os demais módulos do curso.\n'
            '\\end{exercicio}\n\n'
            '\\begin{exercicio}\n'
            'Implemente em Python um dos modelos discutidos neste capítulo e analise '
            'o comportamento do sistema para diferentes valores de parâmetros.\n'
            '\\end{exercicio}\n'
        )
    
    return content + '\n'


# Gerar todos os capítulos configurados
for num, title in METAS.items():
    out = OUT_DIR / f'cap{num}.tex'
    src = SRCS[num]
    print(f'Gerando cap{num}: {title}...', end=' ', flush=True)
    try:
        content = build_chapter(num, title, src)
        out.write_text(content, encoding='utf-8')
        nlines = content.count('\n')
        print(f'OK ({nlines} linhas)')
    except Exception as e:
        print(f'ERRO: {e}')

print('\nConcluído!')
