FROM python:3.8

# Criar o diretório de destino para a aplicação
RUN mkdir -p /app

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os arquivos da aplicação para o diretório de trabalho
COPY . /webapp/impl/app

# Instalar as dependências da aplicação
#RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]    


