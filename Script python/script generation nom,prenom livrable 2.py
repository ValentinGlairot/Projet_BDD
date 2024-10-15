import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Initialisation de Faker
fake = Faker('fr_FR')

# Génération des données
num_rows = 200
data = {
    'Nom_personnel': [fake.last_name() for _ in range(num_rows)],
    'Prenom_personnel': [fake.first_name_male() if fake.boolean() else fake.first_name_female() for _ in range(num_rows)],
    'Date_naissance': [fake.date_of_birth(minimum_age=18, maximum_age=64).strftime('%Y-%m-%d') for _ in range(num_rows)],
    'Date_fonction': [fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d') for _ in range(num_rows)]
}

# Création du DataFrame
df = pd.DataFrame(data)

# Export vers un fichier Excel
excel_filename = 'donnees_personnelles.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Données exportées vers {excel_filename}")
