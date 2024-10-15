SELECT R.Nom_region
FROM Region R
JOIN ( SELECT Ad.id_region, COUNT(DISTINCT C.id_capteur) AS nb_capteurs, COUNT(DISTINCT A.id_agence) AS nb_agences
       FROM Adresse Ad
       LEFT JOIN Agence A ON Ad.id_adresse = A.id_adresse
	   LEFT JOIN Capteur C ON Ad.id_adresse = C.id_adresse
       GROUP BY Ad.id_region) AS T ON R.id_region = T.id_region
WHERE 
    T.nb_capteurs > T.nb_agences;
