import random
import csv

# Liste des secteurs
secteurs = ['energie', 'transport', 'agriculture', 'textile', 'industrie', 'construction']

# Nombre de choix à faire
nombre_choix = 50

# Nom du fichier CSV de sortie
nom_fichier_csv = 'secteurs_choisis.csv'

# Effectuer les choix aléatoires et les stocker dans une liste
choix = [random.choice(secteurs) for _ in range(nombre_choix)]

# Écriture des choix dans le fichier CSV
with open(nom_fichier_csv, 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerow(['Secteur'])
    for secteur in choix:
        writer.writerow([secteur])

print(f"{nombre_choix} secteurs ont été choisis aléatoirement et enregistrés dans le fichier '{nom_fichier_csv}'.")
