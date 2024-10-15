SELECT DISTINCT Employe.Nom_personnel, Employe.Prenom_personnel
FROM Employe
JOIN Capteur ON Employe.id_personnel = Capteur.id_personnel
JOIN Identifier ON Capteur.id_capteur = Identifier.id_capteur
JOIN Gaz ON Identifier.id_gaz = Gaz.id_gaz
WHERE Gaz.Type_gaz IN ('NH3', 'CO2 non bio','CH4');

