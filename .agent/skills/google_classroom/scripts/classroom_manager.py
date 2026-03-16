import os.path
import argparse
import tempfile
import markdown
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

# Escopos de permissões
SCOPES = [
    'https://www.googleapis.com/auth/classroom.courses.readonly',
    'https://www.googleapis.com/auth/classroom.courseworkmaterials',
    'https://www.googleapis.com/auth/classroom.coursework.students',
    'https://www.googleapis.com/auth/classroom.announcements',
    'https://www.googleapis.com/auth/drive.file' # Necessário para o PDF
]

def authenticate(credentials_path="credentials.json", token_path="token.json"):
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_path):
                raise FileNotFoundError(f"Erro: O arquivo '{credentials_path}' não foi encontrado.")
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    return creds

def convert_md_to_pdf_drive(drive_service, md_filepath, title):
    """Converte markdown para PDF usando a API do Google Drive."""
    print("Lendo e convertendo Markdown para HTML...")
    with open(md_filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    html_text = f"<html><body>{markdown.markdown(md_text, extensions=['fenced_code', 'tables'])}</body></html>"
    
    # Prepara o HTML em arquivo na pasta
    temp_html_path = "temp_upload.html"
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(html_text)

    print("Enviando HTML para o Google Drive para renderizar...")
    file_metadata = {'name': title, 'mimeType': 'application/vnd.google-apps.document'}
    media = MediaFileUpload(temp_html_path, mimetype='text/html', resumable=True)
    
    doc = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    doc_id = doc.get('id')
    
    print("Exportando arquivo final em PDF...")
    request = drive_service.files().export_media(fileId=doc_id, mimeType='application/pdf')
    
    temp_pdf_path = "temp_upload.pdf"
    with open(temp_pdf_path, 'wb') as f:
        f.write(request.execute())
        
    print("Refazendo upload do PDF como material raiz...")
    pdf_metadata = {'name': f"{title}.pdf"}
    pdf_media = MediaFileUpload(temp_pdf_path, mimetype='application/pdf', resumable=True)
    pdf_file = drive_service.files().create(body=pdf_metadata, media_body=pdf_media, fields='id').execute()
    
    # Limpeza
    drive_service.files().delete(fileId=doc_id).execute()
    
    try:
        os.remove(temp_html_path)
        os.remove(temp_pdf_path)
    except:
        pass
        
    pdf_id = pdf_file.get('id')
    print(f"PDF Finalizado de ID: {pdf_id}")
    return pdf_id

def upload_local_pdf(drive_service, pdf_filepath, title):
    """Sobe um arquivo PDF já existente na máquina para o Google Drive."""
    print("Enviando arquivo PDF bruto para o Google Drive...")
    pdf_metadata = {'name': f"{title}.pdf"}
    pdf_media = MediaFileUpload(pdf_filepath, mimetype='application/pdf', resumable=True)
    pdf_file = drive_service.files().create(body=pdf_metadata, media_body=pdf_media, fields='id').execute()
    
    pdf_id = pdf_file.get('id')
    print(f"PDF Local transferido com sucesso. ID: {pdf_id}")
    return pdf_id

def list_courses(service):
    try:
        results = service.courses().list(pageSize=10).execute()
        for course in results.get('courses', []):
            print(f"- {course.get('name')} (ID/Course-ID: {course.get('id')})")
    except HttpError as error:
        print(error)

def post_announcement(service, course_id, text):
    try:
        body = {'text': text, 'state': 'PUBLISHED'}
        res = service.courses().announcements().create(courseId=course_id, body=body).execute()
        print(f"[Sucesso] Anúncio: {res.get('id')}")
    except HttpError as error:
        print(error)

def post_material(classroom_service, drive_service, course_id, title, description, link=None, filepath=None):
    try:
        material = {'title': title, 'description': description, 'state': 'PUBLISHED', 'materials': []}
        
        if link:
            material['materials'].append({'link': {'url': link}})
            
        if filepath:
            pdf_id = None
            if filepath.endswith('.md'):
                pdf_id = convert_md_to_pdf_drive(drive_service, filepath, title)
            elif filepath.endswith('.pdf'):
                pdf_id = upload_local_pdf(drive_service, filepath, title)
            
            if pdf_id:
               material['materials'].append({
                   'driveFile': {
                       'driveFile': {'id': pdf_id},
                       'shareMode': 'VIEW'
                   }
               })
            
        res = classroom_service.courses().courseWorkMaterials().create(courseId=course_id, body=material).execute()
        print(f"[Sucesso] Material didático postado! Material-ID: {res.get('id')}")
    except HttpError as error:
        print(f'Um erro ocorreu ao postar material didático: {error}')

def main():
    parser = argparse.ArgumentParser(description='Skill: Google Classroom CLI Manager')
    subparsers = parser.add_subparsers(dest='command')
    subparsers.add_parser('list-courses')
    
    p_ann = subparsers.add_parser('post-announcement')
    p_ann.add_argument('--course-id', required=True)
    p_ann.add_argument('--text', required=True)

    p_mat = subparsers.add_parser('post-material')
    p_mat.add_argument('--course-id', required=True)
    p_mat.add_argument('--title', required=True)
    p_mat.add_argument('--description', required=True)
    p_mat.add_argument('--link')
    p_mat.add_argument('--file', help='Caminho para um arquivo markdown local para converter e anexar como PDF.')

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    try:
        creds = authenticate()
        classroom_service = build('classroom', 'v1', credentials=creds)
        drive_service = build('drive', 'v3', credentials=creds)

        if args.command == 'list-courses':
            list_courses(classroom_service)
        elif args.command == 'post-announcement':
            post_announcement(classroom_service, args.course_id, args.text)
        elif args.command == 'post-material':
            post_material(classroom_service, drive_service, args.course_id, args.title, args.description, args.link, getattr(args, 'file', None))

    except Exception as e:
        print(f"Erro Crítico: {e}")

if __name__ == '__main__':
    main()
