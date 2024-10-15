SELECT e.Nom_personnel, e.Prenom_personnel
FROM Employe e
JOIN Travail t ON e.id_personnel = t.id_personnel
JOIN Agence a ON t.id_agence = a.id_agence
JOIN Adresse adr ON a.id_adresse = adr.id_adresse
JOIN Region r ON adr.id_region = r.id_region
WHERE a.Nom_agence = 'Agence_Bordeaux';
