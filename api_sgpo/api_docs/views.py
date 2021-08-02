from django.shortcuts import render
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import os
import datetime

SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']

def viewConnection(request):
	# Identificado erro quando requisita nova conexao após token estar vencido
	creds = None

	if os.path.exists('api_docs/token.json'):
		creds = Credentials.from_authorized_user_file('api_docs/token.json', SCOPES)
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_secrets_file('api_docs/credentials.json', SCOPES)
			creds = flow.run_local_server(port=0)
		
		path = 'api_docs/'
		file = 'token.json'
		completeName = os.path.join(path, file)
		with open(completeName, 'w') as token:
			token.write(creds.to_json())
	return HttpResponse(status=200)


@csrf_exempt
def getFilesAndMerge(request):

	creds = Credentials.from_authorized_user_file('api_docs/token.json', SCOPES)
	drive_service = build('drive', 'v3', credentials=creds)
	docs_service = build('docs', 'v1', credentials=creds) 
	if request.method == 'POST':		
		data = JSONParser().parse(request)

		modelo_nome = data['doc_modelo']
		nome_processo = data['nome_processo']
		codigo_processo = data['codigo_processo']
		objetivo_processo = data['objetivo_processo']
		cadeia_valor = data['cadeia_valor']
		processo_gestor = data['processo_gestor']
		processo_proprietario = data['processo_proprietario']

		try:
			response = drive_service.files().list(
				q=("mimeType='application/vnd.google-apps.document'" and "name='%s'"%modelo_nome),
				spaces='drive',
				fields='nextPageToken, files(id,name)'
				).execute()	

			file = response.get('files', [])

			if(len(file) > 0):

				data = datetime.datetime.now()
				document_id = file[0]['id']
				copy_title = file[0]['name'] + "/" + str(data)	

				body = {
					'name': copy_title,
					'parents': ['1XTA0MqjPWmzUGr0SeZX3XDrZoPTvsJGD']
				}

				copy_response = drive_service.files().copy(fileId=document_id,
					body=body).execute()

				document_copy_id = copy_response.get('id')

				requests = [
						{
							'replaceAllText': {
								'containsText':{
									'text': '{{nome-processo}}',
									'matchCase': 'true'
								},
								'replaceText': nome_processo
						}},
						{
							'replaceAllText':{
								'containsText':{
									'text': '{{codigo-processo}}',
									'matchCase':'true'
								},
								'replaceText': codigo_processo
							}
						},
						{
							'replaceAllText': {
								'containsText':{
									'text': '{{objetivo-processo}}',
									'matchCase': 'true'
								},
								'replaceText': objetivo_processo
						}},
						{
							'replaceAllText': {
								'containsText':{
									'text': '{{cadeia-valor}}',
									'matchCase': 'true'
								},
								'replaceText': cadeia_valor
						}},
						{
							'replaceAllText': {
								'containsText':{
									'text': '{{processo-gestor}}',
									'matchCase': 'true'
								},
								'replaceText': processo_gestor
						}},
						{
							'replaceAllText': {
								'containsText':{
									'text': '{{processo-proprietario}}',
									'matchCase': 'true'
								},
								'replaceText': processo_proprietario
						}}
					]

				result = docs_service.documents().batchUpdate(
				documentId=document_copy_id, body={'requests': requests}).execute()
			else:
				return HttpResponse(status=400)
		except:
			return HttpResponse(status=400)
	return HttpResponse(status=200)



















