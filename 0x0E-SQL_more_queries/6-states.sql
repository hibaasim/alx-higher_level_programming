-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
        (id INT UNIQUE NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(id),
        name NOT NULL VARCHAR(256));
