* Get a look at the whole table
SELECT * FROM `deb-01-346205.bq_code_review.roman_emperors`;

# Combine Birth_City and Birth_Province columns
SELECT *, CONCAT(Birth_City, ", ", Birth_Province) as Birth_Location
FROM `deb-01-346205.bq_code_review.roman_emperors`
ORDER BY index ASC;

# Order emperors by how they achieved power
SELECT * 
FROM `deb-01-346205.bq_code_review.roman_emperors`
ORDER BY Succession ASC;

# Get all emperors who were elected into power
SELECT *
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Succession LIKE "%Election%"
ORDER BY index ASC;

# Selecting all the emperors that died of assassination;
SELECT * 
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Cause LIKE "Assassination";

# Finding the most common cause of death. No surprise!
SELECT Cause, COUNT(Cause) AS `Incidents`
FROM `deb-01-346205.bq_code_review.roman_emperors`
GROUP BY Cause
ORDER BY Incidents DESC
LIMIT 1;

# What emperors died of "natural" causes?
SELECT *
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Cause Like "%Natural%";

# What emperors have verified information?
SELECT *
FROM `deb-01-346205.bq_code_review.roman_emperors`
WHERE Verif NOT LIKE "0";