#Importa imagem do python como alpine (versão leve com apenas o essêncial do linux)
FROM python:3.8.3-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code

#Define diretório de trabalho no container
WORKDIR /code

#Atualiza o pip do python
RUN pip install --upgrade pip

#Cópia o arquivo requirements.txt para dentro do container
COPY requirements.txt .

#Instala as dependências contidas no requirements.txt
RUN pip install  -r requirements.txt

#Cópia todos os arquivos da atuais da aplicação para o container (diretório de trabalho)
COPY . .