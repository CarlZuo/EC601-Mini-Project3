-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 2019-12-09 16:30:42
-- server version： 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_zy18750`
--

-- --------------------------------------------------------

--
-- table `twitter`
--

CREATE TABLE `twitter` (
  `ID` int(100) NOT NULL,
  `Name` varchar(200) NOT NULL,
  `Text` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- data `twitter`
--

INSERT INTO `twitter` (`ID`, `Name`, `Text`) VALUES
(1, 'tungws', 'omg, i\'m so jealous !! wow, that has to be the best pic of the iPhone 11 yet!'),
(2, 'iPhonedo', 'You should have added a “I’m an iPhone user but want to see the results of the poll” option'),
(3, 'biankeydoodle', ' \"malinis\" naman yung toilet hahahaha i think di pa time for iphone 11 but i think its time for…');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
