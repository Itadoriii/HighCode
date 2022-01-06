-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: cavesbd
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `estado_equipos`
--

DROP TABLE IF EXISTS `estado_equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_equipos` (
  `Familia` int unsigned NOT NULL,
  `Nivel` varchar(5) NOT NULL,
  `Estado` int unsigned NOT NULL,
  `Combustible` int unsigned NOT NULL,
  `Fecha` varchar(10) NOT NULL,
  `Hora` varchar(7) NOT NULL,
  `Id_frente` varchar(15) NOT NULL,
  `Id_equipo` varchar(15) NOT NULL COMMENT 'Llave primaria',
  PRIMARY KEY (`Id_equipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_equipos`
--

LOCK TABLES `estado_equipos` WRITE;
/*!40000 ALTER TABLE `estado_equipos` DISABLE KEYS */;
/*!40000 ALTER TABLE `estado_equipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_frentes`
--

DROP TABLE IF EXISTS `estado_frentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_frentes` (
  `Operacion` int unsigned NOT NULL,
  `Estado_Avance` int unsigned NOT NULL,
  `Estado_general` int unsigned NOT NULL,
  `Notas_generales` varchar(50) DEFAULT NULL,
  `Hora_Inicio` varchar(7) NOT NULL,
  `Hora_Termino` varchar(7) NOT NULL,
  `Fecha` varchar(10) NOT NULL,
  `Hora` varchar(7) NOT NULL,
  `Criticidad` int unsigned NOT NULL,
  `Direccion` varchar(1) NOT NULL,
  `Id_frente` varchar(15) NOT NULL COMMENT 'Llave primaria',
  PRIMARY KEY (`Id_frente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_frentes`
--

LOCK TABLES `estado_frentes` WRITE;
/*!40000 ALTER TABLE `estado_frentes` DISABLE KEYS */;
/*!40000 ALTER TABLE `estado_frentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_servicios`
--

DROP TABLE IF EXISTS `estado_servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_servicios` (
  `Estado_general` int unsigned NOT NULL,
  `Estado_servicio` int unsigned NOT NULL,
  `Nota_Servicio` varchar(50) DEFAULT NULL,
  `Pk_servicio` int unsigned NOT NULL,
  `Nota_Pk` varchar(50) DEFAULT NULL,
  `Fecha` varchar(10) NOT NULL,
  `Hora` varchar(7) NOT NULL,
  `Id_Frente` varchar(15) NOT NULL COMMENT 'Llave primaria',
  PRIMARY KEY (`Id_Frente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_servicios`
--

LOCK TABLES `estado_servicios` WRITE;
/*!40000 ALTER TABLE `estado_servicios` DISABLE KEYS */;
/*!40000 ALTER TABLE `estado_servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frentes`
--

DROP TABLE IF EXISTS `frentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `frentes` (
  `Tipo` int unsigned NOT NULL,
  `Sigla` varchar(5) NOT NULL,
  `Numero` varchar(10) NOT NULL,
  `Direccion` varchar(1) NOT NULL,
  `Estado` int unsigned NOT NULL,
  `Tamaño` varchar(1) NOT NULL,
  `Ruta_Critica` int unsigned NOT NULL,
  `Distancia_Marinas` int unsigned NOT NULL,
  `Nivel` varchar(5) NOT NULL,
  `Macrobloque` varchar(5) NOT NULL,
  `Id_Frente` varchar(15) NOT NULL COMMENT 'Llave primaria',
  PRIMARY KEY (`Id_Frente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frentes`
--

LOCK TABLES `frentes` WRITE;
/*!40000 ALTER TABLE `frentes` DISABLE KEYS */;
/*!40000 ALTER TABLE `frentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topografia`
--

DROP TABLE IF EXISTS `topografia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `topografia` (
  `Avance` int unsigned NOT NULL,
  `Nivel` varchar(5) NOT NULL,
  `Nota_actividad` varchar(50) DEFAULT NULL,
  `Pk_acumulado` varchar(50) NOT NULL,
  `Fecha` varchar(10) NOT NULL,
  `Hora` varchar(7) NOT NULL,
  `Id_Frente` varchar(15) NOT NULL COMMENT 'Llave primaria',
  PRIMARY KEY (`Id_Frente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topografia`
--

LOCK TABLES `topografia` WRITE;
/*!40000 ALTER TABLE `topografia` DISABLE KEYS */;
/*!40000 ALTER TABLE `topografia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `Rut` int unsigned NOT NULL,
  `Dv` varchar(1) NOT NULL,
  `Password` varchar(20) NOT NULL,
  `Codigo_proyecto` varchar(50) DEFAULT NULL,
  `Codigo_contrato` varchar(50) DEFAULT NULL,
  `Identificador_cedula` varchar(50) DEFAULT NULL,
  `Grupo` varchar(50) DEFAULT NULL,
  `Turno` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-05 21:51:10
