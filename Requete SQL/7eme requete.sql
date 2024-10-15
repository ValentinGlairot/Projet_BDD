SELECT r.*
FROM Rapport r
JOIN Contenir c ON r.id_rapport = c.id_rapport
JOIN Donnee d ON c.id_donnee = d.id_donnee
JOIN Capteur cp ON d.id_capteur = cp.id_capteur
JOIN Identifier i ON cp.id_capteur = i.id_capteur
JOIN Gaz g ON i.id_gaz = g.id_gaz
WHERE g.Type_gaz = 'NH3'
ORDER BY r.date_publication;
