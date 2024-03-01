-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 01, 2024 at 05:07 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `face_recognition_system`
--

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `dep` varchar(45) DEFAULT NULL,
  `course` varchar(45) DEFAULT NULL,
  `year` varchar(45) DEFAULT NULL,
  `Semester` varchar(45) DEFAULT NULL,
  `StudentId` varchar(45) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `Classdiv` varchar(45) DEFAULT NULL,
  `RollNo` varchar(45) DEFAULT NULL,
  `Gender` varchar(45) DEFAULT NULL,
  `Dob` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Phone_number` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Teacher_Name` varchar(45) DEFAULT NULL,
  `PhotoSamplestatus` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`dep`, `course`, `year`, `Semester`, `StudentId`, `name`, `Classdiv`, `RollNo`, `Gender`, `Dob`, `Email`, `Phone_number`, `Address`, `Teacher_Name`, `PhotoSamplestatus`) VALUES
('CSE', 'B.tech', '2021', 'Semester 1', '1', 'Aniruddha', 'A', '21BCS022', 'Male', '18/10', 'email', '10101010', 'adderess', 'duggu', 'Yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`StudentId`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
