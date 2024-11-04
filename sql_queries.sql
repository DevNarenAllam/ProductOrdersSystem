
CREATE USER 'naren'@'%' IDENTIFIED BY 'Python#123';
GRANT ALL PRIVILEGES ON *.* TO 'naren'@'%';
FLUSH PRIVILEGES;
CREATE DATABASE sample;
CREATE TABLE users (
        id INTEGER NOT NULL AUTO_INCREMENT, 
        name VARCHAR(50) NOT NULL, 
        email VARCHAR(50) NOT NULL, 
        phone VARCHAR(20), 
        date_of_birth DATE, 
        registered_on DATE NOT NULL, 
        hashed_password VARCHAR(50) NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (email), 
        UNIQUE (phone)
)AUTO_INCREMENT=1001