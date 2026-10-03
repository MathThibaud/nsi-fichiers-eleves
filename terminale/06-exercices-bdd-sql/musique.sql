-- ============================================================
--  Base de donnees "musique" -- feuille d'exercices SQL
--  A tester dans la console SQL de Basthon :
--    https://console.basthon.fr/?kernel=sql
--  1) copier-coller TOUT ce script puis l'executer (Entree) ;
--  2) taper ensuite vos propres requetes SELECT / UPDATE / ...
-- ============================================================

CREATE TABLE artiste (
    id   INTEGER PRIMARY KEY,
    nom  TEXT,
    pays TEXT
);

CREATE TABLE chanson (
    id         INTEGER PRIMARY KEY,
    titre      TEXT,
    id_artiste INTEGER,   -- cle etrangere -> artiste.id
    annee      INTEGER,
    duree      INTEGER,   -- duree en secondes
    streams    INTEGER    -- nombre d'ecoutes, en millions
);

INSERT INTO artiste (id, nom, pays) VALUES
    (1, 'Daft Punk', 'France'),
    (2, 'Stromae',   'Belgique'),
    (3, 'Adele',     'Royaume-Uni'),
    (4, 'Angèle',    'Belgique');

INSERT INTO chanson (id, titre, id_artiste, annee, duree, streams) VALUES
    (1,  'One More Time',       1, 2000, 320,  450),
    (2,  'Get Lucky',           1, 2013, 369,  900),
    (3,  'Instant Crush',       1, 2013, 337,  600),
    (4,  'Alors on danse',      2, 2009, 216,  700),
    (5,  'Papaoutai',           2, 2013, 232,  850),
    (6,  'Formidable',          2, 2013, 197,  500),
    (7,  'Someone Like You',    3, 2011, 285,  950),
    (8,  'Hello',               3, 2015, 295, 1000),
    (9,  'Balance ton quoi',    4, 2018, 191,  400),
    (10, 'Bruxelles je t''aime',4, 2021, 200,  300);
