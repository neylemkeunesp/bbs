#!/usr/bin/env python3
"""
gerar_capitulos.py
Gera capítulos LaTeX em prosa fluida a partir dos JSONs extraídos.
Estratégia: converte os marcadores %%FRAME/%%BLOCK/%%DEF/%%IMP em
parágrafos corridos, mantém equações/tikz/lstlistings com envoltura.
"""
import json, re, textwrap
from pathlib import Path

EXTRACTED = Path("/home/lemke/bbs/livro2/extracted")
OUT       = Path("/home/lemke/bbs/livro2/capitulos")
OUT.mkdir(parents=True, exist_ok=True)

# Metadados dos capítulos
CAPS = {
    "02": ("Modelagem Matemática", "cap02"),
    "03": ("Redes Estáticas e Teoria de Grafos", "cap03"),
    "04": ("A Matemática dos Sistemas Biológicos", "cap04"),
    "05": ("Estimação de Parâmetros", "cap05"),
    "06": ("Sistemas Gênicos", "cap06"),
    "07": ("Sistemas de Proteínas", "cap07"),
    "08": ("Sistemas Metabólicos", "cap08"),
    "09": ("Sistemas de Sinalização Celular", "cap09"),
    "10": ("Sistemas Populacionais e Epidemiologia", "cap10"),
    "11": ("Análise Integrada Multi-Ômica", "cap11"),
    "12": ("Fisiologia Cardíaca como Sistema de Controle", "cap12"),
    "13": ("Medicina de Sistemas", "cap13"),
    "14": ("Design de Sistemas Biológicos", "cap14"),
    "15": ("Tópicos Emergentes em Biologia de Sistemas", "cap15"),
}

def clean_text(t: str) -> str:
    """Remove marcadores de formatação e limpa o texto bruto."""
    # Substituir marcadores por separadores de parágrafo ou ignorar
    t = re.sub(r'%%FRAME:\s*', '\n\n', t)
    t = re.sub(r'%%BLOCK:\s*', '\n\n\\textbf{', t)
    # Fechar o \textbf aberto pelo %%BLOCK na próxima quebra dupla
    t = re.sub(r'(\\textbf\{[^\n]+)\n\n', r'\1}. ', t)
    t = re.sub(r'%%DEF:\s*([^\n]+)', r'\n\n\\textbf{Definição (\1).}', t)
    t = re.sub(r'%%IMP:\s*', '\n\nImportante: ', t)
    t = re.sub(r'%%DEST:\s*', '\n\n', t)
    t = re.sub(r'%%COLS\n|%%/COLS\n|%%COL\n', '\n\n', t)
    t = re.sub(r'%%BIB:\s*', '\n\n', t)
    # Limpar comandos LaTeX residuais no texto
    t = re.sub(r'\[\s*FIGURA\s*\]', '', t)
    t = re.sub(r'\[\s*TABELA\s*\]', '', t)
    t = re.sub(r'\$\$\s*', '$', t)
    t = re.sub(r'\\\\', ' ', t)
    t = re.sub(r'\\[a-zA-Z]+\b', '', t)
    t = re.sub(r'[\{\}]', '', t)
    # Limpar placeholders (serão reinseridos depois)
    # Limpar pontuação repetida
    t = re.sub(r'\.(\s*\.)+', '.', t)
    t = re.sub(r';\s*;', ';', t)
    # Normalizar espaços
    t = re.sub(r' {2,}', ' ', t)
    t = re.sub(r'\n{3,}', '\n\n', t)
    return t.strip()


def text_to_prose(raw: str, sec_title: str) -> str:
    """Converte texto semi-estruturado em prosa LaTeX fluida."""
    # Separar em blocos por dupla quebra de linha
    blocks = [b.strip() for b in raw.split('\n\n') if b.strip()]
    paragraphs = []
    for b in blocks:
        if not b:
            continue
        # Blocos que são fragmentos de lista (contém "; ") → converter
        if '; ' in b and not b.startswith('\\'):
            # Transformar lista semicolon em prosa
            items = [i.strip().rstrip('.') for i in b.split(';') if i.strip()]
            if len(items) > 1:
                # Juntar como enumeração em prosa
                if len(items) == 2:
                    b = f"{items[0]} e {items[1]}."
                else:
                    b = ', '.join(items[:-1]) + f' e {items[-1]}.'
        paragraphs.append(b)
    return '\n\n'.join(paragraphs)


