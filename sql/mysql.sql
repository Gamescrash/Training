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
SELECT name, MAX(aisle) FROM grocieries;


-- ///////////////////////////////////////

CREATE TABLE exercise_logs 
(id INTEGER PRIMARY KEY AUTOINCREMENT,
type TEXT,
minutes INTEGER,
calories INTEGER,
heart_rate INTEGER);

INSERT INTO exercise_logs (type, minutes, calories, heart_rate)
VALUES ("biking", 30, 115, 110);
INSERT INTO exercise_logs (type, minutes, calories, heart_rate)
VALUES ("biking", 60, 200, 120);
INSERT INTO exercise_logs (type, minutes, calories, heart_rate)
VALUES ("biking", 120, 260, 125);
INSERT INTO exercise_logs (type, minutes, calories, heart_rate)
VALUES ("dancing", 50, 90, 99);
INSERT INTO exercise_logs (type, minutes, calories, heart_rate)
VALUES ("dancing", 45, 80, 108);
INSERT INTO exercise_logs (type, minutes, calories, heart_rate)
VALUES ("hiking", 200, 270, 150);
INSERT INTO exercise_logs (type, minutes, calories, heart_rate)
VALUES ("rowing", 150, 210, 200);
INSERT INTO exercise_logs (type, minutes, calories, heart_rate)
VALUES ("bowling", 20, 45, 105);

SELECT * FROM exercise_logs;

SELECT type, SUM(calories) AS total_calories FROM exercise_logs
    GROUP BY type
    HAVING total_calories > 250
    ;

SELECT type, AVG(calories) as avg_calories FROM exercise_logs
    GROUP BY type
    HAVING avg_calories > 70;