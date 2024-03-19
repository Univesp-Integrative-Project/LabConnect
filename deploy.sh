# Entrar na pasta do projeto
cd LabConnect/

# Atualizar repositório
git fetch --all
sudo git clean -fdx
git reset --hard origin

# Construir e iniciar os contêineres Docker
sudo docker-compose up -d