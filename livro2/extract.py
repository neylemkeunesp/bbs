#!/usr/bin/env python3
"""
extract.py — Extrai o conteúdo semântico dos TEX Beamer em estrutura Python.

Retorna por capítulo:
  - sections: lista de {title, subsections: [{title, content_blocks}]}
  - equations: todas as equações
  - lstlistings: todos os blocos de código
  - tikz_blocks: todos os TikZ
  - biblio: \bibitem entries
"""

import re
import sys
from pathlib import Path


def normalize(tex: str) -> str:
    return tex.replace('\r\n', '\n').replace('\r', '\n')


def extract_body(tex: str) -> str:
    m = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', tex, re.DOTALL)
    return m.group(1) if m else tex


def strip_beamer_meta(tex: str) -> str:
    """Remove comandos de metadados e controle do Beamer."""
    # titlepage, tableofcontents, pause, only, etc.
    tex = re.sub(r'\\(titlepage|tableofcontents|pause)\b[^\n]*', '', tex)
    tex = re.sub(r'\\only<[^>]*>\{[^}]*\}', '', tex)
    tex = re.sub(r'\\uncover<[^>]*>\{([^}]*)\}', r'\1', tex)
    tex = re.sub(r'\\visible<[^>]*>\{([^}]*)\}', r'\1', tex)
    tex = re.sub(r'\\alert<[^>]*>\{([^}]*)\}', r'\1', tex)
    tex = re.sub(r'\\alert\{([^}]*)\}', r'\\textbf{\1}', tex)
    tex = re.sub(r'\\frametitle(\[[^\]]*\])?\{[^}]*\}', '', tex)
    tex = re.sub(r'\\framesubtitle\{[^}]*\}', '', tex)
    tex = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}', '', tex)
    tex = re.sub(r'\\vspace\*?\{[^}]*\}', ' ', tex)
    tex = re.sub(r'\\hspace\*?\{[^}]*\}', ' ', tex)
    tex = re.sub(r'\\vfill\b', '', tex)
    tex = re.sub(r'\\hfill\b', '', tex)
    tex = re.sub(r'\\centering\b', '', tex)
    tex = re.sub(r'\\small\b', '', tex)
    tex = re.sub(r'\\scriptsize\b', '', tex)
    tex = re.sub(r'\\tiny\b', '', tex)
    tex = re.sub(r'\\large\b', '', tex)
    tex = re.sub(r'\\Large\b', '', tex)
    tex = re.sub(r'\\LARGE\b', '', tex)
    tex = re.sub(r'\\huge\b', '', tex)
    tex = re.sub(r'\\Huge\b', '', tex)
    tex = re.sub(r'\\textwidth\b', '', tex)
    tex = re.sub(r'%[^\n]*', '', tex)   # comentários
    return tex


def extract_sections(tex: str) -> list:
    """Divide o corpo em seções."""
    # Dividir por \section{}
    parts = re.split(r'(\\section\{[^}]*\})', tex)
    sections = []
    intro = parts[0] if parts else ''
    if intro.strip():
        sections.append({'title': 'Introdução', 'body': intro})
    i = 1
    while i < len(parts) - 1:
        sec_cmd = parts[i]
        body = parts[i + 1] if i + 1 < len(parts) else ''
        title = re.search(r'\\section\{([^}]*)\}', sec_cmd)
        title = title.group(1) if title else 'Seção'
        sections.append({'title': title, 'body': body})
        i += 2
    return sections


def extract_frames_content(body: str) -> str:
    """Extrai o conteúdo textual dos frames, removendo os wrappers."""

    # Remover frames de título/sumário
    body = re.sub(
        r'\\begin\{frame\}(\[[^\]]*\])?\s*\n?\s*\\titlepage[^\\]*\\end\{frame\}',
        '', body, flags=re.DOTALL
    )
    body = re.sub(
        r'\\begin\{frame\}(\[[^\]]*\])?\{Sumário\}.*?\\end\{frame\}',
        '', body, flags=re.DOTALL
    )

    # Frames com título: guardar título como comentário marcador
    def frame_with_title(m):
        title = (m.group(2) or '').strip()
        content = (m.group(3) or '').strip()
        if title:
            return f'\n%%FRAME: {title}\n{content}\n'
        return f'\n{content}\n'

    body = re.sub(
        r'\\begin\{frame\}(\[[^\]]*\])?\{([^}]*)\}(.*?)\\end\{frame\}',
        frame_with_title, body, flags=re.DOTALL
    )
    body = re.sub(
        r'\\begin\{frame\}(\[[^\]]*\])?(.*?)\\end\{frame\}',
        lambda m: '\n' + (m.group(2) or '').strip() + '\n',
        body, flags=re.DOTALL
    )
    return body


