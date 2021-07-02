CREATE SCHEMA IF NOT EXISTS nathaniel_palmer;

USE nathaniel_palmer;

CREATE TABLE IF NOT EXISTS store_doctors (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	specialization VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS maladies (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS animal_breed (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(150) NOT NULL
);

CREATE TABLE IF NOT EXISTS store_animals (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	doctorId INT REFERENCES store_doctors(id),
	maladyId INT REFERENCES maladies(id),
	breedId INT REFERENCES animal_breed(id)
);


SHOW TABLES;

INSERT INTO store_doctors 
	(name, specialization)
VALUES
	('Stephen Vincent Strange', 'Finding Purpose'),
	('Lucas Fox', 'Intellect'),
	('Silas Wetherbi', 'Humor Improvement'),
	('Gardenia Orellana', 'Beauty'),
	('Pop Eye', 'Strength');

INSERT INTO maladies
	(name)
VALUES
	('Sad Eyes'),
	('Hair Straggles'),
	('Leg Wobbles'),
	('Barks at Everythings'),
	('Sleeping too Much');

INSERT INTO animal_breed
	(name)
VALUES
	('German Shepard'),
	('Pomeranian'),
	('Australian Shepard'),
	('Poodle'),
	('Great Dane');

INSERT INTO store_animals 
	(name, doctorId, maladyId, breedId)
VALUES
	('Timothy', 1, 5, 5),
	('Fredrick', 5, 3, 4),
	('Lucille', 4, 2, 3),
	('Mo', 2, 4, 2),
	('Spot', 1, 1, 3),
	('Steel', 2, 3, 4),
	('Wolfie', 5, 2, 3),
	('Mike', 3, 4, 1),
	('Pookie', 1, 2, 3),
	('Cliffard', 2, 3, 1);
	
-- general print out of tables
SELECT * FROM store_animals sa ;

SELECT * FROM store_animals;
-- prints out the id of a given doctor name
SELECT name, id FROM store_doctors WHERE name LIKE 'Gardenia Orellana';

-- shows all dog and malady names for given doctor ID
SELECT 
	store_animals.name, maladies.name
FROM 
	store_animals
LEFT JOIN 
	maladies
ON
	store_animals.doctorId = maladies.id
WHERE store_animals.doctorId LIKE 4;

-- shows all dog and malady names for given doctor name
SELECT 
	store_animals.name, maladies.name
FROM 
	store_animals
LEFT JOIN 
	maladies
ON
	store_animals.doctorId = maladies.id
LEFT JOIN
	store_doctors
ON
	store_animals.doctorId = store_doctors.id 
WHERE store_doctors.name LIKE 'Gardenia Orellana';

-- Shows all possible combinations of dog names and maladies 
-- ignore the actual malady stored with each dog
-- tip: number of rows should be dogs times maladies
SELECT store_animals.name, maladies.name
FROM store_animals
JOIN maladies
ON TRUE;