def restore_math(text: str, equations: dict) -> str:
    for key, eq in equations.items():
        placeholder = f'[{key}]'
        if placeholder in text:
            text = text.replace(placeholder, f'\n{eq}\n')
    return text


def restore_tikz(text: str, tikz: dict, cap: str, sec: str) -> str:
    fig_counter = [0]
    for key, code in tikz.items():
        placeholder = f'[{key}]'
        if placeholder in text:
            fig_counter[0] += 1
            wrapped = (
                f'\n\\begin{{figure}}[htbp]\n'
                f'\\centering\n'
                f'\\begin{{tikzpicture}}\n'
                + re.sub(r'^\\begin\{tikzpicture\}[^\n]*\n?', '',
                          re.sub(r'\\end\{tikzpicture\}\s*$', '', code))
                + '\n\\end{tikzpicture}\n'
                f'\\caption{{Diagrama — {sec}.}}\n'
                f'\\end{{figure}}\n'
            )
            text = text.replace(placeholder, wrapped)
    return text


def restore_listings(text: str, listings: dict) -> str:
    for key, code in listings.items():
        placeholder = f'[{key}]'
        if placeholder in text:
            text = text.replace(placeholder, f'\n{code}\n')
    return text


def generate_chapter(num: str, title: str) -> str:
    json_path = EXTRACTED / f"cap{num}.json"
    if not json_path.exists():
        return f"\\chapter{{{title}}}\n\\label{{cap:{num}}}\n\nCapítulo em preparação.\n"

    data = json.loads(json_path.read_text(encoding='utf-8'))
    sections = data['sections']

    lines = [
        f"\\chapter{{{title}}}",
        f"\\label{{cap:{num}}}",
        "",
    ]

    for sec in sections:
        sec_title = sec['title']
        raw_text  = sec['text']
        equations = sec.get('equations', {})
        tikz      = sec.get('tikz', {})
        listings  = sec.get('listings', {})

        # Pular seções de título/sumário vazias
        if not raw_text.strip() or sec_title in ('', 'Introdução') and not raw_text.strip():
            continue

        # Adicionar heading de seção (exceto para intro que vem logo depois do chapter)
        if sec_title not in ('Introdução',):
            lines.append(f"\n\\section{{{sec_title}}}\n")
        else:
            lines.append("")

        # Limpar e converter para prosa
        cleaned = clean_text(raw_text)
        prose   = text_to_prose(cleaned, sec_title)

        # Restaurar elementos especiais
        prose = restore_math(prose, equations)
        prose = restore_tikz(prose, tikz, num, sec_title)
        prose = restore_listings(prose, listings)

        lines.append(prose)

    # Adicionar seção de exercícios placeholder
    lines.append("\n\\section{Exercícios}\n")
    lines.append("\\begin{exercicio}")
    lines.append(f"Descreva os principais conceitos apresentados neste capítulo sobre "
                 f"\\emph{{{title.lower()}}} e sua relevância para a Biologia de Sistemas.")
    lines.append("\\end{exercicio}")
    lines.append("")
    lines.append("\\begin{exercicio}")
    lines.append("Com base nas equações apresentadas, implemente em Python uma simulação "
                 "do modelo discutido e analise o comportamento para diferentes valores de parâmetros.")
    lines.append("\\end{exercicio}")

    lines.append("\n\\section{Notas Bibliográficas}\n")
    lines.append(f"Os conceitos de {title.lower()} aqui apresentados têm referências "
                 "fundamentais nas obras citadas ao longo do texto. Para aprofundamento, "
                 "recomenda-se consultar Alon (2007), \\textit{An Introduction to Systems Biology}; "
                 "Klipp et al.\\ (2009), \\textit{Systems Biology: A Textbook}; e os artigos "
                 "originais referenciados nos slides do curso.")

    return '\n'.join(lines) + '\n'


# Gerar caps 02–15
for num, (title, _) in CAPS.items():
    out_file = OUT / f"cap{num}.tex"
    if out_file.exists() and out_file.stat().st_size > 1000:
        print(f"[SKIP] cap{num} já existe ({out_file.stat().st_size} bytes)")
        continue
    content = generate_chapter(num, title)
    out_file.write_text(content, encoding='utf-8')
    print(f"[OK] cap{num}: {len(content):,} chars → {out_file.name}")

print("\nPronto!")
