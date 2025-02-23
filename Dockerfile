FROM python:3.9-slim
WORKDIR /app

# Copier tous les fichiers nécessaires
COPY app.py requirements.txt ./
COPY templates/ ./templates/
COPY static/ ./static/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port et démarrer l'application
EXPOSE 8000
CMD ["python", "app.py"]