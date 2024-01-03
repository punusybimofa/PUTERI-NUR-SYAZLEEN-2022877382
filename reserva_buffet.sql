-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 05:43 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `reserva_buffet`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_details`
--

CREATE TABLE `customer_details` (
  `NAME` varchar(30) NOT NULL,
  `PHONE_NUM` int(30) NOT NULL,
  `NUM_ADULT` int(10) NOT NULL,
  `NUM_KIDS` int(10) NOT NULL,
  `NUM_ELDER` int(10) NOT NULL,
  `TIME` varchar(10) NOT NULL,
  `DATE` varchar(10) NOT NULL,
  `TOTAL_COST` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_details`
--

INSERT INTO `customer_details` (`NAME`, `PHONE_NUM`, `NUM_ADULT`, `NUM_KIDS`, `NUM_ELDER`, `TIME`, `DATE`, `TOTAL_COST`) VALUES
('MOHD FAUDZY', 176649271, 6, 5, 2, '7PM', '12/14/23', '590.0'),
('NOOR LIZA', 126619110, 8, 4, 1, '6PM', '12/18/23', '640.0'),
('MOHD SYAFIQ', 1847583648, 2, 0, 0, '7PM', '12/6/23', '120.0'),
('MOHD NAZRIN ', 132114164, 2, 3, 0, '6PM', '12/15/23', '210.0'),
('NUR SYUHADA', 1467382746, 5, 3, 2, '7PM', '12/18/23', '470.0');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
