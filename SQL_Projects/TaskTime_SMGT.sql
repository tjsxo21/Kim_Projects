-- CREATING TASK MGT TABLE
CREATE TABLE taskmgt(
    id INT AUTO_INCREMENT PRIMARY KEY,
    task VARCHAR(100),
    category VARCHAR(100)
);

-- CREATING TIME MGT TABLE
CREATE TABLE timemgt(
    id INT AUTO_INCREMENT PRIMARY KEY,
    hours INT
);

-- CREATING STATE MGT TABLE
CREATE TABLE statemgt(
    id INT AUTO_INCREMENT PRIMARY KEY,
    overall_rating DECIMAL(2,1),
    timemgt_id INT,
    taskmgt_id INT,
    FOREIGN KEY(timemgt_id) REFERENCES timemgt(id),
    FOREIGN KEY(taskmgt_id) REFERENCES taskmgt(id)
);

-- INSERTING SAMPLE DATA
INSERT INTO taskmgt (task, category) VALUES
    ('Homework', 'School'),('Engineering', 'Job'),('Python/SQL Project', 'Skill Dev'),('Research', 'Other'),('Movie', 'Hobby'),('Movie','Hobby');
   
INSERT INTO timemgt (hours) VALUES
    (40), (25), (20), (10), (2), (2);
    
INSERT INTO statemgt(taskmgt_id, timemgt_id, overall_rating) VALUES
    (1, 1, 8.0), (1, 2, 4.0), (1, 3, 7.5), 
    (2, 3, 8.0), (2, 4, 4.0), (2, 5, 7.5),
    (3, 3, 7.0),
    (4, 4, 7.0), 
    (5, 5, 6.5), (5, 6, 6.5),
    (6, 5, 4.0);

-- Join Tables
SELECT * FROM taskmgt
JOIN statemgt
    ON taskmgt.id = statemgt.taskmgt_id;
    
SELECT * FROM timemgt
JOIN statemgt
    ON timemgt.id = statemgt.timemgt_id;
    
SELECT
    taskmgt.id,
    task,
    overall_rating
FROM taskmgt
JOIN statemgt
    ON taskmgt.id = statemgt.taskmgt_id;
-- ORDER BY avg_concentration; (DNW:Doesn't Work)
-- GROUP BY taskmgt.id; (DNW:Doesn't Work)
--  AVG(overall_rating) avg_overallrating

SELECT
    timemgt.id,
    hours,
    overall_rating
FROM timemgt
JOIN statemgt
    ON timemgt.id = statemgt.timemgt_id;

-- JOIN 3 Tables
SELECT 
    task,
    category,
    hours,
    overall_rating
FROM taskmgt
INNER JOIN statemgt   
    ON taskmgt.id = statemgt.taskmgt_id
INNER JOIN timemgt
    ON timemgt.id = statemgt.timemgt_id;