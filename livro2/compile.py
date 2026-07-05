#!/usr/bin/env python3
"""
compile_livro2.py — Compila o livro clássico (livro2) após os subagentes
entregarem os capítulos reescritos.

Verifica capítulos presentes, cria placeholders para os ausentes,
copia imagens, e executa pdflatex 3×.
"""
import subprocess
import sys
from pathlib import Path

LIVRO2 = Path("/home/lemke/bbs/livro2")
CAPS_DIR = LIVRO2 / "capitulos"
CAPS_DIR.mkdir(parents=True, exist_ok=True)

# Capítulos esperados
EXPECTED = [f"cap{i:02d}.tex" for i in range(1, 16)]

def check_caps():
    present, missing = [], []
    for cap in EXPECTED:
        f = CAPS_DIR / cap
        if f.exists() and f.stat().st_size > 500:
            present.append(cap)
        else:
            missing.append(cap)
    return present, missing

def create_placeholder(cap_name: str):
    """Cria capítulo placeholder para compilar sem erros."""
    num = cap_name.replace("cap", "").replace(".tex", "")
    content = (
        f"\\chapter{{Capítulo {num} — Em preparação}}\n"
        f"\\label{{cap:{num}}}\n\n"
        "Este capítulo está sendo revisado e será incluído na próxima versão.\n"
    )
    path = CAPS_DIR / cap_name
    path.write_text(content, encoding='utf-8')
    print(f"  [placeholder] {cap_name}")

def copy_images():
    img_dst = LIVRO2 / "images"
    img_dst.mkdir(exist_ok=True)
    img_src = Path("/home/lemke/bbs/images")
    for f in img_src.glob("*.png"):
        dst = img_dst / f.name
        if not dst.exists():
            import shutil
            shutil.copy(f, dst)

    # Criar placeholders para imagens referenciadas mas ausentes
    needed = [
        "biological_hierarchy_infographic_landscape.png",
        "diagrama_modelagem.png",
        "protein_structure_infographic.png",
        "ramachandran_infographic.png",
    ]
    for img in needed:
        dst = img_dst / img
        if not dst.exists():
            # Copiar do livro1 se existir
            src1 = Path("/home/lemke/bbs/livro/images") / img
            if src1.exists():
                import shutil
                shutil.copy(src1, dst)
            else:
                # Criar placeholder mínimo
                subprocess.run([
                    "convert", "-size", "300x200", "xc:#f0f0f0",
                    "-fill", "#333333", "-pointsize", "14",
                    "-gravity", "Center",
                    "-annotate", "+0+0", f"[{img}]",
                    str(dst)
                ], capture_output=True)

def pdflatex(extra_args=None):
    cmd = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error"]
    if extra_args:
        cmd += extra_args
    cmd.append("main.tex")
    result = subprocess.run(cmd, cwd=LIVRO2, capture_output=True, text=True)
    return result.returncode, result.stdout + result.stderr

def main():
    print("=" * 60)
    print("COMPILADOR — Bioinformática para Biologia de Sistemas v2")
    print("=" * 60)

    present, missing = check_caps()
    print(f"\nCapítulos presentes : {len(present)}/15")
    print(f"Capítulos ausentes  : {len(missing)}")

    if missing:
        print("\nCriando placeholders para capítulos ausentes:")
        for cap in missing:
            create_placeholder(cap)

    print("\nCopiando imagens...")
    copy_images()

    print("\nCompilando (passagem 1/3)...")
    rc, out = pdflatex()
    errors = [l for l in out.splitlines() if l.startswith("!")]
    if errors:
        print(f"  Erros: {len(errors)}")
        for e in errors[:5]:
            print(f"    {e}")
    else:
        print("  OK — sem erros fatais")

    print("Compilando (passagem 2/3)...")
    rc, out = pdflatex()

    print("Compilando (passagem 3/3)...")
    rc, out = pdflatex()

    pdf = LIVRO2 / "main.pdf"
    if pdf.exists():
        size = pdf.stat().st_size / 1024 / 1024
        # Contar páginas
        r = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
        pages = "?"
        for line in r.stdout.splitlines():
            if line.startswith("Pages:"):
                pages = line.split()[-1]
        print(f"\n✓ PDF gerado: {pdf}")
        print(f"  Tamanho : {size:.1f} MB")
        print(f"  Páginas : {pages}")
        # Copiar para nome final
        dst = LIVRO2 / "bbs-livro-classico.pdf"
        import shutil
        shutil.copy(pdf, dst)
        print(f"  Saída   : {dst}")
    else:
        print("\n✗ PDF não gerado — verificar main.log")
        sys.exit(1)

if __name__ == "__main__":
    main()