def extract_text_content(body: str) -> dict:
    """Extrai texto semântico, equações, código e TikZ separadamente."""

    # Proteger blocos especiais (substituir por placeholders)
    equations = {}
    tikz_blocks = {}
    lst_blocks = {}
    counter = [0]

    def protect(d, content, prefix='X'):
        key = f'PLACEHOLDER_{prefix}_{counter[0]}'
        counter[0] += 1
        d[key] = content
        return f' [{key}] '

    # TikZ
    body = re.sub(
        r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',
        lambda m: protect(tikz_blocks, m.group(0), 'TIKZ'),
        body, flags=re.DOTALL
    )
    # lstlisting
    body = re.sub(
        r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}',
        lambda m: protect(lst_blocks, m.group(0), 'LST'),
        body, flags=re.DOTALL
    )
    # equation / align / gather
    body = re.sub(
        r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}',
        lambda m: protect(equations, m.group(0), 'EQ'),
        body, flags=re.DOTALL
    )
    # displaymath $$...$$
    body = re.sub(
        r'\$\$.*?\$\$',
        lambda m: protect(equations, m.group(0), 'EQ'),
        body, flags=re.DOTALL
    )

    return {
        'body': body,
        'equations': equations,
        'tikz': tikz_blocks,
        'listings': lst_blocks,
    }


def clean_block_commands(body: str) -> str:
    """Remove wrappers de blocos Beamer mantendo o conteúdo."""

    def unwrap_block(m):
        title = m.group(1) or ''
        content = m.group(2) or ''
        if title.strip():
            return f'\n%%BLOCK: {title.strip()}\n{content.strip()}\n'
        return f'\n{content.strip()}\n'

    for env in ('block', 'exampleblock', 'alertblock'):
        body = re.sub(
            r'\\begin\{' + env + r'\}\{([^}]*)\}(.*?)\\end\{' + env + r'\}',
            unwrap_block, body, flags=re.DOTALL
        )

    # definicao{título}{corpo} → marcador + corpo
    body = re.sub(
        r'\\definicao\{([^}]*)\}\{(.*?)\}(?=\s*\\)',
        lambda m: f'\n%%DEF: {m.group(1)}\n{m.group(2)}\n',
        body, flags=re.DOTALL
    )
    body = re.sub(
        r'\\definicao\{([^}]*)\}\{',
        lambda m: f'\n%%DEF: {m.group(1)}\n',
        body
    )

    # importante{corpo}
    body = re.sub(
        r'\\importante\{(.*?)\}(?=\s*(?:\\|$))',
        lambda m: f'\n%%IMP: {m.group(1)}\n',
        body, flags=re.DOTALL
    )

    # destaque{corpo}
    body = re.sub(
        r'\\destaque\{(.*?)\}',
        lambda m: f'\n%%DEST: {m.group(1)}\n',
        body, flags=re.DOTALL
    )

    # columns/column → separador
    body = re.sub(r'\\begin\{columns\}(\[[^\]]*\])?', '\n%%COLS\n', body)
    body = re.sub(r'\\end\{columns\}', '\n%%/COLS\n', body)
    body = re.sub(r'\\column\{[^}]+\}', '\n%%COL\n', body)

    return body


def items_to_text(body: str) -> str:
    """Extrai texto de itens itemize/enumerate."""
    def itemize_repl(m):
        content = m.group(1)
        items = re.findall(r'\\item\s+(.*?)(?=\\item|$)', content, re.DOTALL)
        items = [i.strip().replace('\n', ' ') for i in items if i.strip()]
        return '\n' + '; '.join(items) + '.\n'

    body = re.sub(
        r'\\begin\{(?:itemize|enumerate)\}(.*?)\\end\{(?:itemize|enumerate)\}',
        itemize_repl, body, flags=re.DOTALL
    )
    return body


