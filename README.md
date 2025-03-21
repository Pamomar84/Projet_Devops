# Basic Docker Project

## Objectif

Créer un serveur HTTP minimaliste en Python avec Docker, sans utiliser de frameworks.
# Les etapes pour etapes pour executer le projet sans docker compose 
apres avoir creer le projet la structure et les codes, il faut ouvrir powershell et executer les commandes suivantes :
 -docker build -t basic-docker-projet  .         : pour creer une image docker et le nommer basic-docker-project             
 -docker run -p 8000:8000 basic-python-server    : pour creer un conteneur et executer 

# pour le dockerhub
docker login : pour se conencter 

docker tag basic-docker-project-momarapp pamomar84/basic-docker-project:latest

docker push pamomar84/basic-docker-project:latest

## Structure du projet

