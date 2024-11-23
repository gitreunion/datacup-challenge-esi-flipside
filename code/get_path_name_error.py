#get more details in the ipynb file
#main output: zeop_with_errors.csv
#other outputs: wrong_no_accents.csv, zeop_jasmins.csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from unidecode import unidecode
import openpyxl as px #may need to install openpyxl (pip install openpyxl)
from geopy.distance import geodesic #may need to install geopy (pip install geopy)

df = pd.read_csv("Adresses ZEOP Les 3 Bassins.geocoded.csv", delimiter=';')
df_zeop = pd.read_excel("Adresses ZEOP Les 3 Bassins.xlsx")
df_ban = pd.read_excel("Adresses BAN Les 3 Bassins.xlsx", sheet_name="Feuil1")
#takes off the rows where the 'certification_commune' is 0
df_ban = df_ban[df_ban['certification_commune'] != 0]
# bring out the scores that are lower than 1
df_2 = df[df['result_score'] < 1]

#get only the 1st word of the 'result_street' column
df_2['type_result'] = df_2['result_street'].str.split(' ').str[0]

#prélève que les noms de voies de la colonne 'result_street' en enlevant les types de voies dans ce nom

df_2['result_street'] = df_2['result_street'].str.split(' ').str[1:].str.join(' ')

# Convert columns to string, replace commas with dots, and convert to float
df_2['x'] = df_2['x'].astype(str).str.replace(',', '.').astype(float)
df_2['y'] = df_2['y'].astype(str).str.replace(',', '.').astype(float)
df_ban['lat'] = df_ban['lat'].astype(str).str.replace(',', '.').astype(float)
df_ban['lon'] = df_ban['lon'].astype(str).str.replace(',', '.').astype(float)

# Filtrer le dataframe ZEOP pour le nom de voie "DES JASMINS"
zeop_jasmins = df_2[df_2['nom_voie'].str.lower() == 'des jasmins']



def find_closest_address(row, df_ban): #row est une ligne du dataframe zeop_jasmins, df_ban est le dataframe des ad
    zeop_coords = (row['y'], row['x'])
    df_ban['distance'] = df_ban.apply(lambda x: geodesic(zeop_coords, (x['lat'], x['lon'])).meters, axis=1)
    closest_address = df_ban.loc[df_ban['distance'].idxmin()]
    return {
        'closest_lat': closest_address['lat'],
        'closest_lon': closest_address['lon'],
        'distance': closest_address['distance'],
        'address': closest_address.get('address', 'Unknown')  # Ensure 'address' key exists
    }

# Appliquer la fonction find_closest_address à chaque ligne du dataframe ZEOP
zeop_jasmins['closest_address'] = zeop_jasmins.apply(lambda x: find_closest_address(x, df_ban), axis=1)

# Extraire les informations d'adresse à partir des coordonnées les plus proches
def get_real_address(row, df_ban): #row est une ligne du dataframe zeop_jasmins, df_ban est le dataframe des adresses BAN
    closest_lat = row['closest_address']['closest_lat']
    closest_lon = row['closest_address']['closest_lon']
    real_address = df_ban[(df_ban['lat'] == closest_lat) & (df_ban['lon'] == closest_lon)]
    if not real_address.empty:
        return {
            'numero': real_address.iloc[0].get('numero', 'Unknown'),
            'nom_voie': real_address.iloc[0].get('nom_voie', 'Unknown')
        }
    return {'numero': 'Unknown', 'nom_voie': 'Unknown'}

# Ajouter les informations d'adresse réelle au dataframe zeop_jasmins
zeop_jasmins['real_address'] = zeop_jasmins.apply(lambda x: get_real_address(x, df_ban), axis=1)

zeop_jasmins.to_csv('./zeop_jasmins.csv', sep=';')

# create a dataframe with only the matching results with the column 'result_street' and 'nom_voie' not caring about the case
df_3 = df_2[df_2['result_street'].str.lower() == df_2['nom_voie'].str.lower()]
df_3
df_wrong = df_2[df_2['result_street'].str.lower() != df_2['nom_voie'].str.lower()]

# Remove accents for comparison
df_wrong['result_street_no_accents'] = df_wrong['result_street'].apply(unidecode).str.lower()
df_wrong['nom_voie_no_accents'] = df_wrong['nom_voie'].apply(unidecode).str.lower()

# Filter out rows where the only difference is the accent
df_wrong_no_accents = df_wrong[df_wrong['result_street_no_accents'] != df_wrong['nom_voie_no_accents']]

# Write df_wrong_no_accents to a csv file but only the columns 'nom_voie', 'result_street', 'result_score', 'result_type', 'result_status', taking off the duplicated names in the 'nom_voie' column
df_wrong_no_accents.drop_duplicates(subset='result_street').to_csv('wrong_no_accents.csv', columns=['nom_voie', 'type_result', 'result_street', 'result_score', 'result_type', 'result_status'], sep=';')

df_wrong_names_no_accents = pd.read_csv('wrong_no_accents.csv', delimiter=';')

# Define a function to check for errors
def check_for_errors(row, df_wrong_names_no_accents):
    if row['nom_voie'] in df_wrong_names_no_accents['nom_voie'].values:
        return True, 'Mauvais nom de voie ou faute'
    else:
        return False, None

# Apply the function to the df_zeop dataframe
df_zeop[['error', 'error_type']] = df_zeop.apply(lambda row: check_for_errors(row, df_wrong_names_no_accents), axis=1, result_type='expand')

#put the zeop dataframe in a csv file
df_zeop.to_csv('zeop_with_errors.csv', sep=';')