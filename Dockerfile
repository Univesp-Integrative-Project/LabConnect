# Imagem base
FROM python:3.12

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Diretório de trabalho
WORKDIR /app

# Instalando dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        nginx \
        openssl \
    && rm -rf /var/lib/apt/lists/*

# Copiando o arquivo de requisitos e instalando as dependências do Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o código da aplicação para o contêiner
COPY . /app/

# Criando diretório SSL
RUN mkdir -p /etc/nginx/ssl/

# Gerando certificado SSL
RUN openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx-selfsigned.key -out /etc/nginx/ssl/nginx-selfsigned.crt -subj "/C=BR/ST=Sao Paulo/L=Sao Paulo/O=Univesp/CN=2106743@aluno.univesp.br"

# Configurando o NGINX
COPY nginx.conf /etc/nginx/nginx.conf
RUN rm /etc/nginx/sites-enabled/default

# Porta de exposição
EXPOSE 80
EXPOSE 443

# Comando para iniciar a aplicação
CMD ["nginx", "-g", "daemon off;"]
