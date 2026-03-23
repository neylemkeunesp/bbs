---
name: Classroom Content Injector
description: Skill gerenciadora do Google Classroom para listar cursos e injetar conteúdos (Material e Atividades) diretamente a partir de arquivos Markdown locais.
---

# Classroom Content Injector

Esta **Skill** une a capacidade de listar os cursos disponíveis no Google Classroom e de injetar de forma direta arquivos Markdown locais como **Material Didático** ou **Atividades (Assignments)**. 
Foi baseada nos scripts `injeta_atividade.py`, `injeta_classroom.py` e `print_courses.py` originais.

## Pré-requisitos
1. **Credenciais do Google Cloud:** Você precisa de um arquivo `credentials.json` (OAuth 2.0 Desktop app) na raiz do projeto ou na pasta da skill `.agent/skills/classroom_injector/`.
2. Instalar as dependências:
```bash
pip install -r .agent/skills/classroom_injector/requirements.txt
```

## Como Usar (Para a IA)

Sempre que o usuário solicitar a postagem de um aviso, material ou atividade gerados por você em Markdown, salve o conteúdo em um arquivo temporário/artefato e utilize a CLI abaixo.

### Comandos da CLI disponíveis:

**1. Listar Cursos Disponíveis**
```bash
python .agent/skills/classroom_injector/scripts/injector.py list-courses
```
*Sempre rode este comando primeiro caso não tenha o ID da turma (Course-ID).*

**2. Postar Material Didático (Material)**
```bash
python .agent/skills/classroom_injector/scripts/injector.py post-material --course-id "ID_DO_CURSO" --title "Título do Material" --file "/caminho/absoluto/do/arquivo.md"
```
*Irá criar um post de Material preenchendo o campo de descrição com o conteúdo raw do markdown.*

**3. Postar Atividade (Assignment)**
```bash
python .agent/skills/classroom_injector/scripts/injector.py post-atividade --course-id "ID_DO_CURSO" --title "Título da Atividade" --file "/caminho/absoluto/do/arquivo.md"
```
*Cria um **Assignment** (Atividade), diferentemente de um Material, permitindo que os alunos recebam nota e integrem a área de tarefas.*

> **Nota:** Se o sistema ainda não possuir `token.json`, a primeira execução disparará o fluxo OAuth no navegador.
