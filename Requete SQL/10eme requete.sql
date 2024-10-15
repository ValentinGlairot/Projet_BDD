SELECT E.Nom_personnel, E.Prenom_personnel, COUNT(R.id_rapport) AS Nombre_de_rapports_ecrits, DATEDIFF(CURDATE(), E.Date_naissance) AS Anciennete_dans_le_poste, COUNT(R.id_rapport) / DATEDIFF(CURDATE(), E.Date_naissance) AS Taux_de_productivite
FROM Employe E
JOIN Ecriture EC ON E.id_personnel = EC.id_personnel
JOIN Rapport R ON EC.id_rapport = R.id_rapport
JOIN Travail T ON E.id_personnel = T.id_personnel
JOIN Agence A ON T.id_agence = A.id_agence
JOIN Adresse Ad ON A.id_adresse = Ad.id_adresse
JOIN Region Re ON Ad.id_region = Re.id_region
WHERE A.Nom_agence = 'Agence_Toulouse'
GROUP BY E.id_personnel
ORDER BY Taux_de_productivite DESC;
