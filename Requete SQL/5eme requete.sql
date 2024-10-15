SELECT R.Nom_region, SUM(D.valeur_donnee) AS Total_emissions
FROM Donnee D
INNER JOIN Capteur C ON D.id_capteur = C.id_capteur
INNER JOIN Adresse A ON C.id_adresse = A.id_adresse
INNER JOIN Region R ON A.id_region = R.id_region
INNER JOIN Identifier I ON C.id_capteur = I.id_capteur
INNER JOIN Gaz G ON I.id_gaz = G.id_gaz
WHERE YEAR(D.Date_donnee) = 2020
GROUP BY R.Nom_region;
