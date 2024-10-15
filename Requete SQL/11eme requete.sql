

DELIMITER //
CREATE PROCEDURE getStudentInfo(IN s_name VARCHAR(64))
BEGIN
SELECT R.id_rapport, R.Nom_rapport, R.date_publication, R.Date_de_modification
FROM Rapport R
JOIN Contenir C ON R.id_rapport = C.id_rapport
JOIN Donnee D ON C.id_donnee = D.id_donnee
JOIN Identifier I ON D.id_capteur = I.id_capteur
JOIN Gaz G ON I.id_gaz = G.id_gaz
WHERE G.Type_gaz = s_name;
END//

call getStudentInfo('CH4');