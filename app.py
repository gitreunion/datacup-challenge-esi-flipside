import os
import pandas as pd
from flask import Flask, request, render_template, send_file, redirect, url_for

app = Flask(__name__)

# Répertoire pour stocker les fichiers temporairement
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint pour gérer le téléchargement de fichier
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Sauvegarder le fichier téléchargé
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Traiter le fichier avec le programme Python
    processed_filepath = process_file(filepath)

    # Renvoyer le fichier traité à l'utilisateur
    return send_file(processed_filepath, as_attachment=True)

# Fonction pour traiter le fichier (remplacez par votre programme Python)
def process_file(filepath):
    # Lire le fichier CSV ou Excel
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format")

    # Exemple de traitement (remplacez par votre logique)
    df['Processed'] = True  # Ajout d'une colonne fictive

    # Sauvegarder le fichier traité
    processed_filepath = os.path.join(app.config['PROCESSED_FOLDER'], 'processed_file.csv')
    df.to_csv(processed_filepath, index=False)
    return processed_filepath

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)