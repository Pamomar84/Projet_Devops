# Utiliser l'image officielle Python 3.9, version slim pour plus de légèreté
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le dossier 'app' dans le répertoire de travail du conteneur
COPY app/ /app

# Exposer le port 8000 pour que Docker le mappe vers l'hôte
EXPOSE 8000

# Commande pour démarrer le serveur Python
CMD ["python", "server.py"]