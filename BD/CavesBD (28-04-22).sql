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
  `distancia_acumulada` varchar(50) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `id_frente` varchar(50) NOT NULL
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
INSERT INTO `estado_equipos` VALUES ('Jumbo fortificacion','HD','fecha','operativo','E1'),('Jumbo avance','PD','fecha','operativo','E10'),('Jumbo avance','CH','fecha','operativo','E11'),('Jumbo avance','INY','fecha','operativo','E12'),('Jumbo avance','EXT','fecha','operativo','E13'),('Jumbo avance','TI','fecha','operativo','E14'),('Jumbo avance','-','fecha','operativo','E15'),('Jumbo avance','-','fecha','operativo','E16'),('LHD','HD','fecha','operativo','E17'),('LHD','PD','fecha','operativo','E18'),('LHD','CH','fecha','operativo','E19'),('Jumbo fortificacion','PD','fecha','operativo','E2'),('LHD','INY','fecha','operativo','E20'),('LHD','EXT','fecha','operativo','E21'),('LHD','TI','fecha','operativo','E22'),('LHD','-','fecha','operativo','E23'),('LHD','-','fecha','operativo','E24'),('Manitou','HD','fecha','operativo','E25'),('Manitou','PD','fecha','operativo','E26'),('Manitou','CH','fecha','operativo','E27'),('Manitou','INY','fecha','operativo','E28'),('Manitou','EXT','fecha','operativo','E29'),('Jumbo fortificacion','CH','fecha','operativo','E3'),('Manitou','TI','fecha','operativo','E30'),('Manitou','-','fecha','operativo','E31'),('Manitou','-','fecha','operativo','E32'),('Roboshot','HD','fecha','operativo','E33'),('Roboshot','PD','fecha','operativo','E34'),('Roboshot','CH','fecha','operativo','E35'),('Roboshot','INY','fecha','operativo','E36'),('Roboshot','EXT','fecha','operativo','E37'),('Roboshot','TI','fecha','operativo','E38'),('Roboshot','-','fecha','operativo','E39'),('Jumbo fortificacion','INY','fecha','operativo','E4'),('Roboshot','-','fecha','operativo','E40'),('Mixer','HD','fecha','operativo','E41'),('Mixer','PD','fecha','operativo','E42'),('Mixer','CH','fecha','operativo','E43'),('Mixer','INY','fecha','operativo','E44'),('Mixer','EXT','fecha','operativo','E45'),('Mixer','TI','fecha','operativo','E46'),('Mixer','-','fecha','operativo','E47'),('Mixer','-','fecha','operativo','E48'),('Camion marina','HD','fecha','operativo','E49'),('Jumbo fortificacion','EXT','fecha','operativo','E5'),('Camion marina','PD','fecha','operativo','E50'),('Camion marina','CH','fecha','operativo','E51'),('Camion marina','INY','fecha','operativo','E52'),('Camion marina','EXT','fecha','operativo','E53'),('Camion marina','TI','fecha','operativo','E54'),('Camion marina','-','fecha','operativo','E55'),('Camion marina','-','fecha','operativo','E56'),('Retroexcavadora','HD','fecha','operativo','E57'),('Retroexcavadora','PD','fecha','operativo','E58'),('Retroexcavadora','CH','fecha','operativo','E59'),('Jumbo fortificacion','TI','fecha','operativo','E6'),('Retroexcavadora','INY','fecha','operativo','E60'),('Retroexcavadora','EXT','fecha','operativo','E61'),('Retroexcavadora','TI','fecha','operativo','E62'),('Retroexcavadora','-','fecha','operativo','E63'),('Retroexcavadora','-','fecha','operativo','E64'),('Jumbo fortificacion','-','fecha','operativo','E7'),('Jumbo fortificacion','-','fecha','operativo','E8'),('Jumbo avance','HD','fecha','operativo','E9');
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
  `fortificacion` varchar(45) NOT NULL,
  PRIMARY KEY (`id_frente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_frentes`
--

LOCK TABLES `estado_frentes` WRITE;
/*!40000 ALTER TABLE `estado_frentes` DISABLE KEYS */;
INSERT INTO `estado_frentes` VALUES ('perforacion_pernos','0','-','fecha','alta','N','F1','p-m-sh'),('escaner','0','-','fecha','baja','S','F2','p-m-sh'),('tronadura','0','-','fecha','alta','E','F3','p-m-sh'),('marcacion_topografica','0','-','fecha','baja','O','F4','p-m-sh'),('lechado_pernos','0','-','fecha','alta','N','F5','p-m-sh'),('tronadura','0','-','fecha','baja','E','F6','p-m-sh');
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
  `distancia` varchar(50) NOT NULL,
  `fecha` varchar(50) NOT NULL,
  `id_frente` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estado_servicios`
--

LOCK TABLES `estado_servicios` WRITE;
/*!40000 ALTER TABLE `estado_servicios` DISABLE KEYS */;
INSERT INTO `estado_servicios` VALUES ('disponible','11','fecha','F1'),('disponible','22','fecha','F2'),('disponible','33','fecha','F3'),('disponible','44','fecha','F4'),('disponible','55','fecha','F5'),('disponible','66','fecha','F6');
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
  `foco` varchar(50) NOT NULL,
  `largo` char(50) NOT NULL,
  `tipofort` varchar(50) DEFAULT NULL,
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
INSERT INTO `frentes` VALUES ('Cabecera','CAB','1','N','activo','C','Si','677','HD','S01','F1','ce1','S1','1','N','0','159','p-m-sh'),('Calle','CAL','2','S','activo','M','No','456','PD','S02','F2','ce1','S2','2','S','1','247','p-m-sh'),('Zanja','ZA','3','E','activo','G','Si','999','CH','S03','F3','ce1','S2','3','E','0','368','p-m-sh'),('Fronton inyeccion','FRI','4','O','activo','C','No','233','INY','S04','F4','ce1','S1','4','O','0','495','p-m-sh'),('Fronton extraccion','FEX','5','N','activo','M','Si','155','EXT','S05','F5','ce1','S1','5','N','1','579','p-m-sh'),('Calle','CAL','6','E','activo','C','No','287','TI','S01','F6','ce1','S2','6','E','0','667','p-m-sh');
/*!40000 ALTER TABLE `frentes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recurso_dotacion`
--

DROP TABLE IF EXISTS `recurso_dotacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recurso_dotacion` (
  `cuadrilla` varchar(50) NOT NULL,
  `cantidad` varchar(50) NOT NULL,
  `nivel` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recurso_dotacion`
--

LOCK TABLES `recurso_dotacion` WRITE;
/*!40000 ALTER TABLE `recurso_dotacion` DISABLE KEYS */;
INSERT INTO `recurso_dotacion` VALUES ('cuadrilla mineros 1','1','HD'),('cuadrilla mineros 2','1','PD'),('cuadrilla mineros 3','1','CH'),('cuadrilla mineros 4','1','INY'),('cuadrilla mineros 5','1','EXT'),('cuadrilla mineros 6','1','TI'),('cuadrilla mineros 7','1','-'),('cuadrilla mineros 8','1','-'),('cuadrilla servicios 1','1','HD'),('cuadrilla servicios 2','1','PD'),('cuadrilla servicios 3','1','CH'),('cuadrilla servicios 4','1','INY'),('cuadrilla servicios 5','1','EXT'),('cuadrilla servicios 6','1','TI'),('cuadrilla servicios 7','1','-'),('cuadrilla servicios 8','1','-');
/*!40000 ALTER TABLE `recurso_dotacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recurso_equipos`
--

DROP TABLE IF EXISTS `recurso_equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recurso_equipos` (
  `flota` varchar(50) NOT NULL,
  `codigo_equipo` varchar(50) NOT NULL,
  `cantidad` varchar(50) NOT NULL,
  `nivel` varchar(50) NOT NULL,
  PRIMARY KEY (`codigo_equipo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recurso_equipos`
--

LOCK TABLES `recurso_equipos` WRITE;
/*!40000 ALTER TABLE `recurso_equipos` DISABLE KEYS */;
INSERT INTO `recurso_equipos` VALUES ('Jumbo fortificacion','E1','1','HD'),('Jumbo avance','E10','1','PD'),('Jumbo avance','E11','1','CH'),('Jumbo avance','E12','1','INY'),('Jumbo avance','E13','1','EXT'),('Jumbo avance','E14','1','TI'),('Jumbo avance','E15','1','-'),('Jumbo avance','E16','1','-'),('LHD','E17','1','HD'),('LHD','E18','1','PD'),('LHD','E19','1','CH'),('Jumbo fortificacion','E2','1','PD'),('LHD','E20','1','INY'),('LHD','E21','1','EXT'),('LHD','E22','1','TI'),('LHD','E23','1','-'),('LHD','E24','1','-'),('Manitou','E25','1','HD'),('Manitou','E26','1','PD'),('Manitou','E27','1','CH'),('Manitou','E28','1','INY'),('Manitou','E29','1','EXT'),('Jumbo fortificacion','E3','1','CH'),('Manitou','E30','1','TI'),('Manitou','E31','1','-'),('Manitou','E32','1','-'),('Roboshot','E33','1','HD'),('Roboshot','E34','1','PD'),('Roboshot','E35','1','CH'),('Roboshot','E36','1','INY'),('Roboshot','E37','1','EXT'),('Roboshot','E38','1','TI'),('Roboshot','E39','1','-'),('Jumbo fortificacion','E4','1','INY'),('Roboshot','E40','1','-'),('Mixer','E41','1','HD'),('Mixer','E42','1','PD'),('Mixer','E43','1','CH'),('Mixer','E44','1','INY'),('Mixer','E45','1','EXT'),('Mixer','E46','1','TI'),('Mixer','E47','1','-'),('Mixer','E48','1','-'),('Camion marina','E49','1','HD'),('Jumbo fortificacion','E5','1','EXT'),('Camion marina','E50','1','PD'),('Camion marina','E51','1','CH'),('Camion marina','E52','1','INY'),('Camion marina','E53','1','EXT'),('Camion marina','E54','1','TI'),('Camion marina','E55','1','-'),('Camion marina','E56','1','-'),('Retroexcavadora','E57','1','HD'),('Retroexcavadora','E58','1','PD'),('Retroexcavadora','E59','1','CH'),('Jumbo fortificacion','E6','1','TI'),('Retroexcavadora','E60','1','INY'),('Retroexcavadora','E61','1','EXT'),('Retroexcavadora','E62','1','TI'),('Retroexcavadora','E63','1','-'),('Retroexcavadora','E64','1','-'),('Jumbo fortificacion','E7','1','-'),('Jumbo fortificacion','E8','1','-'),('Jumbo avance','E9','1','HD');
/*!40000 ALTER TABLE `recurso_equipos` ENABLE KEYS */;
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
INSERT INTO `usuarios` VALUES ('1','1','ce1'),('204687293','admin','ce1'),('5','5','ce1');
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

-- Dump completed on 2022-04-28 11:16:02
