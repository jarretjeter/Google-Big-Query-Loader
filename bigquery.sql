-- I would have liked to do queries such as finding the longest lived emperor, or the longest/shortest reign, but the datetime values of the Birth, Death, Reign_Start and Reign_End columns were too much trouble to transform at the moment.

-- Get a look at the whole table
SELECT * FROM `deb-01-346205.bq_code_review.roman_emperors`;

-- Combine Birth_City and Birth_Province columns to return a new column called Birth_Location
SELECT *, CONCAT(Birth_City, ", ", Birth_Province) as Birth_Location
FROM `deb-01-346205.bq_code_review.roman_emperors`
ORDER BY index ASC;

-- Order emperors by their Succession column to find how they achieved power
SELECT Name, Full_Name, Succession 
FROM `deb-01-346205.bq_code_review.roman_emperors`
ORDER BY Succession ASC;

-- Get all emperors who were elected into power
SELECT *
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Succession LIKE "%Election%"
ORDER BY index ASC;

-- Selecting all the emperors that died of assassination;
SELECT Name, Full_Name, Succession, Cause 
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Cause LIKE "Assassination";

-- Which emperors stole power and had it stolen by deadly means?
SELECT Name, Full_Name, Succession, Cause 
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Succession LIKE "%Seized%" AND Cause LIKE "%Assassination%";

-- Finding the most common cause of death. No surprise!
-- I'm selecting the Cause column and then counting the most occurring value in Cause, aliasing this column as Incidents and ordering by it
SELECT Cause, COUNT(Cause) AS `Incidents`
FROM `deb-01-346205.bq_code_review.roman_emperors`
GROUP BY Cause
ORDER BY Incidents DESC
LIMIT 1;

-- What emperors died of "natural" causes?
SELECT *
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Cause Like "%Natural%";

-- What emperors have verified information?
SELECT *
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Verif NOT LIKE "0";