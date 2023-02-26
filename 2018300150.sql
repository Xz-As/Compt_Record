-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: 2018300150
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `match`
--

DROP TABLE IF EXISTS `match`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `match` (
  `mid` int unsigned NOT NULL,
  `mlv` int unsigned NOT NULL DEFAULT '0',
  `mred` int unsigned NOT NULL,
  `mblue` int unsigned NOT NULL,
  `mwinner` tinyint unsigned NOT NULL,
  `mjudge` int unsigned NOT NULL,
  PRIMARY KEY (`mid`),
  KEY `blueteam_fk_idx` (`mblue`),
  KEY `redteam_fk_idx` (`mred`),
  KEY `judge_fk_idx` (`mjudge`),
  CONSTRAINT `blueteam_fk` FOREIGN KEY (`mblue`) REFERENCES `team` (`tid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `judge_fk` FOREIGN KEY (`mjudge`) REFERENCES `user` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `redteam_fk` FOREIGN KEY (`mred`) REFERENCES `team` (`tid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `match`
--

LOCK TABLES `match` WRITE;
/*!40000 ALTER TABLE `match` DISABLE KEYS */;
INSERT INTO `match` VALUES (2,4,3,4,0,2018300000);
/*!40000 ALTER TABLE `match` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mr`
--

DROP TABLE IF EXISTS `mr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mr` (
  `mid` int unsigned NOT NULL,
  `mnum` tinyint unsigned NOT NULL DEFAULT '0',
  `loss` int unsigned NOT NULL DEFAULT '0',
  `wipe` int unsigned NOT NULL DEFAULT '0',
  `ctrl` int unsigned NOT NULL DEFAULT '0',
  `scr` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`mid`,`mnum`),
  CONSTRAINT `mid_fk` FOREIGN KEY (`mid`) REFERENCES `match` (`mid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mr`
--

LOCK TABLES `mr` WRITE;
/*!40000 ALTER TABLE `mr` DISABLE KEYS */;
INSERT INTO `mr` VALUES (2,0,130,130,130,390),(2,1,120,130,130,380);
/*!40000 ALTER TABLE `mr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `team`
--

DROP TABLE IF EXISTS `team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `team` (
  `tid` int unsigned NOT NULL,
  `tleader` int unsigned NOT NULL,
  `ttype` tinyint unsigned NOT NULL DEFAULT '0',
  `tlv` int unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`tid`),
  KEY `leader_idx` (`tleader`),
  CONSTRAINT `leader` FOREIGN KEY (`tleader`) REFERENCES `user` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `team`
--

LOCK TABLES `team` WRITE;
/*!40000 ALTER TABLE `team` DISABLE KEYS */;
INSERT INTO `team` VALUES (3,2018306666,1,2),(4,2018306666,0,0);
/*!40000 ALTER TABLE `team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `uid` int unsigned NOT NULL,
  `utype` tinyint unsigned NOT NULL DEFAULT '0',
  `uname` varchar(45) NOT NULL,
  `dept` varchar(45) NOT NULL,
  `gender` tinyint unsigned NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `uname_UNIQUE` (`uname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (234,0,'aaa','hc',0),(2000000000,0,'qq','0',0),(2018300000,1,'77','0',1),(2018306666,0,'朱瑞杰','hc',1);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ut`
--

DROP TABLE IF EXISTS `ut`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ut` (
  `uid` int unsigned NOT NULL,
  `tid` int unsigned NOT NULL,
  PRIMARY KEY (`uid`,`tid`),
  KEY `tid_fk_ut_idx` (`tid`),
  CONSTRAINT `tid_fk_ut` FOREIGN KEY (`tid`) REFERENCES `team` (`tid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `uid_fk_ut` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ut`
--

LOCK TABLES `ut` WRITE;
/*!40000 ALTER TABLE `ut` DISABLE KEYS */;
INSERT INTO `ut` VALUES (234,3),(2018306666,3),(2018306666,4);
/*!40000 ALTER TABLE `ut` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-23 10:26:47
