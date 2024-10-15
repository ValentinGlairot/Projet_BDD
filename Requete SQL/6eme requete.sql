SELECT C.secteur_activite, SUM(D.valeur_donnee) AS Total_emissions
FROM Donnee D
INNER JOIN Capteur C ON D.id_capteur = C.id_capteur
INNER JOIN Adresse A ON C.id_adresse = A.id_adresse
INNER JOIN Region R ON A.id_region = R.id_region
WHERE R.Nom_region = 'Ile de France'
GROUP BY C.secteur_activite
ORDER BY Total_emissions DESC;



