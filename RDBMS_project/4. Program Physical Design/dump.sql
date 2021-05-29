-- MariaDB dump 10.17  Distrib 10.5.6-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.5.6-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `db`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `db` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `db`;

--
-- Table structure for table `album`
--

DROP TABLE IF EXISTS `album`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `album` (
  `album_name` varchar(50) NOT NULL,
  `enroll_date` date DEFAULT NULL,
  `artist` int(11) NOT NULL,
  PRIMARY KEY (`artist`,`album_name`),
  CONSTRAINT `album_ibfk_1` FOREIGN KEY (`artist`) REFERENCES `artist` (`a_index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `album`
--

LOCK TABLES `album` WRITE;
/*!40000 ALTER TABLE `album` DISABLE KEYS */;
INSERT INTO `album` VALUES ('TESTING','2018-05-25',101),('DETOX','2020-04-08',102),('Freudian','2017-08-25',103),('Her','2017-12-07',104),('The Anecdote','2015-08-27',105),('The Marshall Mathers LP','2000-05-23',106),('Blonde','2016-08-20',107),('My Beautiful Dark Twisted Fantasy','2010-01-01',108),('To Pimp A Butterfly','2015-03-18',109),('YSIV','2018-09-28',110),('BENTLEY 2','2020-11-11',112),('Stormy Friday','2011-11-29',112),('TEAM BABY','2017-05-30',113),('2 MANY HOMES 4 1 KID','2016-06-14',117),('Love poem','2019-11-18',215),('Palette','2017-04-21',215),('STABLE MINDSET','2019-07-02',216),('Midnight Candy','2018-11-06',218),('Morning Glory','2020-12-07',311),('Seoul Disease','2016-05-19',314),('24 26','2020-12-07',317),('del album','2020-12-07',318),('del music','2020-12-07',318);
/*!40000 ALTER TABLE `album` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artist`
--

DROP TABLE IF EXISTS `artist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `artist` (
  `a_index` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `b_date` date DEFAULT NULL,
  PRIMARY KEY (`a_index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artist`
--

LOCK TABLES `artist` WRITE;
/*!40000 ALTER TABLE `artist` DISABLE KEYS */;
INSERT INTO `artist` VALUES (101,'Asap Rocky','1988-10-03'),(102,'BILL STAX','1980-12-18'),(103,'Daniel Caesar','1995-04-05'),(104,'DPR LIVE','1993-01-01'),(105,'E SENS','1987-02-09'),(106,'Eminem','1972-10-17'),(107,'Frank Ocean','1987-10-28'),(108,'Kanye West','1977-06-08'),(109,'Kendrick Lamar','1987-06-17'),(110,'Logic','1990-01-22'),(112,'The Quiett','1985-01-29'),(113,'BlackSkirts','1982-12-05'),(117,'Justhis','1991-05-07'),(215,'IU','1993-05-16'),(216,'YoonHa','1988-04-29'),(218,'Fromm','1985-07-24'),(311,'Oasis',NULL),(314,'Thorn Apple',NULL),(315,'Mr.Kang','1997-07-31'),(316,'Birdy','1996-05-15'),(317,'Beenzino','1987-09-12'),(318,'del','2020-12-07');
/*!40000 ALTER TABLE `artist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `date_stream`
--

DROP TABLE IF EXISTS `date_stream`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `date_stream` (
  `str_cnt` int(11) NOT NULL,
  `music` varchar(50) NOT NULL,
  `artist` int(11) NOT NULL,
  `album` varchar(50) NOT NULL,
  `str_date` date NOT NULL,
  PRIMARY KEY (`artist`,`album`,`music`,`str_date`) USING BTREE,
  CONSTRAINT `date_stream_ibfk_1` FOREIGN KEY (`artist`, `album`, `music`) REFERENCES `music` (`artist`, `album`, `music_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `date_stream`
--

LOCK TABLES `date_stream` WRITE;
/*!40000 ALTER TABLE `date_stream` DISABLE KEYS */;
INSERT INTO `date_stream` VALUES (25,'Distorted Records',101,'TESTING','2020-12-05'),(29,'Distorted Records',101,'TESTING','2020-12-06'),(43,'Distorted Records',101,'TESTING','2020-12-07'),(73,'OG Beeper',101,'TESTING','2020-12-05'),(95,'OG Beeper',101,'TESTING','2020-12-06'),(79,'OG Beeper',101,'TESTING','2020-12-07'),(72,'Tony Tone',101,'TESTING','2020-12-05'),(68,'Tony Tone',101,'TESTING','2020-12-06'),(12,'Tony Tone',101,'TESTING','2020-12-07'),(53,'Price Tag',102,'DETOX','2020-12-05'),(10,'Price Tag',102,'DETOX','2020-12-06'),(35,'Price Tag',102,'DETOX','2020-12-07'),(45,'WASABI',102,'DETOX','2020-12-05'),(88,'WASABI',102,'DETOX','2020-12-06'),(30,'WASABI',102,'DETOX','2020-12-07'),(82,'Wickr me',102,'DETOX','2020-12-05'),(69,'Wickr me',102,'DETOX','2020-12-06'),(49,'Wickr me',102,'DETOX','2020-12-07'),(74,'Best Part',103,'Freudian','2020-12-05'),(45,'Best Part',103,'Freudian','2020-12-06'),(82,'Best Part',103,'Freudian','2020-12-07'),(92,'Blessed',103,'Freudian','2020-12-05'),(29,'Blessed',103,'Freudian','2020-12-06'),(99,'Blessed',103,'Freudian','2020-12-07'),(97,'GET YOU',103,'Freudian','2020-12-05'),(51,'GET YOU',103,'Freudian','2020-12-06'),(69,'GET YOU',103,'Freudian','2020-12-07'),(60,'Jasmine',104,'Her','2020-12-05'),(78,'Jasmine',104,'Her','2020-12-06'),(12,'Jasmine',104,'Her','2020-12-07'),(79,'Martini Blue',104,'Her','2020-12-05'),(60,'Martini Blue',104,'Her','2020-12-06'),(38,'Martini Blue',104,'Her','2020-12-07'),(71,'Text Me',104,'Her','2020-12-05'),(35,'Text Me',104,'Her','2020-12-06'),(81,'Text Me',104,'Her','2020-12-07'),(60,'Back In Time',105,'The Anecdote','2020-12-05'),(46,'Back In Time',105,'The Anecdote','2020-12-06'),(15,'Back In Time',105,'The Anecdote','2020-12-07'),(76,'Dice',105,'The Anecdote','2020-12-05'),(59,'Dice',105,'The Anecdote','2020-12-06'),(69,'Dice',105,'The Anecdote','2020-12-07'),(35,'Unknown Verse',105,'The Anecdote','2020-12-05'),(25,'Unknown Verse',105,'The Anecdote','2020-12-06'),(68,'Unknown Verse',105,'The Anecdote','2020-12-07'),(29,'Amityville',106,'The Marshall Mathers LP','2020-12-05'),(62,'Amityville',106,'The Marshall Mathers LP','2020-12-06'),(71,'Amityville',106,'The Marshall Mathers LP','2020-12-07'),(12,'Kill You',106,'The Marshall Mathers LP','2020-12-05'),(54,'Kill You',106,'The Marshall Mathers LP','2020-12-06'),(66,'Kill You',106,'The Marshall Mathers LP','2020-12-07'),(77,'Stan',106,'The Marshall Mathers LP','2020-12-05'),(27,'Stan',106,'The Marshall Mathers LP','2020-12-06'),(21,'Stan',106,'The Marshall Mathers LP','2020-12-07'),(56,'Ivy',107,'Blonde','2020-12-05'),(48,'Ivy',107,'Blonde','2020-12-06'),(24,'Ivy',107,'Blonde','2020-12-07'),(73,'Self Control',107,'Blonde','2020-12-05'),(41,'Self Control',107,'Blonde','2020-12-06'),(20,'Self Control',107,'Blonde','2020-12-07'),(82,'White Ferrari',107,'Blonde','2020-12-05'),(15,'White Ferrari',107,'Blonde','2020-12-06'),(94,'White Ferrari',107,'Blonde','2020-12-07'),(50,'All Of The Lights',108,'My Beautiful Dark Twisted Fantasy','2020-12-05'),(83,'All Of The Lights',108,'My Beautiful Dark Twisted Fantasy','2020-12-06'),(87,'All Of The Lights',108,'My Beautiful Dark Twisted Fantasy','2020-12-07'),(23,'Blame Game',108,'My Beautiful Dark Twisted Fantasy','2020-12-05'),(52,'Blame Game',108,'My Beautiful Dark Twisted Fantasy','2020-12-06'),(77,'Blame Game',108,'My Beautiful Dark Twisted Fantasy','2020-12-07'),(45,'So Appalled',108,'My Beautiful Dark Twisted Fantasy','2020-12-05'),(72,'So Appalled',108,'My Beautiful Dark Twisted Fantasy','2020-12-06'),(24,'So Appalled',108,'My Beautiful Dark Twisted Fantasy','2020-12-07'),(72,'Alright',109,'To Pimp A Butterfly','2020-12-05'),(74,'Alright',109,'To Pimp A Butterfly','2020-12-06'),(79,'Alright',109,'To Pimp A Butterfly','2020-12-07'),(28,'Mortal Man',109,'To Pimp A Butterfly','2020-12-05'),(12,'Mortal Man',109,'To Pimp A Butterfly','2020-12-06'),(21,'Mortal Man',109,'To Pimp A Butterfly','2020-12-07'),(58,'u',109,'To Pimp A Butterfly','2020-12-05'),(11,'u',109,'To Pimp A Butterfly','2020-12-06'),(77,'u',109,'To Pimp A Butterfly','2020-12-07'),(79,'Everybody Dies',110,'YSIV','2020-12-05'),(28,'Everybody Dies',110,'YSIV','2020-12-06'),(52,'Everybody Dies',110,'YSIV','2020-12-07'),(88,'Thank You',110,'YSIV','2020-12-05'),(92,'Thank You',110,'YSIV','2020-12-06'),(11,'Thank You',110,'YSIV','2020-12-07'),(97,'The Return',110,'YSIV','2020-12-05'),(77,'The Return',110,'YSIV','2020-12-06'),(89,'The Return',110,'YSIV','2020-12-07'),(49,'Abu Dhabi',112,'BENTLEY 2','2020-12-05'),(82,'Abu Dhabi',112,'BENTLEY 2','2020-12-06'),(94,'Abu Dhabi',112,'BENTLEY 2','2020-12-07'),(63,'BENTLY 2',112,'BENTLEY 2','2020-12-05'),(52,'BENTLY 2',112,'BENTLEY 2','2020-12-06'),(85,'BENTLY 2',112,'BENTLEY 2','2020-12-07'),(96,'Came From The Bottom',112,'Stormy Friday','2020-12-05'),(41,'Came From The Bottom',112,'Stormy Friday','2020-12-06'),(60,'Came From The Bottom',112,'Stormy Friday','2020-12-07'),(43,'Mr.Lonely part 2',112,'Stormy Friday','2020-12-05'),(18,'Mr.Lonely part 2',112,'Stormy Friday','2020-12-06'),(85,'Mr.Lonely part 2',112,'Stormy Friday','2020-12-07'),(16,'The Real Me',112,'Stormy Friday','2020-12-05'),(89,'The Real Me',112,'Stormy Friday','2020-12-06'),(55,'The Real Me',112,'Stormy Friday','2020-12-07'),(51,'EVERYTHING',113,'TEAM BABY','2020-12-05'),(47,'EVERYTHING',113,'TEAM BABY','2020-12-06'),(93,'EVERYTHING',113,'TEAM BABY','2020-12-07'),(10,'Hyeya',113,'TEAM BABY','2020-12-05'),(59,'Hyeya',113,'TEAM BABY','2020-12-06'),(19,'Hyeya',113,'TEAM BABY','2020-12-07'),(32,'Who Do You Love',113,'TEAM BABY','2020-12-05'),(89,'Who Do You Love',113,'TEAM BABY','2020-12-06'),(41,'Who Do You Love',113,'TEAM BABY','2020-12-07'),(97,'Atelier',117,'2 MANY HOMES 4 1 KID','2020-12-05'),(61,'Atelier',117,'2 MANY HOMES 4 1 KID','2020-12-06'),(11,'Atelier',117,'2 MANY HOMES 4 1 KID','2020-12-07'),(72,'Sell The Soul',117,'2 MANY HOMES 4 1 KID','2020-12-05'),(25,'Sell The Soul',117,'2 MANY HOMES 4 1 KID','2020-12-06'),(86,'Sell The Soul',117,'2 MANY HOMES 4 1 KID','2020-12-07'),(64,'Welcome to My HOME',117,'2 MANY HOMES 4 1 KID','2020-12-05'),(39,'Welcome to My HOME',117,'2 MANY HOMES 4 1 KID','2020-12-06'),(28,'Welcome to My HOME',117,'2 MANY HOMES 4 1 KID','2020-12-07'),(31,'Bluming',215,'Love poem','2020-12-05'),(61,'Bluming',215,'Love poem','2020-12-06'),(66,'Bluming',215,'Love poem','2020-12-07'),(49,'Love poem',215,'Love poem','2020-12-05'),(62,'Love poem',215,'Love poem','2020-12-06'),(89,'Love poem',215,'Love poem','2020-12-07'),(41,'That Person',215,'love poem','2020-12-07'),(86,'unlucky',215,'Love poem','2020-12-05'),(38,'unlucky',215,'Love poem','2020-12-06'),(63,'unlucky',215,'Love poem','2020-12-07'),(87,'For Name',215,'Palette','2020-12-05'),(96,'For Name',215,'Palette','2020-12-06'),(37,'For Name',215,'Palette','2020-12-07'),(34,'Jam Jam',215,'Palette','2020-12-05'),(65,'Jam Jam',215,'Palette','2020-12-06'),(83,'Jam Jam',215,'Palette','2020-12-07'),(63,'This Moment',215,'Palette','2020-12-05'),(52,'This Moment',215,'Palette','2020-12-06'),(61,'This Moment',215,'Palette','2020-12-07'),(54,'Lonely',216,'STABLE MINDSET','2020-12-05'),(40,'Lonely',216,'STABLE MINDSET','2020-12-06'),(83,'Lonely',216,'STABLE MINDSET','2020-12-07'),(44,'On a Rainy Day',216,'STABLE MINDSET','2020-12-05'),(97,'On a Rainy Day',216,'STABLE MINDSET','2020-12-06'),(41,'On a Rainy Day',216,'STABLE MINDSET','2020-12-07'),(59,'Toughest Day',216,'STABLE MINDSET','2020-12-05'),(37,'Toughest Day',216,'STABLE MINDSET','2020-12-06'),(65,'Toughest Day',216,'STABLE MINDSET','2020-12-07'),(71,'Hold Me Like Its Forever',218,'Midnight Candy','2020-12-05'),(38,'Hold Me Like Its Forever',218,'Midnight Candy','2020-12-06'),(13,'Hold Me Like Its Forever',218,'Midnight Candy','2020-12-07'),(14,'Midnight Driver',218,'Midnight Candy','2020-12-05'),(67,'Midnight Driver',218,'Midnight Candy','2020-12-06'),(56,'Midnight Driver',218,'Midnight Candy','2020-12-07'),(61,'Us On a Young Night',218,'Midnight Candy','2020-12-05'),(15,'Us On a Young Night',218,'Midnight Candy','2020-12-06'),(97,'Us On a Young Night',218,'Midnight Candy','2020-12-07'),(38,'Difficult Moon',314,'Seoul Disease','2020-12-05'),(61,'Difficult Moon',314,'Seoul Disease','2020-12-06'),(45,'Difficult Moon',314,'Seoul Disease','2020-12-07'),(69,'Pomegranate taste',314,'Seoul Disease','2020-12-05'),(96,'Pomegranate taste',314,'Seoul Disease','2020-12-06'),(82,'Pomegranate taste',314,'Seoul Disease','2020-12-07'),(31,'Seoul',314,'Seoul Disease','2020-12-05'),(35,'Seoul',314,'Seoul Disease','2020-12-06'),(88,'Seoul',314,'Seoul Disease','2020-12-07'),(4,'del album1',318,'del album','2020-12-07'),(3,'del album2',318,'del album','2020-12-07'),(3,'del music1',318,'del music','2020-12-07'),(1,'del music2',318,'del music','2020-12-07'),(1,'del music3',318,'del music','2020-12-07');
/*!40000 ALTER TABLE `date_stream` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `in_playlist`
--

DROP TABLE IF EXISTS `in_playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `in_playlist` (
  `playlist` int(11) NOT NULL,
  `producer` int(11) NOT NULL,
  `music` varchar(50) NOT NULL,
  `album` varchar(50) NOT NULL,
  `artist` int(11) NOT NULL,
  PRIMARY KEY (`producer`,`playlist`,`artist`,`album`,`music`),
  KEY `playlist` (`playlist`,`producer`),
  KEY `artist` (`artist`,`album`,`music`),
  CONSTRAINT `in_playlist_ibfk_1` FOREIGN KEY (`playlist`, `producer`) REFERENCES `playlist` (`pl_index`, `producer`),
  CONSTRAINT `in_playlist_ibfk_2` FOREIGN KEY (`artist`, `album`, `music`) REFERENCES `music` (`artist`, `album`, `music_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `in_playlist`
--

LOCK TABLES `in_playlist` WRITE;
/*!40000 ALTER TABLE `in_playlist` DISABLE KEYS */;
INSERT INTO `in_playlist` VALUES (0,1,'OG Beeper','TESTING',101),(0,1,'Text Me','Her',104),(0,1,'All Of The Lights','My Beautiful Dark Twisted Fantasy',108),(0,1,'BENTLY 2','BENTLEY 2',112),(0,1,'Bluming','Love poem',215),(0,1,'Hold Me Like Its Forever','Midnight Candy',218),(1,1,'Tony Tone','TESTING',101),(1,1,'Back In Time','The Anecdote',105),(1,1,'Blame Game','My Beautiful Dark Twisted Fantasy',108),(1,1,'Came From The Bottom','Stormy Friday',112),(1,1,'Love poem','Love poem',215),(1,1,'Midnight Driver','Midnight Candy',218),(2,1,'Price Tag','DETOX',102),(2,1,'Dice','The Anecdote',105),(2,1,'So Appalled','My Beautiful Dark Twisted Fantasy',108),(2,1,'Mr.Lonely part 2','Stormy Friday',112),(2,1,'That Person','love poem',215),(2,1,'Us On a Young Night','Midnight Candy',218),(0,3,'Amityville','The Marshall Mathers LP',106),(0,3,'Mortal Man','To Pimp A Butterfly',109),(0,3,'Who Do You Love','TEAM BABY',113),(1,3,'Ivy','Blonde',107),(0,4,'WASABI','DETOX',102),(0,4,'Unknown Verse','The Anecdote',105),(0,4,'Alright','To Pimp A Butterfly',109),(0,4,'The Real Me','Stormy Friday',112),(0,4,'unlucky','Love poem',215),(0,5,'del album1','del album',318),(0,5,'del album2','del album',318),(0,5,'del music1','del music',318),(1,5,'del music2','del music',318),(1,5,'del music3','del music',318);
/*!40000 ALTER TABLE `in_playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager`
--

DROP TABLE IF EXISTS `manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manager` (
  `m_index` int(11) NOT NULL,
  `email` varchar(40) NOT NULL,
  `phone_num` char(13) NOT NULL,
  `name` varchar(20) NOT NULL,
  `bdate` date NOT NULL,
  `sex` char(1) NOT NULL,
  `passwd` varchar(20) NOT NULL,
  PRIMARY KEY (`m_index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager`
--

LOCK TABLES `manager` WRITE;
/*!40000 ALTER TABLE `manager` DISABLE KEYS */;
INSERT INTO `manager` VALUES (0,'osj2387@naver.com','010-8756-2387','OhSungJoon','1997-03-17','M','dhtjdwns123'),(1,'TA','010-****-****','TA','2020-12-07','M','TA123');
/*!40000 ALTER TABLE `manager` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `music`
--

DROP TABLE IF EXISTS `music`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `music` (
  `music_name` varchar(50) NOT NULL,
  `enroll_date` date DEFAULT NULL,
  `artist` int(11) NOT NULL,
  `album` varchar(50) NOT NULL,
  PRIMARY KEY (`artist`,`album`,`music_name`),
  CONSTRAINT `music_ibfk_1` FOREIGN KEY (`artist`, `album`) REFERENCES `album` (`artist`, `album_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `music`
--

LOCK TABLES `music` WRITE;
/*!40000 ALTER TABLE `music` DISABLE KEYS */;
INSERT INTO `music` VALUES ('Distorted Records','2018-05-25',101,'TESTING'),('OG Beeper','2018-05-25',101,'TESTING'),('Tony Tone','2018-05-25',101,'TESTING'),('Price Tag','2020-04-08',102,'DETOX'),('WASABI','2020-04-08',102,'DETOX'),('Wickr me','2020-04-08',102,'DETOX'),('Best Part','2017-08-25',103,'Freudian'),('Blessed','2017-08-25',103,'Freudian'),('GET YOU','2017-08-25',103,'Freudian'),('Jasmine','2017-12-07',104,'Her'),('Martini Blue','2017-12-07',104,'Her'),('Text Me','2017-12-07',104,'Her'),('Back In Time','2015-08-27',105,'The Anecdote'),('Dice','2015-08-27',105,'The Anecdote'),('Unknown Verse','2015-08-27',105,'The Anecdote'),('Amityville','2000-05-23',106,'The Marshall Mathers LP'),('Kill You','2000-05-23',106,'The Marshall Mathers LP'),('Stan','2000-05-23',106,'The Marshall Mathers LP'),('Ivy','2016-08-20',107,'Blonde'),('Self Control','2016-08-20',107,'Blonde'),('White Ferrari','2016-08-20',107,'Blonde'),('All Of The Lights','2010-01-01',108,'My Beautiful Dark Twisted Fantasy'),('Blame Game','2010-01-01',108,'My Beautiful Dark Twisted Fantasy'),('So Appalled','2010-01-01',108,'My Beautiful Dark Twisted Fantasy'),('Alright','2015-03-18',109,'To Pimp A Butterfly'),('Mortal Man','2015-03-18',109,'To Pimp A Butterfly'),('u','2015-03-18',109,'To Pimp A Butterfly'),('Everybody Dies','2018-09-28',110,'YSIV'),('Thank You','2018-09-28',110,'YSIV'),('The Return','2018-09-28',110,'YSIV'),('Abu Dhabi','2020-11-11',112,'BENTLEY 2'),('BENTLY 2','2020-11-11',112,'BENTLEY 2'),('Came From The Bottom','2011-11-29',112,'Stormy Friday'),('Mr.Lonely part 2','2011-11-29',112,'Stormy Friday'),('The Real Me','2011-11-29',112,'Stormy Friday'),('EVERYTHING','2017-05-30',113,'TEAM BABY'),('Hyeya','2017-05-30',113,'TEAM BABY'),('Who Do You Love','2017-05-30',113,'TEAM BABY'),('Atelier','2016-06-14',117,'2 MANY HOMES 4 1 KID'),('Sell The Soul','2016-06-14',117,'2 MANY HOMES 4 1 KID'),('Welcome to My HOME','2016-06-14',117,'2 MANY HOMES 4 1 KID'),('Bluming','2019-11-18',215,'Love poem'),('Love poem','2019-11-18',215,'Love poem'),('That Person','2020-12-06',215,'love poem'),('unlucky','2019-11-18',215,'Love poem'),('For Name','2017-04-21',215,'Palette'),('Jam Jam','2017-04-21',215,'Palette'),('This Moment','2017-04-21',215,'Palette'),('Lonely','2019-07-02',216,'STABLE MINDSET'),('On a Rainy Day','2019-07-02',216,'STABLE MINDSET'),('Toughest Day','2019-07-02',216,'STABLE MINDSET'),('Hold Me Like Its Forever','2018-11-06',218,'Midnight Candy'),('Midnight Driver','2018-11-06',218,'Midnight Candy'),('Us On a Young Night','2018-11-06',218,'Midnight Candy'),('Cast No Shadow','2020-12-07',311,'Morning Glory'),('Dont Look Back In Anger','2020-12-07',311,'Morning Glory'),('Wonderwall','2020-12-07',311,'Morning Glory'),('Difficult Moon','2016-05-19',314,'Seoul Disease'),('Pomegranate taste','2016-05-19',314,'Seoul Disease'),('Seoul','2016-05-19',314,'Seoul Disease'),('Boogie On&On','2020-12-07',317,'24 26'),('del album1','2020-12-07',318,'del album'),('del album2','2020-12-07',318,'del album'),('del music1','2020-12-07',318,'del music'),('del music2','2020-12-07',318,'del music'),('del music3','2020-12-07',318,'del music');
/*!40000 ALTER TABLE `music` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `playlist`
--

DROP TABLE IF EXISTS `playlist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `playlist` (
  `pl_name` varchar(50) NOT NULL,
  `pl_index` int(11) NOT NULL,
  `producer` int(11) NOT NULL,
  PRIMARY KEY (`pl_index`,`producer`),
  KEY `producer` (`producer`),
  CONSTRAINT `playlist_ibfk_1` FOREIGN KEY (`producer`) REFERENCES `user` (`u_index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `playlist`
--

LOCK TABLES `playlist` WRITE;
/*!40000 ALTER TABLE `playlist` DISABLE KEYS */;
INSERT INTO `playlist` VALUES ('pl1 by user1',0,1),('pl1 by user3',0,3),('pl1 by user2',0,4),('delete',0,5),('pl2 by user1',1,1),('pl2 by user3',1,3),('dele',1,5),('pl3 by user1',2,1);
/*!40000 ALTER TABLE `playlist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `u_index` int(11) NOT NULL,
  `email` varchar(40) DEFAULT NULL,
  `phone_num` char(13) NOT NULL,
  `name` varchar(20) NOT NULL,
  `bdate` date DEFAULT NULL,
  `sex` char(1) DEFAULT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`u_index`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (0,'abc@abc.com','***-****-****','TA',NULL,'F','TA123'),(1,'user1@naver.com','010-1234-1234','user1','1997-03-03','M','12341234'),(3,'user3@google.com','010-9876-9876','user3','2001-01-01','M','98769876'),(4,'user4@hanyang.ac.kr','010-7845-7845','user2','2010-12-26','F','78457845'),(5,'delu@delu.net','010-4444-4444','delu','2020-12-07','M','delu123');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-07 18:25:25
