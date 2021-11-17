-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT UNIQUE PRIMARY KEY AUTO_INCREMENT,
	state_id INT NOT NULL , FOREIGN KEY (state_id) REFERENCES states(id),
	name VARCHAR(256) NOT NULL);

