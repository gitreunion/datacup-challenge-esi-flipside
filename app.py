import os
import pandas as pd
from flask import Flask, request, render_template, send_file, redirect, url_for
import dash
from dash import dcc, html
import plotly.express as px

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

    # A remplacer paler le code de correction
    df['Processed'] = True 

    # Sauvegarder le fichier traité
    processed_filepath = os.path.join(app.config['PROCESSED_FOLDER'], 'processed_file.csv')
    df.to_csv(processed_filepath, index=False)
    return processed_filepath

# Dash app setup
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash/')

def create_map(input_path, output_path):
    # Check if files exist
    if not os.path.exists(input_path) or not os.path.exists(output_path):
        # Return an empty map with a default location if files are missing
        return px.scatter_mapbox(
            lat=[0], lon=[0], zoom=2, mapbox_style="carto-positron"
        )

    try:
        # Load data
        input_df = pd.read_csv(input_path)
        output_df = pd.read_csv(output_path)

        # Check if the required columns are present
        if 'y' not in input_df.columns or 'x' not in input_df.columns:
            raise ValueError("Input file must contain 'y' and 'x' columns")
        if 'y' not in output_df.columns or 'x' not in output_df.columns:
            raise ValueError("Output file must contain 'y' and 'x' columns")

        # Create map
        fig = px.scatter_mapbox(
            input_df,
            lat='y',
            lon='x',
            color_discrete_sequence=['red'],
            size_max=80,
            zoom=12,
            mapbox_style="carto-positron",
            hover_name="imb_id",  # Add hover labels from the 'Address' column
            hover_data={"num_voie": True, "type_voie": True, "nom_voie": True, "cp_no_voie":True} 
        )
        fig.add_scattermapbox(
            lat=output_df['y'],
            lon=output_df['x'],
            mode='markers',
            marker=dict(size=8, color='blue'),
            name='Processed Addresses'
        )
        return fig

    except Exception as e:
        print(UPLOAD_FOLDER)
        print(f"Error in creating map: {e}")
        # Return an empty map with a default location on error
        return px.scatter_mapbox(
            lat=[0], lon=[0], zoom=2, mapbox_style="carto-positron"
        )

dash_app.layout = html.Div([
    html.H1("Map Visualization"),
    dcc.Graph(id='map', figure=create_map(os.path.join(UPLOAD_FOLDER, 'input.csv'), os.path.join(PROCESSED_FOLDER, 'processed_file.csv')))
])

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)