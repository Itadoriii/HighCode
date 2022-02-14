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
-- Table structure for table `avances`
--

DROP TABLE IF EXISTS `avances`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `avances` (
  `avance` varchar(50) NOT NULL,
  `nivel` varchar(50) NOT NULL,
  `nota_actividad` varchar(50) NOT NULL,
  `pk_acumulado` varchar(50) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `id_frente` varchar(50) NOT NULL,
  PRIMARY KEY (`id_frente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `avances`
--

LOCK TABLES `avances` WRITE;
/*!40000 ALTER TABLE `avances` DISABLE KEYS */;
/*!40000 ALTER TABLE `avances` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresas`
--

DROP TABLE IF EXISTS `empresas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresas` (
  `nombre` varchar(50) NOT NULL,
  `codigo_empresa` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresas`
--

LOCK TABLES `empresas` WRITE;
/*!40000 ALTER TABLE `empresas` DISABLE KEYS */;
INSERT INTO `empresas` VALUES ('empresa1','ce1'),('empresa2','ce2');
/*!40000 ALTER TABLE `empresas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `equipos`
--

DROP TABLE IF EXISTS `equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipos` (
  `flota` varchar(50) NOT NULL,
  `codigo_equipo` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo_equipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipos`
--

LOCK TABLES `equipos` WRITE;
/*!40000 ALTER TABLE `equipos` DISABLE KEYS */;
INSERT INTO `equipos` VALUES ('aa','e1'),('aaa','e2');
/*!40000 ALTER TABLE `equipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_equipos`
--

DROP TABLE IF EXISTS `estado_equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_equipos` (
  `flota` varchar(50) NOT NULL,
  `nivel` varchar(50) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `codigo_equipo` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo_equipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_equipos`
--

LOCK TABLES `estado_equipos` WRITE;
/*!40000 ALTER TABLE `estado_equipos` DISABLE KEYS */;
INSERT INTO `estado_equipos` VALUES ('1','1','1','1','1');
/*!40000 ALTER TABLE `estado_equipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_frentes`
--

DROP TABLE IF EXISTS `estado_frentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_frentes` (
  `operacion` varchar(50) NOT NULL,
  `estado_avance` varchar(50) NOT NULL,
  `observaciones` varchar(50) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `criticidad` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `id_frente` varchar(50) NOT NULL,
  PRIMARY KEY (`id_frente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_frentes`
--

LOCK TABLES `estado_frentes` WRITE;
/*!40000 ALTER TABLE `estado_frentes` DISABLE KEYS */;
INSERT INTO `estado_frentes` VALUES ('1','1','1','1','1','1','1');
/*!40000 ALTER TABLE `estado_frentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estado_servicios`
--

DROP TABLE IF EXISTS `estado_servicios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estado_servicios` (
  `estado_servicio` varchar(50) NOT NULL,
  `nota_estado` varchar(50) NOT NULL,
  `pk_servicio` varchar(50) NOT NULL,
  `nota_pk` varchar(50) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `id_frente` varchar(50) NOT NULL,
  PRIMARY KEY (`id_frente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_servicios`
--

LOCK TABLES `estado_servicios` WRITE;
/*!40000 ALTER TABLE `estado_servicios` DISABLE KEYS */;
INSERT INTO `estado_servicios` VALUES ('1','1','1','1','1','1');
/*!40000 ALTER TABLE `estado_servicios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `frentes`
--

DROP TABLE IF EXISTS `frentes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `frentes` (
  `tipo` varchar(50) NOT NULL,
  `sigla` varchar(50) NOT NULL,
  `numero` varchar(50) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `tamaño` varchar(50) NOT NULL,
  `ruta_critica` varchar(50) NOT NULL,
  `distancia_marina` varchar(50) NOT NULL,
  `nivel` varchar(50) NOT NULL,
  `macrobloque` varchar(50) NOT NULL,
  `id_frente` varchar(50) NOT NULL,
  `codigo_empresa` varchar(50) NOT NULL,
  `sector` varchar(20) NOT NULL,
  `numero_referencia` varchar(50) NOT NULL,
  `direccion_referencia` varchar(50) NOT NULL,
  PRIMARY KEY (`id_frente`),
  KEY `codigo_empresa` (`codigo_empresa`),
  CONSTRAINT `frentes_ibfk_1` FOREIGN KEY (`codigo_empresa`) REFERENCES `empresas` (`codigo_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `frentes`
--

LOCK TABLES `frentes` WRITE;
/*!40000 ALTER TABLE `frentes` DISABLE KEYS */;
INSERT INTO `frentes` VALUES ('Cabecera','CAB','1','N','Activo','C','No','1','PD','S01','f1','ce1','S1','1','N');
/*!40000 ALTER TABLE `frentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `Rut` varchar(50) NOT NULL,
  `Contraseña` varchar(50) NOT NULL,
  `Codigo_empresa` varchar(50) NOT NULL,
  PRIMARY KEY (`Rut`),
  KEY `Codigo_empresa` (`Codigo_empresa`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`Codigo_empresa`) REFERENCES `empresas` (`codigo_empresa`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES ('204687293','admin','ce1');
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

-- Dump completed on 2022-01-19 11:19:26
