# drop database python_imdb;
create database python_imdb
default character set utf8
collate utf8_polish_ci;

use python_imdb;

select host, user from mysql.user;
# DROP USER  'python_user_table'@'localhost';

#############
create user 'python_admin'@'localhost' identified by 'admin';
grant SELECT, INSERT, UPDATE, DELETE  on python_imdb.* to 'python_admin'@'localhost';
flush privileges;
#############


drop table actor;
create table actor (
ID int  not null auto_increment,
FirstName varchar(100) not null,
LastName varchar(100) not null,
Nationality varchar(5),
primary key(ID)
);

drop table director;
create table director (
ID int not null auto_increment,
FirstName varchar(100) not null,
LastName varchar(100) not null,
Nationality varchar(5),
primary key(ID)
);

drop table genre;
create table genre (
ID int not null auto_increment,
GenreName varchar(100),
primary key(ID)
);

drop table film;
create table film (
ID int not null auto_increment,
Title varchar(100),
OriginTitle varchar(100),
DirectorID int,
RelYear int,
DurationMins int,
Ranking int,
Voters int,
Rating float,
primary key(ID),
foreign key (DirectorID) references director(ID)
);

drop table film_has_genre;
create table film_has_genre (
ID int not null auto_increment,
FilmID int not null,
GenreID int not null,
foreign key (FilmID) references film(ID),
foreign key (GenreID) references genre(ID),
primary key(id)
);

drop table actor_in_film;
create table actor_in_film (
id int  not null auto_increment,
FilmID int not null,
ActorID int not null,
foreign key (FilmID) references film(ID),
foreign key (ActorID) references actor(ID),
primary key(id)
);

select * from actor;
select * from director;
select * from genre;
select * from film;
select * from film_has_genre;
select * from actor_in_film;

delete from film_has_genre where id>0;
delete from actor_in_film where id>0;
delete from film where id>0;
delete from actor where id>0;
delete from genre where id>0;
delete from director where id>0;


select
f.title,
f.OriginTitle,
f.RelYear,
f.DurationMins,
f.Ranking,
f.Voters,
a.FirstName,
a.LastName,
d.FirstName,
d.LastName,
g.GenreName
from
film f
join actor_in_film af on f.ID = af.filmID
join actor a on a.ID = af.actorID
join director d on f.DirectorID = d.ID
join film_has_genre fg on f.ID = fg.filmID
join genre g  on fg.GenreID = g.ID;

