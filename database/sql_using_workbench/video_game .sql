create database video_game;
use video_game;

-- create table structure statements begin here --

create table category
(
	categoryId		int(3)	auto_increment,
	categoryName	varchar(15)	not null,
	primary key (categoryId)
);

create table console
(
	consoleId		int(3)	auto_increment,
	consoleName		varchar(15)	not null,
	primary key (consoleId)
);

create table game_titles
(
	gameId		int(4)	auto_increment,
	title		varchar(40)	not null,
	cond		varchar(12),
	game_type	varchar(10)	not null,
	game_inst	char(1)	not null,
	game_box	char(1)	not null,
	consoleId	int(3),
	categoryId	int(3),
	primary key (gameId),
	foreign key (categoryId) references category(categoryId),
	foreign key (consoleId) references console(consoleId)
);

create table game_finance
(
	gameId				int(4),
	purchasePrice		decimal(5,2)	not null,
	gameMV				decimal(5,2)	not null,
	dateOfPurchase		date			not null,
	primary key (gameId)
);

alter table game_finance add foreign key (gameId) references game_titles(gameId) on delete cascade;

-- create table structure statements end here --
select * from console;
select * from category;
select * from game_titles;
select * from game_finance;
commit;
-- insert data instructions begin here --

INSERT INTO `video_game`.`console` (`consoleId`, `consoleName`) VALUES ('1', 'Nintendo');
INSERT INTO `video_game`.`console` (`consoleId`, `consoleName`) VALUES ('2', 'PlayStation');
INSERT INTO `video_game`.`console` (`consoleId`, `consoleName`) VALUES ('3', 'Sega');
INSERT INTO `video_game`.`console` (`consoleId`, `consoleName`) VALUES ('4', 'Xbox');
INSERT INTO `video_game`.`console` (`consoleId`, `consoleName`) VALUES ('5', 'Atari');

INSERT INTO `video_game`.`category` (`categoryId`, `categoryName`) VALUES ('1', 'Action');
INSERT INTO `video_game`.`category` (`categoryId`, `categoryName`) VALUES ('2', 'RPG');
INSERT INTO `video_game`.`category` (`categoryId`, `categoryName`) VALUES ('3', 'Sports');
INSERT INTO `video_game`.`category` (`categoryId`, `categoryName`) VALUES ('4', 'Adventure');
-- insert data instructions end here --

-- importing data from the csv file to our table --

load data local infile 'G:\video_game.csv' into table game_titles fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(gameId,title,cond,game_type,game_inst,game_box,consoleId,categoryId );

load data local infile 'G:\game_finance.csv' into table game_finance fields terminated by ','
enclosed by '"'
lines terminated by '\n'
(gameId,purchasePrice,gameMV,dateOfPurchase);

-- importing statements end --
-- first
select  g.title, c.consoleName   from game_titles g, console c
where c.consoleId = g.consoleId;

-- second
select title from game_titles group by title having count(title) > 1;

-- third
select sum(gameMV) as total_cost from game_finance;

-- fourth
select 
IF(game_inst = "N" or game_box = "N", title,'') as incomplete_games,
IF(game_inst = "Y" and game_box = "Y", title,'') as complete_games
from game_titles;

-- five
select g.title from game_titles g, game_finance f 
where g.gameId = f.gameId and 
f.gameMV = (select max(gameMV) from game_finance);

-- sixth
select g.title from game_titles g , game_finance f
where g.gameId = f.gameId and 
f.purchasePrice < f.gameMV;

-- seventh
select g.title, (f.gameMV - f.purchasePrice) as increase_value 
from game_titles g ,game_finance f
where g.gameId = f.gameId and 
(f.gameMV - f.purchasePrice) = (select max(gameMV - purchasePrice) from game_finance);