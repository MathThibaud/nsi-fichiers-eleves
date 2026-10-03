-- ============================================================
--  Base de donnees "pays" -- feuille d'exercices SQL
--  A tester dans la console SQL de Basthon :
--    https://console.basthon.fr/?kernel=sql
--  Copier-coller TOUT ce script, l'executer, puis requeter.
-- ============================================================

CREATE TABLE pays (
    id         INTEGER PRIMARY KEY,
    nom        TEXT,
    continent  TEXT,
    capitale   TEXT,
    population INTEGER,   -- en millions d'habitants
    superficie INTEGER    -- en milliers de km2
);

INSERT INTO pays (id, nom, continent, capitale, population, superficie) VALUES
    (1,  'France',    'Europe',   'Paris',     68,  552),
    (2,  'Allemagne', 'Europe',   'Berlin',    84,  358),
    (3,  'Italie',    'Europe',   'Rome',      59,  301),
    (4,  'Espagne',   'Europe',   'Madrid',    48,  506),
    (5,  'Japon',     'Asie',     'Tokyo',    125,  378),
    (6,  'Chine',     'Asie',     'Pékin',   1412, 9597),
    (7,  'Inde',      'Asie',     'New Delhi',1417, 3287),
    (8,  'Brésil',    'Amérique', 'Brasilia', 215, 8516),
    (9,  'Canada',    'Amérique', 'Ottawa',    39, 9985),
    (10, 'Mexique',   'Amérique', 'Mexico',   128, 1964),
    (11, 'Égypte',    'Afrique',  'Le Caire', 109, 1002),
    (12, 'Nigéria',   'Afrique',  'Abuja',    219,  924),
    (13, 'Australie', 'Océanie',  'Canberra',  26, 7692),
    (14, 'Maroc',     'Afrique',  'Rabat',     37,  447);
