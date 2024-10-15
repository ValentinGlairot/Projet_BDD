import random
import csv
from datetime import datetime, timedelta

# Fonction pour générer une date aléatoire au format JJ-MM-AAAA
def generate_random_date():
    start_date = datetime(2004, 1, 1)
    end_date = datetime.now()
    random_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.strftime("%d-%m-%Y")  # Correction du séparateur de date

# Générer 200 dates aléatoires au format JJ-MM-AAAA
random_dates = [generate_random_date() for _ in range(200)]

# Nom du fichier CSV de sortie
csv_filename = 'dates_aleatoires.csv'

# Écriture des données dans le fichier CSV
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Dates aléatoires'])
    for date in random_dates:
        writer.writerow([date])

print(f"Données exportées vers {csv_filename}")
