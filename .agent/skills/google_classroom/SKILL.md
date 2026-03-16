---
name: Google Classroom Manager
description: Skill para gerenciar e automatizar postagens (materiais, anúncios no mural e leitura de dados) no Google Classroom através da integração nativa com a API Auth do Google em Python.
---

# Google Classroom Manager

Esta **Skill** dota o assistente de inteligência e ferramentas cli para que ele possa gerenciar o ambiente virtual do aluno, enviando conteúdos gerados durante a chat diretamente aos alunos daquele professor.

## Pré-requisitos
1. **Credenciais do Google Cloud:** É indispensável criar um projeto no [Google Cloud Console](https://console.cloud.google.com/), buscar e habilitar a "Google Classroom API" e, através da tela "Credentials", gerar e baixar um Client ID OAuth 2.0 (Application Type: Desktop app).
2. Salve o arquivo baixado como `credentials.json` na raiz de onde deseja rodar o código.
3. Instale as dependências: `pip install -r .agent/skills/google_classroom/requirements.txt`.

## Como Usar (Para a IA)

Você (a IA) deve utilizar os comandos do CLI disponíveis no arquivo `scripts/classroom_manager.py` toda vez que o usuário pedir para postar anúncios no mural ou subir materiais didáticos que você gerou localmente.

### Comandos da CLI disponíveis:

**1. Listar Cursos Disponíveis**
```bash
python .agent/skills/google_classroom/scripts/classroom_manager.py list-courses
```
*Use isto primeiro para capturar o ID (course_id) da turma a qual o professor se refere.*

**2. Postar Anúncio no Mural**
```bash
python .agent/skills/google_classroom/scripts/classroom_manager.py post-announcement --course-id "M4SK2039LDF" --text "Lembrete: A atividade 01 vence amanhã!"
```

**3. Criar Material Didático (Arquivos, Links ou Aulas)**
```bash
python .agent/skills/google_classroom/scripts/classroom_manager.py post-material --course-id "ID_AQUI" --title "Material de Onboarding" --description "Instruções do Google Colab e Antigravity." --link "https://url-do-arquivo"
```

> **Atenção:** Ao rodar pela primeira vez no terminal, informaremos ao professor que ele deve checar o navegador para conceder acesso e login via OAuth (Isto gerará o `token.json` automágico).
