import numpy as np
import pandas as pd
from rapidfuzz import fuzz

zeop = pd.read_csv("Adresses ZEOP Les 3 Bassins.csv", delimiter=';')

ban = pd.read_csv("Adresses BAN Les 3 Bassins.csv", delimiter=';')


ban["type_voie"]=ban["nom_afnor"].str.split(pat=" ").str[0]
ban["nom_afnor"]=ban["nom_afnor"].str.split(pat=" ").str[1:].str.join(" ").str.upper()

zeop['type_voie'].fillna(" ", inplace=True)
zeop["type_voie"] = zeop["type_voie"].str.upper()


ban.rename(columns = {'result_housenumber':'num_voie'}, inplace=True)
ban.rename(columns = {'result_street':'nom_voie'}, inplace=True)
ban['nom_voie'] = ban['nom_voie'].str.split(pat=" ").str[1:].str.join(" ").str.upper()
ban.rename(columns = {'numero':'num_voie'}, inplace=True)
ban["type_voie"]=ban["type_voie"].str.replace("CHEM", "CHEMIN", regex=False)  
ban["type_voie"]=ban["type_voie"].str.replace("CD", "CHEMIN DEPARTEMENTAL", regex=False)  
ban["type_voie"] = ban["type_voie"].str.replace("CHEMININ", "CHEMIN", regex=False)
ban["type_voie"].unique()


ban['lat'] = (
    ban['lat']
    .str.replace(" ", "", regex=True)   # Remove spaces
    .str.replace(",", ".", regex=False) # Replace commas with dots
    .astype(float)                      # Convert to float
)

ban['lon'] = (
    ban['lon']
    .str.replace(" ", "", regex=True)   # Remove spaces
    .str.replace(",", ".", regex=False) # Replace commas with dots
    .astype(float)                      # Convert to float
)


# Fonction pour effectuer la correspondance floue sur plusieurs colonnes
def multi_column_fuzzy_match(row, df_to_match, columns_to_match, scorer=fuzz.ratio):
    """
    row: une ligne du DataFrame source
    df_to_match: DataFrame cible pour la correspondance
    columns_to_match: liste des colonnes à comparer
    scorer: méthode de scoring (e.g., fuzz.ratio, fuzz.token_sort_ratio, etc.)
    """
    best_match = None
    best_score = 0
    
    for _, target_row in df_to_match.iterrows():
        try:
            # Assurez-vous que toutes les valeurs sont converties en chaînes
            scores = [
                scorer(str(row[col]), str(target_row[col])) for col in columns_to_match
            ]
            avg_score = sum(scores) / len(columns_to_match)  # Moyenne des scores
            
            if avg_score > best_score:
                best_score = avg_score
                best_match = target_row
        except Exception as e:
            print(f"Error while processing row: {e}")
            continue  # En cas d'erreur, ignorer cette itération
    
    return pd.Series({'matched_id': best_match['id'] if best_match is not None else None,
                      'match_score': best_score})

# Colonnes à comparer
columns = ['nom_voie', 'type_voie', 'num_voie' ]

# Appliquer la correspondance floue ligne par ligne
zeop[['matched_id', 'match_score']] = zeop.apply(
    multi_column_fuzzy_match, 
    axis=1, 
    df_to_match=ban, 
    columns_to_match=columns
)



""" 
À partir d'ici, nous pouvons tester si les coordonnées géographiques de l'adresse proposée 
par le scoring correspond à celle donnée initialement.

Coordonnées à tester 
"""
x_target = 55.29095302
y_target = -21.10194837    

# Calculer la distance euclidienne pour chaque point
ban['distance'] = np.sqrt((ban['lon'] - x_target)**2 + (ban['lat'] - y_target)**2)

# Trouver la ligne avec la distance minimale
closest_row = ban.loc[ban['distance'].idxmin()]

# Récupérer le nom de la voie
closest_nom_voie = closest_row['nom_voie']

#print(f"Le nom de la voie la plus proche est : {closest_nom_voie}")
closest_nom_voie