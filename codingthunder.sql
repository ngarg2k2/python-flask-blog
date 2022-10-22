-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2022 at 10:54 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `msg`, `date`, `email`) VALUES
(1, 'first_post', '1234567890', 'first post', '2022-10-18 12:46:47', 'firstpost@gmail.com'),
(2, 'Nipun Garg', '09988485145', 'chal ja bhai pls', '2022-10-19 08:58:55', 'ngarg4_be20@thapar.edu'),
(3, 'mera naam', '7896541230', 'yrr iss baar bhi chal jaana pls', '2022-10-19 09:01:17', 'meriMailId@gmail.com'),
(4, 'kuch bhi', '248454548', 'Mail send hoja pls', '2022-10-19 09:59:22', 'abc@gmail.com'),
(6, 'ndjn', '662', 'vdvsf', '2022-10-19 10:10:36', 'jdnn'),
(7, 'gggggggggg', '595554', 'last try', '2022-10-19 10:18:30', 'ggggggggggg'),
(8, 'jeevan', '51864168415', 'cbhjcbsdh', '2022-10-19 12:06:40', 'bshdbh'),
(9, 'nmwbd vg', '54165156', 'njbjh hjb', '2022-10-19 12:07:42', 'hvg hbv'),
(10, 'Nipun Garg', '09988485145', 'nc d bc', '2022-10-22 12:37:07', 'abc@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagline` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `img_file` varchar(12) NOT NULL,
  `date` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `tagline`, `slug`, `content`, `img_file`, `date`) VALUES
(1, 'First Post', 'Stock Market', 'first-post', 'This is my first post for this flask playlist!!', 'about-bg.png', '2022-10-22 14:08:24'),
(14, 'Second post', 'This is my 2', 'second_post', 'This is my second post!!', 'home-bg.jpg', '2022-10-22 14:11:37'),
(15, '3rd', 'My blog', 'third_post', 'bbdhvbhd', 'about_bg.jpg', '2022-10-22 14:11:25');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
