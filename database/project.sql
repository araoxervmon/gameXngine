-- phpMyAdmin SQL Dump
-- version 3.5.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 24, 2014 at 01:39 AM
-- Server version: 5.5.24-log
-- PHP Version: 5.3.13

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `project2`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE IF NOT EXISTS `category` (
  `categoryId` int(3) NOT NULL AUTO_INCREMENT,
  `categoryName` varchar(15) NOT NULL,
  PRIMARY KEY (`categoryId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`categoryId`, `categoryName`) VALUES
(1, 'Action'),
(2, 'RPG'),
(3, 'Sports'),
(4, 'Adventure');

-- --------------------------------------------------------

--
-- Table structure for table `console`
--

CREATE TABLE IF NOT EXISTS `console` (
  `consoleId` int(3) NOT NULL AUTO_INCREMENT,
  `consoleName` varchar(15) NOT NULL,
  PRIMARY KEY (`consoleId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `console`
--

INSERT INTO `console` (`consoleId`, `consoleName`) VALUES
(1, 'Nintendo'),
(2, 'PlayStation'),
(3, 'Sega'),
(4, 'Xbox'),
(5, 'Atari');

-- --------------------------------------------------------

--
-- Table structure for table `game_finance`
--

CREATE TABLE IF NOT EXISTS `game_finance` (
  `gameId` int(4) NOT NULL DEFAULT '0',
  `purchasePrice` decimal(5,2) NOT NULL,
  `gameMV` decimal(5,2) NOT NULL,
  `dateOfPurchase` date NOT NULL,
  PRIMARY KEY (`gameId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `game_finance`
--

INSERT INTO `game_finance` (`gameId`, `purchasePrice`, `gameMV`, `dateOfPurchase`) VALUES
(1, '24.99', '26.95', '2007-09-02'),
(2, '3.97', '10.99', '2007-12-12'),
(3, '25.47', '69.99', '2008-01-17'),
(4, '14.97', '46.00', '2008-09-04'),
(5, '4.19', '6.75', '2009-06-10'),
(6, '8.34', '44.95', '2010-07-04'),
(7, '5.99', '27.99', '2007-10-29'),
(8, '11.99', '29.99', '2007-11-21'),
(9, '8.69', '30.00', '2008-08-24'),
(10, '4.95', '12.79', '2008-10-28'),
(11, '8.04', '16.99', '2010-04-13'),
(12, '8.79', '16.24', '2011-03-24'),
(13, '4.46', '6.99', '2011-09-20'),
(14, '6.00', '9.11', '2007-09-28'),
(15, '3.79', '6.99', '2008-03-06'),
(16, '28.00', '36.30', '2008-10-01'),
(17, '3.99', '7.99', '2012-04-24'),
(18, '35.06', '35.06', '2009-04-04'),
(19, '2.04', '6.90', '2012-12-21'),
(20, '9.99', '9.99', '2007-09-21'),
(21, '4.99', '6.00', '2013-03-24'),
(22, '6.00', '10.43', '2007-05-07'),
(23, '5.84', '7.19', '2013-09-03'),
(24, '19.99', '26.00', '2007-09-04'),
(25, '9.97', '13.49', '2011-02-26'),
(26, '10.00', '13.99', '2010-01-02'),
(27, '5.00', '11.99', '2013-12-28'),
(28, '13.00', '15.50', '2010-09-02'),
(29, '5.18', '7.95', '2011-10-30'),
(30, '5.95', '10.76', '2009-10-01'),
(31, '4.12', '4.50', '2010-10-02'),
(32, '4.96', '6.49', '2009-01-03'),
(33, '3.00', '5.60', '2009-05-14'),
(34, '8.99', '11.50', '2007-08-31'),
(35, '2.49', '5.00', '2010-01-23'),
(36, '28.99', '28.99', '2009-10-03'),
(37, '3.69', '3.69', '2007-10-10'),
(38, '2.92', '2.99', '2008-06-13'),
(39, '8.77', '11.00', '2007-05-29'),
(40, '8.25', '9.25', '2012-03-09'),
(41, '30.99', '39.99', '2008-05-10'),
(42, '6.19', '8.09', '2008-11-24'),
(43, '17.00', '18.50', '2009-07-26'),
(44, '19.95', '22.50', '2008-05-07'),
(45, '7.00', '12.99', '2007-01-31'),
(46, '19.95', '19.95', '2013-10-17'),
(47, '16.94', '16.94', '2009-06-12'),
(48, '19.99', '19.99', '2008-06-06'),
(49, '20.50', '22.50', '2007-07-31'),
(50, '10.00', '9.89', '2010-08-12'),
(51, '21.75', '24.95', '2011-03-15'),
(52, '5.50', '5.50', '2008-04-18'),
(53, '25.99', '29.99', '2009-05-08'),
(54, '8.00', '10.50', '2009-07-22'),
(55, '11.99', '25.00', '2010-12-08'),
(56, '123.32', '500.01', '2019-12-01'),
(57, '123.32', '200.00', '2014-12-02'),
(58, '0.00', '0.00', '0000-00-00'),
(59, '100.00', '500.01', '2019-12-01'),
(60, '100.00', '500.01', '2019-12-01'),
(61, '123.32', '500.01', '2014-12-01'),
(62, '123.32', '500.01', '2014-12-01'),
(63, '100.00', '200.00', '2014-12-02'),
(64, '100.00', '200.00', '2014-12-02'),
(65, '123.00', '200.00', '2014-06-10'),
(66, '123.32', '500.01', '2014-11-26'),
(67, '100.00', '200.00', '2014-11-13'),
(68, '25.99', '999.99', '2014-11-10'),
(69, '100.00', '500.01', '2014-06-13'),
(70, '100.00', '500.01', '2014-06-13'),
(71, '999.99', '200.00', '2014-11-10'),
(72, '100.00', '200.00', '2015-03-05'),
(73, '123.32', '500.01', '2014-11-26'),
(74, '100.00', '200.00', '2014-11-26'),
(75, '123.32', '500.01', '2014-11-26'),
(76, '123.32', '500.01', '2014-11-19');

-- --------------------------------------------------------

--
-- Table structure for table `game_titles`
--

CREATE TABLE IF NOT EXISTS `game_titles` (
  `gameId` int(4) NOT NULL AUTO_INCREMENT,
  `title` varchar(40) NOT NULL,
  `cond` varchar(12) DEFAULT NULL,
  `game_type` varchar(10) NOT NULL,
  `game_inst` char(1) NOT NULL,
  `game_box` char(1) NOT NULL,
  `consoleId` int(3) DEFAULT NULL,
  `categoryId` int(3) DEFAULT NULL,
  PRIMARY KEY (`gameId`),
  KEY `categoryId` (`categoryId`),
  KEY `consoleId` (`consoleId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=77 ;

--
-- Dumping data for table `game_titles`
--

INSERT INTO `game_titles` (`gameId`, `title`, `cond`, `game_type`, `game_inst`, `game_box`, `consoleId`, `categoryId`) VALUES
(1, 'Duck Tales 2', 'mint', 'CD', 'Y', 'Y', 1, 4),
(2, 'Chessmaster', 'good', 'Cartridge', 'N', 'N', 1, 3),
(3, 'Captain America and the Avengers', 'mint', 'CD', 'Y', 'N', 1, 1),
(4, 'Addams Family Pugsley''s Scavenger Hunt', 'poor', 'Cartridge', 'N', 'N', 1, 4),
(5, 'Caesar''s Palace', 'poor', 'Cartridge', 'N', 'N', 1, 4),
(6, 'Double Dragon II', 'acceptable', 'Cartridge', 'N', 'N', 1, 1),
(7, 'City Connection', 'very good', 'Cartridge', 'N', 'N', 1, 3),
(8, 'Double Dragon III', 'very good', 'Cartridge', 'N', 'N', 1, 1),
(9, 'Captain Planet and the Planeteers', 'very good', 'Cartridge', 'N', 'N', 1, 1),
(10, 'Dr. Mario', 'good', 'CD', 'Y', 'N', 1, 4),
(11, 'Batman and Robin', 'mint', 'DVD', 'N', 'Y', 2, 1),
(12, 'Battle Arena Toshinden 3', 'acceptable', 'CD', 'Y', 'Y', 2, 1),
(13, 'Grand Theft Auto 2', 'acceptable', 'CD', 'N', 'Y', 2, 2),
(14, 'LEGO Racers', 'acceptable', 'CD', 'N', 'Y', 2, 3),
(15, 'Madden 99', 'poor', 'DVD', 'N', 'N', 2, 3),
(16, 'Marvel Super Heroes vs. Street Fighter', 'poor', 'DVD', 'N', 'Y', 2, 1),
(17, 'MDK', 'mint', 'DVD', 'N', 'Y', 2, 1),
(18, 'Mega Man Legends', 'very good', 'DVD', 'Y', 'Y', 2, 4),
(19, 'NBA Live 2003', 'very good', 'CD', 'Y', 'N', 2, 3),
(20, 'Need for Speed Porsche Unleashed', 'very good', 'CD', 'Y', 'Y', 2, 3),
(21, 'AirForce Delta', 'good', 'Cartridge', 'N', 'N', 3, 1),
(22, 'WWF Royal Rumble', 'good', 'Cartridge', 'N', 'N', 3, 1),
(23, 'Tony Hawk', 'good', 'Cartridge', 'N', 'N', 3, 3),
(24, 'Street Fighter III Double Impact', 'good', 'Cartridge', 'N', 'N', 3, 1),
(25, 'Star Wars Episode I Jedi Power Battles', 'poor', 'Cartridge', 'N', 'N', 3, 1),
(26, 'Soul Calibur', 'mint', 'Cartridge', 'N', 'N', 3, 2),
(27, 'Roadsters', 'mint', 'Cartridge', 'N', 'N', 3, 3),
(28, 'Mortal Kombat Gold', 'acceptable', 'Cartridge', 'N', 'N', 3, 1),
(29, 'Demolition Racer', 'acceptable', 'Cartridge', 'N', 'N', 3, 3),
(30, 'Incoming', 'acceptable', 'Cartridge', 'N', 'N', 3, 4),
(31, 'American Chopper', 'poor', 'DVD', 'Y', 'Y', 4, 4),
(32, 'Avatar the Last Airbender', 'poor', 'DVD', 'N', 'N', 4, 2),
(33, 'BMX XXX', 'mint', 'BlueRay', 'Y', 'Y', 4, 3),
(34, 'Buffy the Vampire Slayer', 'mint', 'BlueRay', 'N', 'Y', 4, 2),
(35, 'Chronicles of Riddick', 'mint', 'BlueRay', 'Y', 'N', 4, 2),
(36, 'Counter Strike', 'mint', 'BlueRay', 'Y', 'Y', 4, 1),
(37, 'Dead Mans Hand', 'acceptable', 'DVD', 'Y', 'Y', 4, 1),
(38, 'Enter the Matrix', 'acceptable', 'DVD', 'N', 'Y', 4, 2),
(39, 'FIFA 2007', 'acceptable', 'DVD', 'Y', 'N', 4, 3),
(40, 'Ford Racing 3', 'acceptable', 'DVD', 'Y', 'Y', 4, 3),
(41, 'Alien', 'very good', 'Cartridge', 'N', 'N', 5, 1),
(42, 'Asteroids', 'very good', 'Cartridge', 'N', 'N', 5, 4),
(43, 'Blackjack', 'very good', 'Cartridge', 'N', 'N', 5, 3),
(44, 'Chuck Norris Superkicks', 'very good', 'Cartridge', 'N', 'N', 5, 1),
(45, 'Commando', 'poor', 'Cartridge', 'N', 'N', 5, 1),
(46, 'Donkey Kong Jr', 'poor', 'Cartridge', 'N', 'N', 5, 4),
(47, 'Fire Fighter', 'mint', 'Cartridge', 'N', 'N', 5, 1),
(48, 'Ghostbusters II', 'mint', 'Cartridge', 'N', 'N', 5, 4),
(49, 'Mario Bros.', 'mint', 'Cartridge', 'N', 'N', 5, 4),
(50, 'Othello', 'very good', 'Cartridge', 'N', 'N', 5, 3),
(51, 'Mario Bros.', 'mint', 'Cartridge', 'N', 'N', 3, 4),
(52, 'NBA Live 2003', 'good', 'CD', 'Y', 'Y', 4, 3),
(53, 'WWF Royal Rumble', 'poor', 'Cartridge', 'N', 'N', 5, 3),
(54, 'MDK', 'very good', 'CD', 'Y', 'N', 1, 1),
(55, 'Chessmaster', 'good', 'Cartridge', 'N', 'N', 3, 3),
(56, 'Fifa 15', 'new', 'CD', 'Y', 'Y', 2, 1),
(57, 'Age of Empire-10', 'mint', 'BlueRay', 'N', 'N', 3, 3),
(58, '', 'new', 'CD', 'Y', 'Y', 1, 1),
(59, 'Superman-222', 'new', 'CD', 'Y', 'Y', 1, 1),
(60, 'Superman-222', 'new', 'CD', 'Y', 'Y', 1, 1),
(61, 'Mega Show100', 'new', 'CD', 'Y', 'Y', 1, 1),
(62, 'Mega Show100', 'new', 'CD', 'Y', 'Y', 1, 1),
(63, 'Superwoman', 'new', 'CD', 'Y', 'Y', 1, 1),
(64, 'Superwoman2', 'new', 'CD', 'Y', 'Y', 1, 1),
(65, 'Superman234', 'new', 'CD', 'Y', 'Y', 1, 3),
(66, 'Mario20122', 'new', 'CD', 'Y', 'Y', 1, 1),
(67, 'Superman23423', 'new', 'CD', 'Y', 'Y', 1, 1),
(68, 'Recoil', 'new', 'DVD', 'Y', 'Y', 1, 1),
(69, 'Superman123213', 'new', 'CD', 'Y', 'Y', 1, 1),
(70, 'Superman123213', 'new', 'CD', 'Y', 'Y', 1, 1),
(71, 'hjhk', 'poor', 'CD', 'N', 'N', 4, 3),
(72, 'hjhk4343', 'poor', 'CD', 'Y', 'Y', 4, 1),
(73, 'Superman123123', 'new', 'CD', 'Y', 'Y', 1, 1),
(74, 'Age of Empire-11', 'new', 'CD', 'Y', 'Y', 1, 1),
(75, 'Superman123123', 'new', 'CD', 'Y', 'Y', 1, 1),
(76, 'Supermandasd432423', 'new', 'CD', 'Y', 'Y', 1, 1);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `game_finance`
--
ALTER TABLE `game_finance`
  ADD CONSTRAINT `game_finance_ibfk_1` FOREIGN KEY (`gameId`) REFERENCES `game_titles` (`gameId`) ON DELETE CASCADE,
  ADD CONSTRAINT `game_finance_ibfk_2` FOREIGN KEY (`gameId`) REFERENCES `game_titles` (`gameId`) ON DELETE CASCADE;

--
-- Constraints for table `game_titles`
--
ALTER TABLE `game_titles`
  ADD CONSTRAINT `game_titles_ibfk_1` FOREIGN KEY (`categoryId`) REFERENCES `category` (`categoryId`),
  ADD CONSTRAINT `game_titles_ibfk_2` FOREIGN KEY (`consoleId`) REFERENCES `console` (`consoleId`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
