#!/usr/bin/env python3
import sys
import re
import os
from typing import List, Dict, Any, Tuple

def parse_log(log_path: str) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Analisa o log em busca de overfull boxes."""
    overfull_vbox: List[Dict[str, Any]] = []
    overfull_hbox: List[Dict[str, Any]] = []
    
    if not os.path.exists(log_path):
        return overfull_vbox, overfull_hbox

    # Regex para capturar Overfull \vbox e \hbox
    vbox_pattern = re.compile(r'Overfull \\vbox \(([^)]+)\) detected at line (\d+)')
    hbox_pattern = re.compile(r'Overfull \\hbox \(([^)]+)\) detected at line (\d+)')
    
    try:
        with open(log_path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
            
            for match in vbox_pattern.finditer(content):
                overfull_vbox.append({'size': match.group(1), 'line': int(match.group(2))})
            
            for match in hbox_pattern.finditer(content):
                overfull_hbox.append({'size': match.group(1), 'line': int(match.group(2))})
    except Exception as e:
        print(f"Erro ao ler log: {e}")
        
    return overfull_vbox, overfull_hbox

def analyze_tex(tex_path: str) -> List[Dict[str, Any]]:
    """Analisa o arquivo .tex em busca de frames longos."""
    frames: List[Dict[str, Any]] = []
    try:
        with open(tex_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Erro ao ler tex: {e}")
        return []

    current_frame: Dict[str, Any] = {}
    in_frame = False
    
    for i, line in enumerate(lines):
        lnum = i + 1
        stripped = line.strip()
        
        # Início de frame
        match_start = re.search(r'\\begin\{frame\}(?:\[[^\]]*\])?(?:\{([^}]*)\})?', stripped)
        if match_start:
            title = match_start.group(1) or "Sem título"
            current_frame = {
                'start': int(lnum), 
                'end': int(lnum), 
                'title': str(title), 
                'content_lines': int(0), 
                'blocks': int(0)
            }
            in_frame = True
            continue
            
        # Fim de frame
        if '\\end{frame}' in stripped and in_frame:
            current_frame['end'] = int(lnum)
            frames.append(current_frame)
            in_frame = False
            continue
            
        if in_frame:
            if stripped and not stripped.startswith('%'):
                current_frame['content_lines'] = int(current_frame['content_lines']) + 1
                if any(x in stripped for x in ['\\begin{block}', '\\begin{alertblock}', '\\begin{exampleblock}']):
                    current_frame['blocks'] = int(current_frame['blocks']) + 1
                    
    return frames

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 beamer_guard.py <arquivo.tex>")
        sys.exit(1)
        
    tex_path = sys.argv[1]
    log_path = os.path.splitext(tex_path)[0] + '.log'
    
    print(f"--- ANALISANDO: {tex_path} ---")
    
    frames = analyze_tex(tex_path)
    overfull_vbox, overfull_hbox = parse_log(log_path)
    
    issues = 0
    
    # 1. Verificar logs (mais preciso para corte de texto)
    if overfull_vbox:
        print("\n🚨 TEXTO CORTADO VERTICALMENTE (Overfull \\vbox):")
        for error in overfull_vbox:
            err_line = int(error['line'])
            frame_title = "Desconhecido"
            for f in frames:
                if int(f['start']) <= err_line <= int(f['end']):
                    frame_title = str(f['title'])
                    break
            print(f" - Linha {err_line} (Slide: {frame_title}): Excesso de {error['size']}")
            issues += 1
            
    if overfull_hbox:
        print("\n⚠️ TEXTO ULTRAPASSANDO LATERAL (Overfull \\hbox):")
        for error in overfull_hbox:
            err_line = int(error['line'])
            frame_title = "Desconhecido"
            for f in frames:
                if int(f['start']) <= err_line <= int(f['end']):
                    frame_title = str(f['title'])
                    break
            print(f" - Linha {err_line} (Slide: {frame_title}): Excesso de {error['size']}")
            issues += 1

    # 2. Heurística de densidade
    print("\n📊 ANÁLISE DE DENSIDADE (Heurística):")
    for f in frames:
        c_lines = int(f['content_lines'])
        c_blocks = int(f['blocks'])
        if c_lines > 12:
            print(f" - Slide '{f['title']}' (linhas {f['start']}-{f['end']}): Muito denso ({c_lines} linhas). Considere dividir.")
            issues += 1
        elif c_blocks > 3:
            print(f" - Slide '{f['title']}' (linhas {f['start']}-{f['end']}): Muitos blocos ({c_blocks}). Considere simplificar.")
            issues += 1

    if issues == 0:
        print("\n✅ Nenhum problema grave detectado. Os slides parecem ok!")
    else:
        print(f"\nTotal de problemas sugeridos: {issues}")
        print("\nDica: Use [allowframebreaks] ou divida os slides manualmente.")

if __name__ == "__main__":
    main()
