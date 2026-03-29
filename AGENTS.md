# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Common commands

- Compile a single chapter (fast, two passes for refs):
  ```bash
  pdflatex -interaction=nonstopmode -halt-on-error capitulos/capitulo01-sistemas-biologicos.tex
  pdflatex -interaction=nonstopmode -halt-on-error capitulos/capitulo01-sistemas-biologicos.tex
  ```

- Compile with latexmk (handles required passes automatically):
  ```bash
  latexmk -pdf capitulos/capitulo01-sistemas-biologicos.tex
  ```

- Watch mode while editing (auto-recompile on save):
  ```bash
  latexmk -pdf -pvc capitulos/capitulo01-sistemas-biologicos.tex
  ```

- Batch-compile all chapters and summarize results (uses pdflatex twice per file):
  ```bash
  ./compile_all.sh
  ```

- Quick sanity compile of sample slides (useful for environment checks):
  ```bash
  pdflatex -interaction=nonstopmode -halt-on-error test_slide.tex
  pdflatex -interaction=nonstopmode -halt-on-error test_tikz_demo.tex
  ```

- Layout/overflow analysis for Beamer slides (detect frames with text overflow, etc.):
  ```bash
  python3 .agent/skills/beamer_layout_guard/scripts/beamer_guard.py capitulos/capitulo01-sistemas-biologicos.tex
  ```

- Heuristic analyzer for long/complex frames (split/structure suggestions):
  ```bash
  python3 .agent/skills/latex_repair/scripts/analyze_frames.py capitulos/capitulo01-sistemas-biologicos.tex
  ```

- Google Classroom integration (CLI, use to list courses and post materials/assignments):
  - List courses to find course_id:
    ```bash
    python .agent/skills/classroom_injector/scripts/injector.py list-courses
    ```
  - Post course material from a local Markdown file:
    ```bash
    python .agent/skills/classroom_injector/scripts/injector.py post-material --course-id "<ID>" --title "Título" --file "/abs/path/arquivo.md"
    ```
  - Post an assignment from a local Markdown file:
    ```bash
    python .agent/skills/classroom_injector/scripts/injector.py post-atividade --course-id "<ID>" --title "Atividade" --file "/abs/path/atividade.md"
    ```

Notes
- For Classroom CLIs, ensure Google OAuth credentials exist and that the first run completes the browser OAuth flow (see skill docs in `.agent/skills/classroom_injector/SKILL.md`).
- Install any Python dependencies listed in each skill's `requirements.txt` as needed.

## High-level architecture

This repository is a LaTeX/Beamer slide deck project with optional automation/QA helpers and Classroom integration.

- Template-first LaTeX structure
  - `template/beamer-template.tex` defines the Beamer theme, color scheme, code listing styles, math and biology-specific convenience commands (e.g., `\definicao{}`, `\exemplo{}`, `\destaque{}`, `\gene{}`, `\proteina{}`), and footline/navigation settings. Individual chapters import or mirror this template for consistent styling and macros.
  - Chapters under `capitulos/` are self-contained Beamer documents (e.g., `capitulo01-*.tex`, `capitulo02-*.tex`, etc.). They rely on standard TeX packages declared in the template and include figures from `images/` when needed. PDFs produced for some chapters are checked in for reference.

- Build and batch automation
  - Local builds are driven directly by `pdflatex`/`latexmk`. A convenience script `compile_all.sh` iterates over `capitulo*.tex`, compiles each twice to resolve references, summarizes successes/failures, and cleans auxiliary files. This is the authoritative way to batch-compile everything in `capitulos/`.

- Slide quality assurance (QA) helpers
  - `.agent/skills/beamer_layout_guard/` provides a Python analyzer that inspects `.tex` and log characteristics to flag overfull frames, long lines, or dense content. Use it proactively after edits to prevent text overflow and readability issues.
  - `.agent/skills/latex_repair/` provides a complementary heuristic analyzer geared toward identifying frames that should be split or restructured (e.g., too many nested blocks or >10 list items). It encodes recommended refactoring patterns like splitting frames, moving verbose content to notes, or using columns judiciously.
  - `test_slide.tex` and `test_tikz_demo.tex` serve as minimal, known-good inputs to validate that the local LaTeX toolchain (fonts, TikZ, theme) is working before compiling full chapters.

- Visual design aid for complex diagrams
  - `.agent/skills/tikz_generator/` documents a workflow to replace complex TikZ diagrams with designed infographic images while keeping slide composition simple (i.e., swap `tikzpicture` blocks for `\includegraphics{...}` with preserved aspect-ratio). This is optional but useful for aesthetic/legibility upgrades.

- Classroom delivery integrations (optional)
  - Two complementary approaches exist:
    - A thin, scripted approach in repo root (`print_courses.py`, `injeta_classroom.py`, `injeta_atividade.py`) that wires into the Classroom API via the skill path.
    - A CLI-first approach under `.agent/skills/classroom_injector/` offering commands to list courses and post materials/assignments from local Markdown files. Prefer the injector CLI for repeatability and clearer parameters; fall back to root scripts only if necessary.

## Key operational context from README

- LaTeX toolchain
  - Install a full TeX distribution (TeX Live/MacTeX/MiKTeX) with Beamer, TikZ, listings, babel (Portuguese), and other common packages. `latexmk` is recommended for multi-pass builds and watch mode.
- Chapter workflow
  - New chapters typically copy or import `template/beamer-template.tex`, define title/author/institute/date, and structure content using Beamer frames, the custom block commands, and optional TikZ/figures. Compile iteratively with `latexmk -pdf` (or `-pvc`).
- Troubleshooting
  - The README documents common fixes (installing language packs, TikZ packages, font map updates, and using `-interaction=nonstopmode -halt-on-error` for faster feedback). Use these when builds fail or are slow.

## Existing guidance files and how to use them

- `README.md` (authoritative user-facing overview)
  - Provides installation prerequisites, compilation commands (single-file, latexmk, batch), customization via the shared template, examples of custom LaTeX commands and TikZ usage, and troubleshooting tips. Pull build commands and environment hints directly from here when guiding users.
- `.agent/skills/*/SKILL.md` (automation/QA playbooks)
  - Beamer Layout Guard: run the analyzer to detect overfull frames and apply the documented fixes (allowframebreaks, manual splits, shrink, columns).
  - LaTeX Repair: use the heuristic analyzer to identify long/complex frames and follow the listed refactoring strategies.
  - TikZ Generator: when asked to beautify or replace complex TikZ, follow the prompt-design and replacement workflow.
  - Classroom Injector and Google Classroom Manager: prefer the injector CLI to list courses and post materials/assignments; complete OAuth on first run.

## When creating or modifying chapters

- Favor the shared template’s custom commands and styles to ensure consistency across chapters.
- After significant content additions, run the layout guard and/or repair analyzer and address flagged frames before committing.
- Use `latexmk -pdf -pvc` during iterative editing; use `./compile_all.sh` to validate the full set before sharing releases.
