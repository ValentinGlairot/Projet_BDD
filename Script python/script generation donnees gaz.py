import random
import csv

# Fonction pour générer un nombre aléatoire avec trois chiffres après la virgule entre 0,000001 et 700
def generate_random_number():
    return round(random.uniform(0.000001, 700), 3)

# Générer 136 nombres aléatoires avec trois chiffres après la virgule et les stocker dans une liste
random_numbers = [generate_random_number() for _ in range(136)]

# Nom du fichier CSV de sortie
csv_filename = 'nombres_aleatoires.csv'

# Écriture des données dans le fichier CSV
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nombres aléatoires'])
    writer.writerows(map(lambda x: [x], random_numbers))

print(f"Données exportées vers {csv_filename}")
