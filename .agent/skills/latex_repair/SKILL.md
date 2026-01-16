---
name: LaTeX Repair
description: Comprehensive guide and tools for fixing common LaTeX/Beamer presentation issues like overfull frames and structural errors.
---

# LaTeX/Beamer Repair Skill

This skill helps identifying and fixing common LaTeX presentation issues, specifically "overfull frames" where text is cut off or too dense, and structural errors.

## 1. Automated Analysis

Use the provided Python script to scan `.tex` files for potential issues.

### Usage
Run the analysis script from the repository root:
```bash
python3 .agent/skills/latex_repair/scripts/analyze_frames.py <path_to_tex_file>
```

### What it Checks
- **Overfull Frames**: Frames with >10 lines of text.
- **Complexity**: Frames with deep nesting or too many blocks (>3).
- **Structure**: Unbalanced environments or missing fields.
- **Log Errors**: Critical errors found in the associated `.log` file (e.g., `! LaTeX Error`).
- **Missing References**: Referenced files (`\input`, `\include`, `\includegraphics`) that are missing.

## 2. Refactoring Strategy

For each identified problematic frame, apply one of the following strategies:

### Strategy A: Split into Multiple Slides
If a frame has multiple distinct topics or blocks:
1.  Duplicate the `\begin{frame}...\end{frame}` structure.
2.  Append `(1/2)`, `(2/2)` or `(Parte 1)`, `(Parte 2)` to the titles.
3.  Distribute the content. Ensure no single slide exceeds the content limits.

### Strategy B: Move Content to Notes
If the frame is verbose but the content is explanation:
1.  Move detailed text to `\note{...}`.
2.  Keep only bullet points or keywords on the slide.

### Strategy C: Optimize Layout
1.  Use `\begin{columns}` to place text side-by-side if vertical space is the issue (careful not to clutter).
2.  Reduce `vspace` overuse.

## 3. Verification

After applying changes:
1.  Verify that every `\begin{frame}` has a matching `\end{frame}`.
2.  Check that itemize/enumerate environments are properly closed.
3.  Re-run the analysis script to confirm issues are resolved.
