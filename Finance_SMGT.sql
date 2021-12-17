-- CREATE TABLE incomemgt
CREATE TABLE incomemgt(
    month INT,
    year INT,
    monthly_income DECIMAL(6,2)
);

-- CREATE TABLE expensemgt
CREATE TABLE expensemgt(
    month INT,
    year INT,
    expense decimal(6,2),
    category VARCHAR(100)
);

-- INSERT SAMPLE DATA
INSERT INTO incomemgt(month, year, monthly_income) VALUES
(1,2020,3300.50),(2,2020,3000.00),(3,2020,3250.75),(4,2020,3500.00),(5,2020,4000.00),(6,2020,3500.80),
(7,2020,2800.50),(8,2020,2000.00),(9,2020,2300.75),(10,2020,3000.00),(11,2020,3900.00),(12,2020,4000.80),
(1,2021,3300.50),(2,2021,3000.00),(3,2021,3250.75),(4,2021,3500.00),(5,2021,4000.00),(6,2021,3500.80),
(7,2021,3800.50),(8,2021,3000.00),(9,2021,3300.75),(10,2021,3000.00),(11,2021,3900.00),(12,2021,4000.80);

INSERT INTO expensemgt(month, year, expense, category) VALUES
-- 2020 Sample Data
(1,2020,400.00,'rent'),(1,2020,210.50,'utilities'),(1,2020,330.75,'grocery'),(1,2020,250.00,'extra'),
(2,2020,400.00,'rent'),(2,2020,210.50,'utilities'),(2,2020,330.75,'grocery'),(2,2020,250.00,'extra'),
(3,2020,400.00,'rent'),(3,2020,210.50,'utilities'),(3,2020,330.75,'grocery'),(3,2020,250.00,'extra'),
(4,2020,400.00,'rent'),(4,2020,210.50,'utilities'),(4,2020,330.75,'grocery'),(4,2020,250.00,'extra'),
(5,2020,400.00,'rent'),(5,2020,210.50,'utilities'),(5,2020,330.75,'grocery'),(5,2020,250.00,'extra'),
(6,2020,400.00,'rent'),(6,2020,210.50,'utilities'),(6,2020,330.75,'grocery'),(6,2020,250.00,'extra'),
(7,2020,400.00,'rent'),(7,2020,210.50,'utilities'),(7,2020,330.75,'grocery'),(7,2020,250.00,'extra'),
(8,2020,400.00,'rent'),(8,2020,210.50,'utilities'),(8,2020,330.75,'grocery'),(8,2020,250.00,'extra'),
(9,2020,400.00,'rent'),(9,2020,210.50,'utilities'),(9,2020,330.75,'grocery'),(9,2020,250.00,'extra'),
(10,2020,400.00,'rent'),(10,2020,210.50,'utilities'),(10,2020,330.75,'grocery'),(10,2020,250.00,'extra'),
(11,2020,400.00,'rent'),(11,2020,210.50,'utilities'),(11,2020,330.75,'grocery'),(11,2020,250.00,'extra'),
(12,2020,400.00,'rent'),(12,2020,210.50,'utilities'),(12,2020,330.75,'grocery'),(12,2020,250.00,'extra'),
-- 2021 Sample Data
(1,2021,500.00,'rent'),(1,2021,300.50,'utilities'),(1,2021,310.75,'grocery'),(1,2021,220.00,'extra'),
(2,2021,550.00,'rent'),(2,2021,250.00,'utilities'),(2,2021,240.35,'grocery'),(2,2021,150.00,'extra'),
(3,2021,500.00,'rent'),(3,2021,300.50,'utilities'),(3,2021,310.75,'grocery'),(3,2021,220.00,'extra'),
(4,2021,550.00,'rent'),(4,2021,250.00,'utilities'),(4,2021,240.35,'grocery'),(4,2021,150.00,'extra'),
(5,2021,500.00,'rent'),(5,2021,300.50,'utilities'),(5,2021,310.75,'grocery'),(5,2021,220.00,'extra'),
(6,2021,550.00,'rent'),(6,2021,250.00,'utilities'),(6,2021,240.35,'grocery'),(6,2021,150.00,'extra'),
(7,2021,500.00,'rent'),(7,2021,300.50,'utilities'),(7,2021,310.75,'grocery'),(7,2021,220.00,'extra'),
(8,2021,550.00,'rent'),(8,2021,250.00,'utilities'),(8,2021,240.35,'grocery'),(8,2021,150.00,'extra'),
(9,2021,500.00,'rent'),(9,2021,300.50,'utilities'),(9,2021,310.75,'grocery'),(9,2021,220.00,'extra'),
(10,2021,550.00,'rent'),(10,2021,250.00,'utilities'),(10,2021,240.35,'grocery'),(10,2021,150.00,'extra'),
(11,2021,500.00,'rent'),(11,2021,300.50,'utilities'),(11,2021,310.75,'grocery'),(11,2021,220.00,'extra'),
(12,2021,NULL,'rent'),(12,2021,NULL,'utilities'),(12,2021,NULL,'grocery'),(12,2021,NULL,'extra');
-- Calculate Max, Min, Sum, Ave
SELECT MAX(expense) from expensemgt WHERE month = 1 AND year = 2021;
SELECT MIN(expense) from expensemgt WHERE month = 1 AND year = 2021;
SELECT SUM(expense) from expensemgt WHERE year = 2021;
SELECT AVG(expense) from expensemgt WHERE category = 'grocery';
-- Subtraction
SELECT
	(SELECT SUM(monthly_income) from incomemgt)
    -
    (SELECT SUM(expense) from expensemgt)
    as total_balance;

SELECT 
    IFNULL(expense, 0) from expensemgt;

-- IF, CASE statements
SELECT 
    IFNULL(expense, 0) from expensemgt;

SELECT
    Round(expense, 1) AS ROUNDED,
    COUNT(expense) AS COUNT
    FROM expensemgt;

SELECT
    IF(expense < 200.00, NULL, expense) AS EXPENSEREPORT
    FROM expensemgt;

SELECT month, year, expense, category
FROM expensemgt WHERE expense IS NULL;
    
SELECT
CASE
    WHEN expense >= 500 THEN 'Above 500'
    WHEN expense >= 300 and expense < 500 THEN 'Above 300'
    ELSE 'Below 300'
END AS EXPENSEANALYSIS
FROM expensemgt;

SELECT
    IF(expense >= 500, 'Above 500', 'Below 500')
FROM expensemgt;

SELECT
IF(expense >= 500)
BEGIN
PRINT('Above 500')
END
FROM expensemgt;

IF(1 = 1_+ 1)
BEGIN
    PRINT 'First If Condition'
END
ELSE IF (1 = 2)
BEGIN   
    PRINT 'Second If Else Block'
END

-- Testing
DECLARE GRADE AS INT;
IF GRADE >= 90
PRINT 'A';
IF GRADE >= 90 and GRADE < 90
PRINT 'B'
ELSE
PRINT 'C or below';