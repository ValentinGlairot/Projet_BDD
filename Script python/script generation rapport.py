import pandas as pd
from faker import Faker
from datetime import datetime, timedelta
import random

# Initialisation de Faker
fake = Faker('fr_FR')

# Génération des données
num_reports = 100
data = {
    'Nom_rapport': [f"rapport_{i}" for i in range(1, num_reports+1)],
    'Date_publication': [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_reports)],
    'Date_de_modification': [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_reports)],
    'Nombre_de_personne_concerne': [random.randint(1, 6) for _ in range(num_reports)]
}

# Ajuster les dates pour que la date de publication soit toujours supérieure à la date de modification
for i in range(num_reports):
    if data['Date_publication'][i] < data['Date_de_modification'][i]:
        data['Date_publication'][i], data['Date_de_modification'][i] = data['Date_de_modification'][i], data['Date_publication'][i]

# Création du DataFrame
df = pd.DataFrame(data)

# Export vers un fichier Excel
excel_filename = 'rapports.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Données exportées vers {excel_filename}")
