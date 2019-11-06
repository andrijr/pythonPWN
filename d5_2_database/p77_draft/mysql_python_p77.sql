
create database python_p77
default character set utf8
collate utf8_polish_ci;

select host, user from mysql.user;
#DROP USER  'python_admin'@'localhost';

#############
create user 'python_admin'@'localhost' identified by 'admin';
grant SELECT, INSERT, UPDATE, DELETE  on python_p77.* to 'python_admin'@'localhost';
flush privileges;
#############

use python_p77;

drop table python_p77.employees;
create table python_p77.employees (
id_employees int primary key auto_increment,
name varchar(255) not null,
lastname varchar(255) not null,
data_birth DATE ,
data_empl DATETIME  default now(),
pesel_no varchar(255) unique ,
gender enum("M", "K") ,
salary_net double(8,2) ,
active bool default 1
);
INSERT INTO python_p77.employees (id_employees, name, lastname, data_birth, data_empl, pesel_no, gender,  salary_net, active) VALUES
	(default, 'Andrzej1', 'A1', '1980-05-01', '2015-05-01' , '75051522151', 'M', 5000, 1 ),
	(default, 'Andrzej2', 'A2', '1980-05-02', '2015-05-02' , '75051522152', 'K', 6000, 1 ),
	(default, 'Andrzej3', 'A3', '1980-05-03', '2015-05-03' , '75051522153', 'M', 7000, 1 );
select * from python_p77.employees;
# select '12345678901' regexp '^[0-9]{10}[0-9]$';



drop table python_p77.users;
create table python_p77.users (
id_users int primary key auto_increment,
login varchar(255) not null,
password varchar(255) not null,
permission enum("role_admin", "role_moderator", "role_user", 'role_user_table') not null,
active bool default 1,
account_blocking int not null default 0
);
INSERT INTO python_p77.users (id_users, login, password, permission, active, account_blocking) VALUES
	(default, 'python_user_table', 'user_table', 'role_user_table', 1 , 0),
	(default, 'python_admin', 'admin', 'role_admin', 1 , 0),
	(default, 'python_moderator', 'moderator', 'role_moderator', 1 , 0),
	(default, 'python_user', 'user', 'role_user', 1 , 0);
select * from users;
