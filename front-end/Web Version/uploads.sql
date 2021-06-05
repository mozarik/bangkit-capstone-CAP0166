-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 04 Jun 2021 pada 12.18
-- Versi server: 10.4.11-MariaDB
-- Versi PHP: 7.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `thewatcher`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `uploads`
--

CREATE TABLE `uploads` (
  `id` int(11) NOT NULL,
  `file_name` varchar(150) NOT NULL,
  `upload_time` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `uploads`
--

INSERT INTO `uploads` (`id`, `file_name`, `upload_time`) VALUES
(15, 'picture67.jpg', '2021-06-02 00:19:23'),
(16, 'picture149.jpg', '2021-06-02 00:23:34'),
(17, 'picture151.jpg', '2021-06-02 00:25:47'),
(18, 'picture207.jpg', '2021-06-02 00:40:04'),
(19, 'picture71.jpg', '2021-06-02 01:21:04'),
(20, 'picture165.jpg', '2021-06-02 01:47:11'),
(24, 'picture81.jpg', '2021-06-02 14:53:27'),
(25, 'picture70.jpg', '2021-06-02 15:15:46'),
(26, 'picture75.jpg', '2021-06-02 16:26:42'),
(27, 'picture151.jpg', '2021-06-02 16:27:04'),
(28, 'picture78.jpg', '2021-06-04 17:17:38');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `uploads`
--
ALTER TABLE `uploads`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `uploads`
--
ALTER TABLE `uploads`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
