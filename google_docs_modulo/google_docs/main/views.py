from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from django.contrib import messages
import datetime

SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']

# View para realizar a requisição da conta google
# As únicas contas google permitidas são aquelas que estão como usuários permitidos pela 
# api do projeto no google cloud
def viewConnection(request):
	creds = None
	# Se não houver token(conexão já estabelecida anteriormente), é requerido através do navegador
	# que o usuário informe a conta google onde vai ocorrer o gerenciamento desses documentos.
	if os.path.exists('main/token.json'):
		creds = Credentials.from_authorized_user_file('main/token.json', SCOPES)
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('main/credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		
		path = 'main/'
		file = 'token.json'
		completeName = os.path.join(path, file)
		with open(completeName, 'w') as token:
			token.write(creds.to_json())
	
	return render(request, "index.html")


def getFilesAndMerge(request):
	
	creds = Credentials.from_authorized_user_file('main/token.json', SCOPES)
	drive_service = build('drive', 'v3', credentials=creds)
	docs_service = build('docs', 'v1', credentials=creds)

	if request.method == 'POST':

		get_customer_name = request.POST['customer-name']
		get_template_name = request.POST['template-name']

		try:

			# Realizar busca de templates na lista
			response = drive_service.files().list(
				q=("mimeType='application/vnd.google-apps.document'" and "name='%s'"%get_template_name),
				spaces='drive',
				fields='nextPageToken, files(id,name)'
				).execute()	

			file = response.get('files', [])

			if(len(file) > 0):

				data = datetime.datetime.now()
				document_id = file[0]['id']
				copy_title = file[0]['name'] + "/" + str(data)	
				
				# direcionar cópias criadas para uma pasta específica
				body = {
				 	'name': copy_title,
				 	'parents': ['1XTA0MqjPWmzUGr0SeZX3XDrZoPTvsJGD']
				}

				#Gerar cópia do arquivo template no drive
				copy_response = drive_service.files().copy(
				 	fileId=document_id, 
				 	body=body).execute()
				
				document_copy_id = copy_response.get('id')

				#Inserção dos dados no template copiado
				requests = [
					{
						'replaceAllText': {
							'containsText':{
								'text': '{{customer-name}}',
								'matchCase': 'true'
							},
							'replaceText': get_customer_name
						}}
				]

				result = None
				result = docs_service.documents().batchUpdate(
					documentId=document_copy_id, body={'requests': requests}).execute()
				
				if result is not None:
					messages.success(request, 'Documento gerado com sucesso')

			else:
				messages.error(request, 'Template requisitado não existe')		
		except:
			messages.error(request, 'Ocorreu um erro ao requisitar api google')
			
	else:
		messages.error(request, 'Método de requisição inválido')

	return HttpResponseRedirect(reverse('index'))















