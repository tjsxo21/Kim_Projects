SET SQL_SAFE_UPDATES = 0;
DROP database IF EXISTS dating_app;
CREATE database dating_app;
USE dating_app;
-- TO DO
-- preferences (free), advanced preferences

CREATE TABLE user_profile(
	id INT auto_increment PRIMARY KEY,
	username VARCHAR(10) UNIQUE NOT NULL,
    gender CHAR(1) NOT NULL,
    name VARCHAR(20) NOT NULL, 
    age INTEGER NOT NULL,
    height INTEGER,
    ethnicity VARCHAR(20),
    school VARCHAR(20),
    workplace VARCHAR(20),
    jobtitle VARCHAR(20),
    religion VARCHAR(20),
    politics VARCHAR(20),
    dating_goals VARCHAR(20),
    sexual_preferences VARCHAR(10)
);

INSERT INTO user_profile(username, gender, name, age, height, ethnicity, school, workplace, jobtitle, religion, politics, dating_goals, sexual_preferences) VALUES
('abc12','M','Mike Hard',27,170,'Asian','Harvard','Google','Software Engineer','Agnostic','Liberal','Casual','Straight'),
('abc23','F','Sarah Go',30,176,'White','Berkley','Walmart','Sales Manager','Christian','Conservative','Casual','Bisexual'),
('za23','F','Molly Holly',35,180,'White','Virginia Tech','Amazon','Data Engineer','Buddhist','Moderate','Relationship','Straight'),
('we2','M','Bobby Smith',40,177,'African American','Caltech','Microsoft','Cloud Engineer','Catholic','Liberal','Casual','Bisexual');

CREATE TABLE male_profile AS SELECT * FROM user_profile WHERE gender = 'M';
CREATE TABLE female_profile AS SELECT * FROM user_profile WHERE gender = 'F';
CREATE TABLE preferences AS SELECT id, gender, age, height, ethnicity, religion, dating_goals, sexual_preferences FROM user_profile;

-- These two should match
SELECT * FROM male_profile WHERE sexual_preferences = 'Straight';
SELECT * FROM female_profile WHERE sexual_preferences = 'Straight';
SELECT @@ServerName