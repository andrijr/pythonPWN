# drop database python_db;
CREATE DATABASE python_db
default character set utf8
collate utf8_polish_ci;

use python_db;

SELECT user, host FROM mysql.user;
#DROP USER  'python_admin'@'localhost';

create user 'python_admin'@'localhost' identified by 'admin';
grant SELECT, INSERT, UPDATE, DELETE  on python_db.* to 'python_admin'@'localhost';
flush privileges;

use python_db;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    birthdate DATE NOT NULL,
    salary DOUBLE(8 , 2 ) NOT NULL,
    gender ENUM('M', 'K')
);

INSERT INTO `python_db`.`users` (`id`, `name`, `lastname`, `birthdate`, `salary`, `gender`) VALUES
	('1', 'Marek', 'Kot', '2000-02-02', '4000', 'M'),
	('2', 'Anna', 'Nowak', '1999-04-02', '3500', 'K'),
	('3', 'Jan', 'Nowy', '1988-02-01', '5000', 'M');

SELECT  * FROM    python_db.users;




