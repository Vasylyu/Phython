use mans_friends;

CREATE TABLE man_is_friends
(
id int auto_increment not null primary key,
Pets VARCHAR(45) NOT NULL,
Pack_animals VARCHAR(45) NOT NULL
);

INSERT INTO man_is_friends (Pets, Pack_animals)
VALUES ('собаки', 'лошади'),
('кошки', 'верблюды'),
('хомяки', 'ослы');



CREATE TABLE dogs
(
id int auto_increment not null primary key,
name VARCHAR(45) NOT NULL,
comands VARCHAR(45) NOT NULL,
date_of_birth date
);

INSERT INTO dogs (name, comands, date_of_birth)
VALUES ('Шарик', 'приносить палку', '2023-11-23'),
 ('Жучка', 'подавать голос', '2022-12-30'),
 ('Федя', 'сторожить тапок', '2023-08-16');
 

 
 
 CREATE TABLE cats
(
id int auto_increment not null primary key,
name VARCHAR(45) NOT NULL,
comands VARCHAR(45) NOT NULL,
date_of_birth date
);

INSERT INTO cats (name, comands, date_of_birth)
VALUES ('Машка', 'лизать лапу', '2023-04-23'),
 ('Пушок', 'мяукать громко', '2024-11-30'),
 ('Муся', 'царапать диван', '2021-09-23');
 
 
 
 CREATE TABLE hamsters
(
id int auto_increment not null primary key,
name VARCHAR(45) NOT NULL,
comands VARCHAR(45) NOT NULL,
date_of_birth date
);

INSERT INTO hamsters (name, comands, date_of_birth)
VALUES ('Лариска', 'бегать в кольце', '2024-01-20'),
 ('Пуся', 'бить в колокольчик', '2024-06-24'),
 ('Толя', 'громко пищать', '2023-12-28');
 


 CREATE TABLE horses
(
id int auto_increment not null primary key,
name VARCHAR(45) NOT NULL,
comands VARCHAR(45) NOT NULL,
date_of_birth date
);

 INSERT INTO horses (name, comands, date_of_birth)
VALUES ('Спирит', 'бегать в манеже', '2019-02-20'),
 ('Матильда', 'громко ржать', '2018-04-19'),
 ('Геракл', 'быстро скокать', '2019-06-18');
 
 
  CREATE TABLE camels
(
id int auto_increment not null primary key,
name VARCHAR(45) NOT NULL,
comands VARCHAR(45) NOT NULL,
date_of_birth date
);

 INSERT INTO camels (name, comands, date_of_birth)
VALUES ('Вован', 'плеваться далеко', '2019-09-23'),
 ('Верочка', 'громко чавкать', '2016-01-21'),
 ('Витек', 'быстро есть и пить', '2017-11-30');
 
 
  CREATE TABLE donkeys
(
id int auto_increment not null primary key,
name VARCHAR(45) NOT NULL,
comands VARCHAR(45) NOT NULL,
date_of_birth date
);

 INSERT INTO donkeys (name, comands, date_of_birth)
VALUES ('Степан', 'возить далеко', '2021-07-03'),
 ('Сара', 'везти тяжелое', '2020-04-11'),
 ('Самсон', 'улыбаться', '2022-03-24');
 
select * from man_is_friends;
select * from dogs;
select * from cats;
select * from hamsters;
 
select * from horses;
select * from camels;
select * from donkeys



 
 

 












