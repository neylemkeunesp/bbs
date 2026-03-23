import os
import sys
import argparse
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.courseworkmaterials',
    'https://www.googleapis.com/auth/classroom.coursework.students'
]

def authenticate(credentials_path="credentials.json", token_path="token.json"):
    creds = None
    # Verifica se o token já existe na raiz ou na pasta da skill para evitar re-autenticação
    if os.path.exists('token.json'):
        token_path = 'token.json'
    elif os.path.exists('.agent/skills/google_classroom/token.json'):
        token_path = '.agent/skills/google_classroom/token.json'
        
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_path) and not os.path.exists('credentials.json'):
                print(f"Erro: O arquivo de credenciais 'credentials.json' não foi encontrado.", file=sys.stderr)
                sys.exit(1)
            
            # Fallback path for credentials
            cred_file = 'credentials.json' if os.path.exists('credentials.json') else credentials_path
            
            flow = InstalledAppFlow.from_client_secrets_file(cred_file, SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Salva o token preferencialmente no diretório atual
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
            
    return creds

def get_service():
    creds = authenticate(credentials_path=os.path.join(os.path.dirname(__file__), '..', 'credentials.json'),
                         token_path=os.path.join(os.path.dirname(__file__), '..', 'token.json'))
    return build('classroom', 'v1', credentials=creds)

def list_courses(service):
    try:
        results = service.courses().list(pageSize=10).execute()
        courses = results.get('courses', [])
        if not courses:
            print("Nenhum curso encontrado.")
        for c in courses:
            print(f"[{c['id']}] {c['name']}")
    except HttpError as error:
        print(f"Erro ao listar cursos: {error}", file=sys.stderr)

def post_material(service, course_id, title, content):
    try:
        material = {
            'title': title,
            'description': content,
            'state': 'PUBLISHED'
        }
        res = service.courses().courseWorkMaterials().create(courseId=course_id, body=material).execute()
        print(f"[Sucesso] Material didático injetado! ID: {res.get('id')}")
    except HttpError as error:
        print(f"Erro ao injetar material: {error}", file=sys.stderr)

def post_assignment(service, course_id, title, content):
    try:
        assignment = {
            'title': title,
            'description': content,
            'workType': 'ASSIGNMENT',
            'state': 'PUBLISHED'
        }
        res = service.courses().courseWork().create(courseId=course_id, body=assignment).execute()
        print(f"[Sucesso] Atividade (Assignment) injetada! ID: {res.get('id')}")
    except HttpError as error:
        print(f"Erro ao injetar atividade: {error}", file=sys.stderr)

def read_markdown(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo Markdown '{filepath}' não encontrado.", file=sys.stderr)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Skill: Classroom Content Injector CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Comando para listar cursos
    subparsers.add_parser("list-courses", help="Lista os cursos/salas do Classroom")

    # Comando para Material
    p_mat = subparsers.add_parser("post-material", help="Injeta material no Classrom com base em um arquivo Markdown")
    p_mat.add_argument("--course-id", required=True, help="O ID da sala (Course-ID)")
    p_mat.add_argument("--title", required=True, help="Título do Material")
    p_mat.add_argument("--file", required=True, help="Caminho do arquivo .md a ser lido")

    # Comando para Atividade
    p_ativ = subparsers.add_parser("post-atividade", help="Injeta atividade (Assignment) com base em arquivo Markdown")
    p_ativ.add_argument("--course-id", required=True, help="O ID da sala (Course-ID)")
    p_ativ.add_argument("--title", required=True, help="Título da Atividade")
    p_ativ.add_argument("--file", required=True, help="Caminho do arquivo .md a ser lido")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    service = get_service()

    if args.command == "list-courses":
        list_courses(service)
    elif args.command == "post-material":
        content = read_markdown(args.file)
        post_material(service, args.course_id, args.title, content)
    elif args.command == "post-atividade":
        content = read_markdown(args.file)
        post_assignment(service, args.course_id, args.title, content)

if __name__ == "__main__":
    main()
