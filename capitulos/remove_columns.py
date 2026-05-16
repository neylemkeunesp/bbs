import re

file_path = 'capitulo04-mathematics.tex'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

titles_to_fix = [
    r"Revisão: Equações Diferenciais Ordinárias",
    r"Campos Vetoriais e Retratos de Fase",
    r"Tipos de Pontos Fixos",
    r"Bifurcação Saddle-Node \(Fold\)",
    r"Bifurcação Transcrítica",
    r"Bifurcação Pitchfork",
    r"Bifurcação de Hopf",
    r"Soluções Periódicas",
    r"Ciclos Limite"
]

for title in titles_to_fix:
    pattern = r'(\\begin\{frame\}\[allowframebreaks\]\{' + title + r'\}.*?\\end\{frame\})'
    
    def replacer(match):
        frame_content = match.group(1)
        frame_content = re.sub(r'\\begin\{columns\}.*?\n', '', frame_content)
        frame_content = re.sub(r'\\end\{columns\}.*?\n', '', frame_content)
        frame_content = re.sub(r'\\column\{.*?\}\n', '', frame_content)
        return frame_content

    content = re.sub(pattern, replacer, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Columns removed from overfull frames.")
