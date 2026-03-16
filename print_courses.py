import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

token_path = 'token.json'
if not os.path.exists(token_path):
    token_path = '.agent/skills/google_classroom/token.json'

creds = Credentials.from_authorized_user_file(token_path)
service = build('classroom', 'v1', credentials=creds)
results = service.courses().list(pageSize=10).execute()
courses = results.get('courses', [])
for c in courses:
    print(f"[{c['id']}] {c['name']}")
