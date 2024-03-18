# Imagem base do Python
FROM python:3.12

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para diretório de trabalho
COPY . .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Comando para iniciar o servidor web com SSL/TLS
CMD [ "python", "manage.py", "runsslserver", "0.0.0.0:443", "--certificate", "/etc/ssl/certs/certificado.crt", "--key", "/etc/ssl/private/chave_privada.key" ]
