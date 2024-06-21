CREATE TABLE grocieries (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER );
INSERT INTO grocieries VALUES (1, "Bananas", 4);
INSERT INTO grocieries VALUES (2, "Peanut Butter", 1);
INSERT INTO grocieries VALUES (3, "Dark chocolate bars", 2);

-- modifica tabella
ALTER TABLE grocieries ADD aisle INTEGER;

UPDATE grocieries SET aisle = 7 WHERE id = 1;
UPDATE grocieries SET aisle = 4 WHERE id = 2;
UPDATE grocieries SET aisle = 5 WHERE id = 3;


--Table visual
SELECT * FROM grocieries ORDER BY aisle;


--Aggregating data
SELECT SUM(aisle) FROM grocieries;
SELECT MAX(aisle) FROM grocieries;
SELECT name, SUM(aisle) FROM grocieries GROUP BY aisle;