-- MariaDB dump 10.19  Distrib 10.4.24-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: a6
-- ------------------------------------------------------
-- Server version	10.4.24-MariaDB
--
-- Creación de la BBDD a6
--
DROP DATABASE IF EXISTS `a6`;
CREATE DATABASE a6;
USE a6;

--
-- Estructura de la tabla `usuarios`
--
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` varchar(60) NOT NULL,
  `password` char(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

--
-- Dump de los datos en la tabla `usuarios`
--

LOCK TABLES `user` WRITE;

INSERT INTO `user` VALUES (1,'samu','pbkdf2:sha256:260000$o830SzYlBiR4uZDu$63c053876d0eb76b6a6a0799dc9321127722f352ffe1195f88e2a83d098645e6');

UNLOCK TABLES;



