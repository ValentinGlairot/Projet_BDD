import pandas as pd
from faker import Faker
import random

# Initialisation de Faker
fake = Faker('fr_FR')

# Génération des données
num_rows = 200
data = {
    'Numero_rue': [random.randint(1, 50) for _ in range(num_rows)],
    'Nom_rue': [fake.street_name() for _ in range(num_rows)],
    'Code_postal': [fake.postcode() for _ in range(num_rows)],
    'Nom_ville': [fake.city() for _ in range(num_rows)]
}

# Création du DataFrame
df = pd.DataFrame(data)

# Export vers un fichier Excel
excel_filename = 'coordonnees_francaises.xlsx'
df.to_excel(excel_filename, index=False)

print(f"Données exportées vers {excel_filename}")
