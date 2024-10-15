import csv
import random
from faker import Faker

fake = Faker()

# Génération des données pour chaque table
gaz_data = sorted([(i+1, fake.word(), fake.word()) for i in range(200)], key=lambda x: x[0])
region_data = sorted([(i+1, fake.city()) for i in range(200)], key=lambda x: x[0])
rapport_data = sorted([(i+1, fake.sentence(), fake.date_between(start_date='-1y', end_date='today'), 
                fake.date_between(start_date='-1y', end_date='today'), random.randint(1, 100)) for i in range(200)], key=lambda x: x[0])
fonction_data = sorted([(i+1, fake.job()) for i in range(200)], key=lambda x: x[0])
adresse_data = sorted([(i+1, fake.random_int(min=1, max=9999), fake.street_name(), fake.random_int(min=10000, max=99999), 
                fake.city(), random.randint(1, 200)) for i in range(200)], key=lambda x: x[0])
agence_data = sorted([(i+1, fake.company(), random.randint(1, 200)) for i in range(200)], key=lambda x: x[0])
employe_data = sorted([(i+1, fake.last_name(), fake.first_name(), fake.date_of_birth(), random.randint(1, 200)) for i in range(200)], key=lambda x: x[0])
capteur_data = sorted([(i+1, fake.word(), random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)) for i in range(200)], key=lambda x: x[0])
donnee_data = sorted([(i+1, round(random.uniform(0, 100), 2), fake.date_between(start_date='-1y', end_date='today'), 
                random.randint(1, 200)) for i in range(200)], key=lambda x: x[0])
ecriture_data = sorted([(random.randint(1, 200), random.randint(1, 200)) for _ in range(200)], key=lambda x: x[0])
contenir_data = sorted([(random.randint(1, 200), random.randint(1, 200)) for _ in range(200)], key=lambda x: x[0])
travail_data = sorted([(random.randint(1, 200), random.randint(1, 200)) for _ in range(200)], key=lambda x: x[0])
identifier_data = sorted([(random.randint(1, 200), random.randint(1, 200)) for _ in range(200)], key=lambda x: x[0])
possede_data = sorted([(random.randint(1, 200), random.randint(1, 200), fake.date_between(start_date='-1y', end_date='today')) for _ in range(200)], key=lambda x: x[0])

# Regrouper toutes les données dans une seule liste de listes
all_data = [gaz_data, region_data, rapport_data, fonction_data, adresse_data, agence_data,
            employe_data, capteur_data, donnee_data, ecriture_data, contenir_data,
            travail_data, identifier_data, possede_data]

# Écrire les données dans un fichier CSV
with open('all_data_1.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for data in all_data:
        writer.writerows(data)
