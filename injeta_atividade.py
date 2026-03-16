import os
import sys

# Adiciona a skill no path pra importar as funcoes
sys.path.append(os.path.join(os.getcwd(), ".agent", "skills", "google_classroom", "scripts"))
from classroom_manager import authenticate, build, post_material

COURSE_ID = "794110679584"
TITLE = "[Atividade 0] Configuração e Teste de Ambiente"

MARKDOWN_PATH = r"C:\Users\lemke\.gemini\antigravity\brain\c3564c61-4df2-4c7d-8a49-7c6d76914ce4\atividade_classroom_setup.md"

try:
    with open(MARKDOWN_PATH, 'r', encoding='utf-8') as f:
        CONTENT = f.read()
except FileNotFoundError:
    print(f"Erro: Não encontrei '{MARKDOWN_PATH}'")
    sys.exit(1)

token_path = 'token.json'
creds = authenticate(token_path=token_path)
service = build('classroom', 'v1', credentials=creds)

print("Iniciando injeção da atividade...")
post_material(service, COURSE_ID, TITLE, CONTENT)
