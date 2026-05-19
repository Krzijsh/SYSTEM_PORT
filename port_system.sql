-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 12, 2026 at 04:52 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `port_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `cargo_records`
--

CREATE TABLE `cargo_records` (
  `record_id` int(11) NOT NULL,
  `vessel_id` int(11) NOT NULL,
  `cargo_type` varchar(100) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `vessels`
--

CREATE TABLE `vessels` (
  `id` int(11) NOT NULL,
  `vessel_name` varchar(100) NOT NULL,
  `vessel_type` varchar(50) NOT NULL,
  `capacity` int(11) NOT NULL,
  `current_load` int(11) NOT NULL DEFAULT 0,
  `status` varchar(50) NOT NULL DEFAULT 'Docked'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vessels`
--

INSERT INTO `vessels` (`id`, `vessel_name`, `vessel_type`, `capacity`, `current_load`, `status`) VALUES
(1, 'GGS', 'Cargo', 10000, 0, 'Docked');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cargo_records`
--
ALTER TABLE `cargo_records`
  ADD PRIMARY KEY (`record_id`);

--
-- Indexes for table `vessels`
--
ALTER TABLE `vessels`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cargo_records`
--
ALTER TABLE `cargo_records`
  MODIFY `record_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `vessels`
--
ALTER TABLE `vessels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
