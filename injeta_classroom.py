import os
import sys

# Adiciona a skill no path pra importar as funcoes
sys.path.append(os.path.join(os.getcwd(), ".agent", "skills", "google_classroom", "scripts"))
from classroom_manager import authenticate, build, post_material

# O ID da turma coletado do comando list-courses
COURSE_ID = "794110679584"
TITLE = "Guia de Onboarding: Ferramentas do Curso"

MARKDOWN_PATH = "C:\\Users\\lemke\\.gemini\\antigravity\\brain\\c3564c61-4df2-4c7d-8a49-7c6d76914ce4\\onboarding_ferramentas.md"
# Lendo com tratamento de Windows Paths
try:
    with open(MARKDOWN_PATH, 'r', encoding='utf-8') as f:
        CONTENT = f.read()
except FileNotFoundError:
    print(f"Erro: Não encontrei '{MARKDOWN_PATH}'")
    sys.exit(1)

token_path = 'token.json'
creds = authenticate(token_path=token_path)
service = build('classroom', 'v1', credentials=creds)

print("Iniciando injeção do material...")
post_material(service, COURSE_ID, TITLE, CONTENT)
