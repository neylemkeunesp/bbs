#!/usr/bin/env python3
"""
prose_writer.py — Converte TEX Beamer em prosa LaTeX de livro.
Estratégia: extrai blocos de conteúdo semântico e os transcreve
como parágrafos fluidos, mantendo equações, tikz e código intactos.
"""
import re, sys, json
from pathlib import Path

def normalize(s): return s.replace('\r\n','\n').replace('\r','\n')

def get_body(tex):
    m = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', tex, re.DOTALL)
    return m.group(1) if m else tex

def protect_special(tex):
    """Protege equações, tikz e lstlisting em dicionários."""
    eq, tikz, lst = {}, {}, {}
    c = [0]
    def save(d, s, pfx):
        k = f'HOLD_{pfx}_{c[0]}'
        c[0] += 1; d[k] = s
        return f'HOLD_{pfx}_{c[0]-1}'
    tex = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',
                 lambda m: save(tikz, m.group(0), 'T'), tex, flags=re.DOTALL)
    tex = re.sub(r'\\begin\{lstlisting\}.*?\\end\{lstlisting\}',
                 lambda m: save(lst, m.group(0), 'L'), tex, flags=re.DOTALL)
    tex = re.sub(r'\\begin\{(equation\*?|align\*?|gather\*?|multline\*?)\}.*?\\end\{\1\}',
                 lambda m: save(eq, m.group(0), 'E'), tex, flags=re.DOTALL)
    return tex, eq, tikz, lst

def extract_frames(tex):
    """Extrai conteúdo dos frames, descartando slides de título/toc."""
    tex = re.sub(r'\\begin\{frame\}[^}]*\n\s*\\titlepage.*?\\end\{frame\}','',tex,flags=re.DOTALL)
    tex = re.sub(r'\\begin\{frame\}[^}]*\{Sumário\}.*?\\end\{frame\}','',tex,flags=re.DOTALL)
    def repl(m):
        title = (m.group(2) or '').strip()
        body  = (m.group(3) or '').strip()
        return f'\n\n{"=== " + title + " ===" if title else ""}\n{body}\n'
    tex = re.sub(r'\\begin\{frame\}(\[[^\]]*\])?\{([^}]*)\}(.*?)\\end\{frame\}',
                 repl, tex, flags=re.DOTALL)
    tex = re.sub(r'\\begin\{frame\}(\[[^\]]*\])?(.*?)\\end\{frame\}',
                 lambda m: '\n'+m.group(2).strip()+'\n', tex, flags=re.DOTALL)
    return tex

def unwrap_beamer_envs(tex):
    """Remove wrappers de block/exampleblock/alertblock preservando conteúdo."""
    for env in ('block','exampleblock','alertblock'):
        def repl(m):
            t, b = m.group(1).strip(), m.group(2).strip()
            return f'\n\n{"--- " + t + " ---" if t else ""}\n{b}\n\n'
        tex = re.sub(r'\\begin\{'+env+r'\}\{([^}]*)\}(.*?)\\end\{'+env+r'\}',
                     repl, tex, flags=re.DOTALL)
    tex = re.sub(r'\\definicao\{([^}]*)\}\{', lambda m: f'\n--- DEF: {m.group(1)} ---\n', tex)
    tex = re.sub(r'\\importante\{','--- IMP: ', tex)
    tex = re.sub(r'\\destaque\{','--- DEST: ', tex)
    return tex

def clean_latex(tex):
    """Remove comandos LaTeX mantendo o texto semântico."""
    tex = re.sub(r'\\begin\{columns\}(\[[^\]]*\])?', '', tex)
    tex = re.sub(r'\\end\{columns\}', '', tex)
    tex = re.sub(r'\\column\{[^}]+\}', '\n', tex)
    tex = re.sub(r'\\begin\{center\}(.*?)\\end\{center\}', r'\1', tex, flags=re.DOTALL)
    tex = re.sub(r'\\begin\{(?:minipage|tabular)[^}]*\}.*?\\end\{(?:minipage|tabular)\}',
                 '[TABELA]', tex, flags=re.DOTALL)
    tex = re.sub(r'\\item\s+', '- ', tex)
    tex = re.sub(r'\\begin\{(?:itemize|enumerate)\}', '', tex)
    tex = re.sub(r'\\end\{(?:itemize|enumerate)\}', '\n', tex)
    tex = re.sub(r'\\textbf\{([^}]*)\}', r'\\textbf{\1}', tex)  # manter
    tex = re.sub(r'\\emph\{([^}]*)\}', r'\\emph{\1}', tex)      # manter
    tex = re.sub(r'\\text(?:it|sc|rm|sf|tt)\{([^}]*)\}', r'\1', tex)
    tex = re.sub(r'\\(?:vspace|hspace)\*?\{[^}]*\}', ' ', tex)
    tex = re.sub(r'\\(?:vfill|hfill|centering|small|scriptsize|tiny|large|Large|LARGE|huge|Huge)\b', '', tex)
    tex = re.sub(r'\\includegraphics(\[[^\]]*\])?\{[^}]*\}', '[FIGURA]', tex)
    tex = re.sub(r'\\label\{[^}]*\}', '', tex)
    tex = re.sub(r'\\(?:pause|tableofcontents|titlepage)\b[^\n]*', '', tex)
    tex = re.sub(r'%[^\n]*', '', tex)
    tex = re.sub(r'\\[a-zA-Z]+\*?\{[^}]*\}', '', tex)
    tex = re.sub(r'\\[a-zA-Z]+\b', '', tex)
    tex = re.sub(r'\{|\}', '', tex)
    tex = re.sub(r'\[TABELA\]|\[FIGURA\]', '', tex)
    tex = re.sub(r'=== \s*===', '', tex)
    tex = re.sub(r'\n{3,}', '\n\n', tex)
    return tex.strip()

def process(src_path):
    tex = normalize(Path(src_path).read_text(encoding='utf-8', errors='replace'))
    tex = get_body(tex)
    tex, eq, tikz, lst = protect_special(tex)
    tex = extract_frames(tex)
    tex = unwrap_beamer_envs(tex)
    
    # Separar por \section{}
    sections = re.split(r'(\\section\{[^}]*\})', tex)
    
    result = {'sections': [], 'eq': eq, 'tikz': tikz, 'lst': lst}
    
    # intro antes da primeira section
    if sections[0].strip():
        raw = clean_latex(sections[0])
        result['sections'].append({'title': None, 'raw': raw})
    
    i = 1
    while i < len(sections) - 1:
        sec_cmd = sections[i]
        body = sections[i+1] if i+1 < len(sections) else ''
        title = re.search(r'\\section\{([^}]*)\}', sec_cmd)
        title = title.group(1) if title else 'Seção'
        raw = clean_latex(body)
        result['sections'].append({'title': title, 'raw': raw})
        i += 2
    
    return result

if __name__ == '__main__':
    src = sys.argv[1]
    data = process(src)
    print(json.dumps(data, ensure_ascii=False, indent=2))
