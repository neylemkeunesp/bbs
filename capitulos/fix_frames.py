import re

file_path = 'capitulo04-mathematics.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace \begin{frame}[shrink=X] with \begin{frame}[allowframebreaks]
content = re.sub(r'\\begin\{frame\}\[shrink=\d+\]', r'\\begin{frame}[allowframebreaks]', content)

# Replace \begin{frame} without options to \begin{frame}[allowframebreaks]
content = re.sub(r'\\begin\{frame\}(?!\[)', r'\\begin{frame}[allowframebreaks]', content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Frames updated successfully!")
