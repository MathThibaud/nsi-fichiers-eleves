-- ============================================================
--  Base de donnees "bibliotheque" -- feuille d'exercices SQL
--  A tester dans la console SQL de Basthon :
--    https://console.basthon.fr/?kernel=sql
--  Copier-coller TOUT ce script, l'executer, puis requeter.
-- ============================================================

CREATE TABLE auteur (
    id   INTEGER PRIMARY KEY,
    nom  TEXT,
    pays TEXT
);

CREATE TABLE livre (
    id        INTEGER PRIMARY KEY,
    titre     TEXT,
    id_auteur INTEGER,   -- cle etrangere -> auteur.id
    annee     INTEGER,
    genre     TEXT
);

CREATE TABLE adherent (
    id     INTEGER PRIMARY KEY,
    nom    TEXT,
    prenom TEXT
);

CREATE TABLE emprunt (
    id           INTEGER PRIMARY KEY,
    id_livre     INTEGER,   -- cle etrangere -> livre.id
    id_adherent  INTEGER,   -- cle etrangere -> adherent.id
    date_emprunt TEXT
);

INSERT INTO auteur (id, nom, pays) VALUES
    (1, 'Orwell',  'Royaume-Uni'),
    (2, 'Camus',   'France'),
    (3, 'Tolkien', 'Royaume-Uni'),
    (4, 'Christie','Royaume-Uni'),
    (5, 'Verne',   'France');

INSERT INTO livre (id, titre, id_auteur, annee, genre) VALUES
    (1, '1984',                             1, 1949, 'SF'),
    (2, 'La Ferme des animaux',             1, 1945, 'Fable'),
    (3, 'L''Étranger',                      2, 1942, 'Roman'),
    (4, 'La Peste',                         2, 1947, 'Roman'),
    (5, 'Le Hobbit',                        3, 1937, 'Fantasy'),
    (6, 'Le Seigneur des anneaux',          3, 1954, 'Fantasy'),
    (7, 'Le Crime de l''Orient-Express',    4, 1934, 'Policier'),
    (8, 'Vingt mille lieues sous les mers', 5, 1870, 'Aventure');

INSERT INTO adherent (id, nom, prenom) VALUES
    (1, 'Martin',  'Julie'),
    (2, 'Bernard', 'Lucas'),
    (3, 'Petit',   'Emma'),
    (4, 'Durand',  'Noah');

INSERT INTO emprunt (id, id_livre, id_adherent, date_emprunt) VALUES
    (1, 1, 1, '2025-01-10'),
    (2, 5, 1, '2025-01-12'),
    (3, 3, 2, '2025-02-01'),
    (4, 6, 3, '2025-02-03'),
    (5, 1, 4, '2025-02-05'),
    (6, 8, 2, '2025-02-10');