def clean_latex_commands(body: str) -> str:
    """Remove comandos LaTeX residuais, mantendo o texto."""
    body = re.sub(r'\\textbf\{([^}]*)\}', r'\1', body)
    body = re.sub(r'\\emph\{([^}]*)\}', r'\1', body)
    body = re.sub(r'\\textit\{([^}]*)\}', r'\1', body)
    body = re.sub(r'\\textsc\{([^}]*)\}', r'\1', body)
    body = re.sub(r'\\text\{([^}]*)\}', r'\1', body)
    body = re.sub(r'\\begin\{center\}(.*?)\\end\{center\}', r'\1', body, flags=re.DOTALL)
    body = re.sub(r'\\begin\{minipage\}[^{]*\{[^}]*\}(.*?)\\end\{minipage\}', r'\1', body, flags=re.DOTALL)
    body = re.sub(r'\\includegraphics(\[[^\]]*\])?\{[^}]*\}', '[FIGURA]', body)
    body = re.sub(r'\\label\{[^}]*\}', '', body)
    body = re.sub(r'\\ref\{[^}]*\}', '', body)
    body = re.sub(r'\\cite\{[^}]*\}', '', body)
    body = re.sub(r'\\bibitem[^{]*\{[^}]*\}', '\n%%BIB: ', body)
    body = re.sub(r'\\begin\{tabular\}.*?\\end\{tabular\}', '[TABELA]', body, flags=re.DOTALL)
    body = re.sub(r'\\toprule|\\midrule|\\bottomrule|\\hline', '', body)
    body = re.sub(r'\\[a-zA-Z]+\*?\{[^}]*\}', '', body)
    body = re.sub(r'\\[a-zA-Z]+\b', '', body)
    body = re.sub(r'[\{\}]', '', body)
    body = re.sub(r'\[([A-Z_]+_\d+)\]', r'[\1]', body)  # reproteger placeholders
    body = re.sub(r'\n\s*\n\s*\n', '\n\n', body)
    return body.strip()


def process_chapter(tex_path: Path) -> dict:
    """Pipeline completo de extração."""
    tex = tex_path.read_text(encoding='utf-8')
    tex = normalize(tex)
    body = extract_body(tex)
    body = strip_beamer_meta(body)
    body = extract_frames_content(body)
    body = clean_block_commands(body)

    sections = extract_sections(body)
    result_sections = []
    for sec in sections:
        sec_body = sec['body']
        extracted = extract_text_content(sec_body)
        sec_body2 = items_to_text(extracted['body'])
        sec_body3 = clean_latex_commands(sec_body2)
        result_sections.append({
            'title': sec['title'],
            'text': sec_body3,
            'equations': extracted['equations'],
            'tikz': extracted['tikz'],
            'listings': extracted['listings'],
        })

    return {
        'path': str(tex_path),
        'sections': result_sections,
    }


if __name__ == '__main__':
    caps = [
        ('capitulo01-sistemas-biologicos.tex', '01'),
        ('capitulo02-modelagem-matematica.tex', '02'),
        ('capitulo03-static-networks.tex', '03'),
        ('capitulo04-mathematics.tex', '04'),
        ('capitulo05-parameter-estimation.tex', '05'),
        ('capitulo06-sistemas-genicos.tex', '06'),
        ('capitulo07-protein-systems.tex', '07'),
        ('capitulo08-metabolic-systems.tex', '08'),
        ('capitulo09-signaling-systems.tex', '09'),
        ('capitulo10-population-systems.tex', '10'),
        ('capitulo11-integrated-analysis.tex', '11'),
        ('capitulo12-heart-physiology.tex', '12'),
        ('capitulo13-medicine.tex', '13'),
        ('capitulo14-design-systems.tex', '14'),
        ('capitulo15-emerging-topics.tex', '15'),
    ]
    caps_dir = Path('/home/lemke/bbs/capitulos')
    out_dir = Path('/home/lemke/bbs/livro2/extracted')
    out_dir.mkdir(parents=True, exist_ok=True)

    import json
    for fname, num in caps:
        src = caps_dir / fname
        if not src.exists():
            print(f"[SKIP] {fname}")
            continue
        data = process_chapter(src)
        out = out_dir / f'cap{num}.json'
        out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        total_text = sum(len(s['text']) for s in data['sections'])
        n_eq = sum(len(s['equations']) for s in data['sections'])
        n_tikz = sum(len(s['tikz']) for s in data['sections'])
        n_lst = sum(len(s['listings']) for s in data['sections'])
        print(f"[OK] cap{num}: {len(data['sections'])} seções, {total_text} chars texto, {n_eq} eq, {n_tikz} tikz, {n_lst} lst")
