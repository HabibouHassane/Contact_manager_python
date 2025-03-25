# Utiliser une image Python 3.13 comme image de base
FROM python:3.13-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires de votre application dans le conteneur
COPY . /app

# Installer les dépendances requises
#RUN pip install --no-cache-dir -r requirements.txt

# Commande pour exécuter votre application
CMD ["python", "main.py"]
