import random
import csv

# Générer 100 nombres aléatoires entre 1 et 13
random_numbers = [random.randint(1, 100) for _ in range(200)]

# Créer une liste de listes contenant les nombres choisis
data = [[number] for number in random_numbers]

# Nom du fichier CSV de sortie
csv_filename = 'nombres_aleatoires.csv'

# Écriture des données dans le fichier CSV
with open(csv_filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Nombre aléatoire'])
    writer.writerows(data)

print(f"Données exportées vers {csv_filename}")
