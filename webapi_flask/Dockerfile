FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /app

# Anforderungen installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App-Dateien kopieren
COPY . .

# Exponierter Port (vom Server verwendeter Port)
EXPOSE 8080

# Startbefehl (anpassen, falls die Hauptdatei anders heißt)
CMD ["python", "/src/start_server.py"]
