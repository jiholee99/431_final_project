-- MySQL dump 10.13  Distrib 8.0.34, for macos13 (arm64)
--
-- Host: 127.0.0.1    Database: final_project_431
-- ------------------------------------------------------
-- Server version	8.1.0

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
-- Table structure for table `Streamer`
--

DROP TABLE IF EXISTS `Streamer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Streamer` (
  `streamer_uid` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `subscribers` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`streamer_uid`),
  CONSTRAINT `streamer_chk_1` CHECK ((`subscribers` >= 0.00))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Streamer`
--

LOCK TABLES `Streamer` WRITE;
/*!40000 ALTER TABLE `Streamer` DISABLE KEYS */;
INSERT INTO `Streamer` VALUES (1,'mbaccus0',7669.01),(2,'kmcimmie1',7054.18),(3,'akenny2',4024.26),(4,'vlampke3',7264.32),(5,'bwelbourn4',5395.69),(6,'cfromont5',763.67),(7,'epearcy6',5004.10),(8,'dwinsome7',6053.30),(9,'jsummerley8',9306.95),(10,'lcuttings9',5045.16),(11,'lgoddarda',7819.00),(12,'jhandesb',4827.37),(13,'mcorderoc',4803.30),(14,'etoquetd',8797.76),(15,'ssquiere',4543.43),(16,'kfratsonf',1802.19),(17,'mhicking',3060.14),(18,'rvallentinh',8909.13),(19,'gchillistonei',1654.59),(20,'sroysonj',8581.83),(21,'nfilippovk',8885.38),(22,'vredsulll',4863.62),(23,'jeilersm',8893.85),(24,'upacen',3782.10),(25,'dkewleyo',3811.29),(26,'cmosesp',577.27),(27,'mmulrooneyq',5727.66),(28,'mlinforthr',8728.41),(29,'egiamettis',6610.35),(30,'cwestwoodt',4931.54),(31,'dcridlanu',8582.72),(32,'kkiftv',1305.04),(33,'apumphreyw',1996.39),(34,'dchidwickx',3301.30),(35,'jbeaulieuy',6058.26),(36,'gmacchaellz',1707.73),(37,'hloukes10',2744.08),(38,'vmurfill11',4619.86),(39,'zcaunce12',5696.27),(40,'pwey13',9794.42),(41,'lposselwhite14',2591.67),(42,'tdensey15',1076.21),(43,'dvanelli16',1596.27),(44,'cfere17',2904.09),(45,'gmulbry18',3332.63),(46,'bbourgour19',9198.97),(47,'jallchin1a',9015.22),(48,'tmcphaden1b',4722.81),(49,'morae1c',4535.83),(50,'cmccollum1d',4782.48),(51,'kyeardsley1e',5165.78),(52,'cfrowde1f',5149.96),(53,'nhasely1g',4002.13),(54,'khatwells1h',5951.31),(55,'pbrandenburg1i',580.96),(56,'kblindt1j',8659.07),(57,'rgreensmith1k',908.25),(58,'qclouter1l',4632.99),(59,'eahmed1m',9449.69),(60,'cygo1n',2477.66),(61,'ujaimez1o',9671.76),(62,'blappin1p',7873.57),(63,'fbertwistle1q',1269.14),(64,'rmichel1r',6970.47),(65,'perrigo1s',6753.72),(66,'jstrangeways1t',4396.95),(67,'tshepherdson1u',6242.46),(68,'mfroud1v',8164.08),(69,'cmellish1w',6015.92),(70,'dshepherd1x',3942.87),(71,'bovenden1y',4030.90),(72,'nkauscher1z',735.93),(73,'megell20',5865.32),(74,'fransley21',4765.05),(75,'vgatecliffe22',1265.45),(76,'abestwick23',3402.54),(77,'kpamphilon24',1754.22),(78,'kgoodhall25',5523.71),(79,'ojanman26',8412.56),(80,'rsamwell27',7283.21),(81,'rbarnfather28',3296.95),(82,'mkarran29',581.89),(83,'krawlingson2a',2221.97),(84,'hvearncombe2b',4991.08),(85,'lbeamont2c',9271.06),(86,'dimlock2d',5895.62),(87,'eingarfield2e',1350.61),(88,'jharradine2f',4134.27),(89,'mpollen2g',2447.40),(90,'hsenecaux2h',5333.16),(91,'cbarsham2i',3584.39),(92,'wpeek2j',9166.51),(93,'akeese2k',6644.40),(94,'awhiff2l',6255.55),(95,'ugloster2m',4287.05),(96,'dgladman2n',4949.48),(97,'abailess2o',3811.98),(98,'mnineham2p',5208.28),(99,'gleavens2q',5237.37),(100,'scattermull2r',3034.09),(101,'adellenbach2s',4285.67),(102,'espickett2t',5463.06),(103,'gkisbee2u',5491.45),(104,'mkneeshaw2v',6091.23),(105,'ageraghty2w',7297.82),(106,'ahollebon2x',4720.32),(107,'wmccorrie2y',1158.16),(108,'mbulstrode2z',4468.39),(109,'wolennikov30',7557.75),(110,'dhunting31',5120.88),(111,'bsimco32',5994.63),(112,'wmatelaitis33',5629.24),(113,'dwaber34',899.26),(114,'rlaweles35',6956.82),(115,'folagen36',1657.16),(116,'hgiurio37',8155.76),(117,'kpyatt38',9371.01),(118,'mkrolle39',9995.77),(119,'gmcasgill3a',6863.28),(120,'bsouthward3b',7305.44),(121,'mpalley3c',7827.13),(122,'sbrankley3d',3096.96),(123,'ttante3e',8408.71),(124,'hsayse3f',9632.84),(125,'dwarmisham3g',1561.91),(126,'fwiburn3h',774.22),(127,'emarcus3i',7020.70),(128,'mkorbmaker3j',5960.50),(129,'whayzer3k',1948.52),(130,'ctaylorson3l',125.84),(131,'chusbands3m',6450.09),(132,'ablenkharn3n',765.95),(133,'sspickett3o',8986.21),(134,'ehaskew3p',6511.81),(135,'hgready3q',8089.84),(136,'mcammish3r',6236.35),(137,'pelwill3s',3840.79),(138,'mgrangier3t',5937.12),(139,'wmillin3u',3313.83),(140,'gdaintith3v',4070.57),(141,'efeatherstone3w',3711.04),(142,'fmorando3x',7903.35),(143,'gmayes3y',1557.44),(144,'rbentjens3z',4158.25),(145,'tharford40',2776.76),(146,'pdurward41',7378.73),(147,'kcoghill42',2155.83),(148,'rstirland43',2729.00),(149,'bivanyushin44',992.98),(150,'sschottli45',4621.97),(151,'sbrabon46',1519.93),(152,'faizlewood47',2772.81),(153,'rbenne48',8717.04),(154,'htenny49',7336.95),(155,'rszubert4a',843.34),(156,'vtilling4b',2028.34),(157,'lwloch4c',9479.09),(158,'cgyorgy4d',9219.20),(159,'srispine4e',4896.28),(160,'spicton4f',8645.61),(161,'gharragin4g',3777.05),(162,'ehartop4h',1773.67),(163,'lfitzgerald4i',7022.49),(164,'dattenbrow4j',6468.59),(165,'jcarnie4k',53.48),(166,'kfancutt4l',3433.96),(167,'ideppen4m',1269.51),(168,'dconnealy4n',9188.53),(169,'dwaterland4o',1268.87),(170,'mawton4p',464.15),(171,'gcaddies4q',2674.28),(172,'azuenelli4r',8113.34),(173,'eeginton4s',8010.89),(174,'gstephens4t',4017.35),(175,'torbell4u',2046.79),(176,'rcorona4v',4764.67),(177,'ecreus4w',7406.76),(178,'tbresman4x',2379.14),(179,'klough4y',5014.44),(180,'mdabbes4z',9610.20),(181,'jmastrantone50',4955.46),(182,'imoff51',630.80),(183,'ehallas52',6606.54),(184,'ecanet53',8359.95),(185,'hyashin54',5426.68),(186,'hreedman55',3150.37),(187,'mmushet56',2536.75),(188,'dramirez57',3136.27),(189,'gmacfayden58',7113.66),(190,'ahatrey59',4775.31),(191,'kmelia5a',6169.23),(192,'fargyle5b',4531.53),(193,'mcornfield5c',7287.96),(194,'zallworthy5d',3868.59),(195,'bforrestall5e',4728.58),(196,'rfortescue5f',2962.19),(197,'cstelfax5g',8616.38),(198,'ttwelvetrees5h',7709.00),(199,'glambol5i',1737.60),(200,'aginnally5j',6728.15),(201,'vchorley5k',824.74),(202,'csymcoxe5l',7110.89),(203,'effrench5m',4635.50),(204,'mmikalski5n',8999.98),(205,'gwardroper5o',7205.26),(206,'kmichelotti5p',7872.21),(207,'abulcock5q',5388.30),(208,'oluchelli5r',4019.57),(209,'kcastrillo5s',7389.90),(210,'mgostall5t',4022.64),(211,'esailes5u',7369.09),(212,'viorillo5v',2023.63),(213,'dgreneham5w',4871.22),(214,'aflamank5x',9676.80),(215,'alutwidge5y',6203.60),(216,'flegall5z',3749.49),(217,'byakobovitz60',9542.72),(218,'eskelhorne61',842.67),(219,'droumier62',9176.03),(220,'ctrevaskis63',1049.50),(221,'ggouldbourn64',6318.36),(222,'mleatherland65',9116.31),(223,'hraddenbury66',8787.39),(224,'bgladdor67',7060.19),(225,'agreenhalgh68',1713.54),(226,'mreffe69',2298.13),(227,'jmalcolmson6a',5513.00),(228,'cdegrey6b',8046.57),(229,'kcunliffe6c',8819.36),(230,'mvivian6d',3741.71),(231,'dalston6e',7209.85),(232,'byukhtin6f',7933.55),(233,'gstott6g',1686.56),(234,'hstollwerck6h',8296.27),(235,'sprovest6i',9857.25),(236,'psutty6j',4022.32),(237,'bturnbull6k',456.99),(238,'alodevick6l',4130.03),(239,'dnovak6m',4414.25),(240,'kburwood6n',8223.61),(241,'ublackburne6o',1278.09),(242,'djohannesson6p',8287.95),(243,'baireton6q',6123.33),(244,'rdowley6r',8671.14),(245,'cdaingerfield6s',9228.53),(246,'nphythean6t',9920.12),(247,'aglaysher6u',7996.93),(248,'bcostin6v',1538.65),(249,'cselway6w',4647.00),(250,'gvasiltsov6x',3170.77),(251,'clarkin6y',5553.50),(252,'gmatschuk6z',983.29),(253,'blindsley70',3340.79),(254,'cpencost71',284.35),(255,'gthominga72',9519.42),(256,'bcrouch73',5116.72),(257,'tgreenrde74',7948.15),(258,'vdumsday75',6500.85),(259,'dgalbreath76',3973.10),(260,'sdedmam77',7858.07),(261,'rmckellen78',694.01),(262,'hshawe79',5920.74),(263,'mtuma7a',5098.75),(264,'uheatlie7b',7676.52),(265,'kalhirsi7c',6509.64),(266,'cmaundrell7d',8921.29),(267,'hattride7e',9721.83),(268,'sslocomb7f',5640.37),(269,'pbuche7g',2476.71),(270,'llydford7h',4094.48),(271,'bdolan7i',3472.96),(272,'erichardot7j',8378.60),(273,'kbrandhardy7k',2702.70),(274,'cguillotin7l',2441.57),(275,'abicksteth7m',82.92),(276,'chawksworth7n',8453.42),(277,'rtalkington7o',2346.86),(278,'ayanez7p',7113.32),(279,'mdyson7q',4113.72),(280,'hhartmann7r',2266.43),(281,'kwaterdrinker7s',8872.74),(282,'gdullard7t',8447.03),(283,'jboak7u',6561.71),(284,'aebbing7v',8943.17),(285,'vwilliam7w',5016.84),(286,'omaffey7x',1310.88),(287,'bmccleod7y',3984.04),(288,'swinnett7z',3867.60),(289,'lhuntress80',8238.74),(290,'lwanderschek81',52.47),(291,'tvondrasek82',5626.40),(292,'gragat83',9518.08),(293,'egoulter84',7584.44),(294,'msqueers85',9270.07),(295,'kreoch86',2102.23),(296,'rserman87',9669.00),(297,'vcraise88',6049.85),(298,'rricci89',7940.29),(299,'vgayter8a',6055.81),(300,'mberrick8b',6013.76),(301,'rdeshon8c',2405.13),(302,'cjephcott8d',697.07),(303,'lhorlick8e',6398.74),(304,'pbeadles8f',6162.64),(305,'wchevis8g',1988.28),(306,'afasham8h',7282.34),(307,'egoshawk8i',8012.19),(308,'cpurbrick8j',4374.29),(309,'agibke8k',2436.43),(310,'slepruvost8l',367.88),(311,'bcordet8m',2577.70),(312,'amenichini8n',8927.09),(313,'mhanney8o',1779.35),(314,'ehaggith8p',1595.72),(315,'vspeak8q',5883.84),(316,'aolahy8r',7332.33),(317,'bpidgin8s',1051.71),(318,'ckobiera8t',786.44),(319,'csabathe8u',7786.81),(320,'jstandley8v',3232.22),(321,'vingerman8w',4979.98),(322,'tarchard8x',4565.77),(323,'whaddacks8y',9195.59),(324,'dwhiskerd8z',2847.83),(325,'tgiroldo90',8380.95),(326,'wklaus91',1256.09),(327,'mcolomb92',6424.81),(328,'lgoater93',1394.23),(329,'bbote94',9693.14),(330,'tbucknill95',5143.45),(331,'nselway96',819.48),(332,'gwitchalls97',5092.24),(333,'cpeet98',325.27),(334,'mdubock99',8106.38),(335,'amaccaughan9a',1242.17),(336,'dsimpkin9b',7986.88),(337,'kwillarton9c',8389.98),(338,'aadamovicz9d',1867.35),(339,'amaccrossan9e',2426.31),(340,'gpoyner9f',8510.31),(341,'mfreear9g',6158.03),(342,'byellowlees9h',1728.24),(343,'lferrolli9i',2782.81),(344,'scutteridge9j',3173.93),(345,'snovis9k',7369.78),(346,'neskrigg9l',2819.48),(347,'santognozzii9m',9119.75),(348,'bspon9n',4204.15),(349,'rglover9o',6134.43),(350,'mthacke9p',5240.51),(351,'mblasio9q',6287.07),(352,'bsaint9r',4671.13),(353,'czupa9s',150.30),(354,'mgalloway9t',8640.13),(355,'nbizzey9u',8909.19),(356,'pfolker9v',5594.86),(357,'aocklin9w',7740.78),(358,'meverington9x',7502.35),(359,'cshallo9y',9456.01),(360,'sartiss9z',4731.11),(361,'abangiarda0',9172.90),(362,'aivensa1',8042.20),(363,'cbourtona2',2583.38),(364,'tphythiena3',7340.25),(365,'mmcruviea4',9186.49),(366,'bgota5',2210.65),(367,'mbraisbya6',9507.35),(368,'cfreeburna7',6042.75),(369,'lmosedalla8',8066.09),(370,'ranespiea9',4924.02),(371,'cwebenaa',9702.96),(372,'kpiffeab',8809.49),(373,'grodnightac',2817.08),(374,'croffeyad',9591.25),(375,'hmullengerae',2252.31),(376,'tbamellaf',1411.78),(377,'bdavissonag',5151.91),(378,'jbhatiaah',417.90),(379,'cgilbanksai',4537.99),(380,'cleveneaj',7757.13),(381,'cspaldinak',9624.15),(382,'poldcoteal',9771.35),(383,'cshepherdsonam',6989.85),(384,'bnorcockan',5144.47),(385,'jsaulao',5781.24),(386,'kaymesap',810.58),(387,'bkelsoaq',5520.46),(388,'bgalletlyar',3587.15),(389,'hweatherillas',671.36),(390,'grawcliffeat',2758.68),(391,'lnendau',5413.35),(392,'areeav',7656.14),(393,'dvinkeraw',8952.97),(394,'lmarcussenax',271.12),(395,'smozziniay',4566.14),(396,'gbrameaz',2996.93),(397,'bnottinghamb0',3296.47),(398,'sdulsonb1',9695.69),(399,'dbampkinb2',9195.70),(400,'gdonib3',1870.45),(401,'eflecknessb4',9285.48),(402,'hyosifovb5',1322.74),(403,'sskymeb6',9778.91),(404,'amcgrailb7',8968.29),(405,'ekivlehanb8',614.55),(406,'adegueb9',3213.33),(407,'edodingba',6759.56),(408,'oolivobb',1164.01),(409,'mgallbc',2013.90),(410,'kgooderickbd',7605.94),(411,'tfewsterbe',2401.30),(412,'mbransonbf',5204.34),(413,'dbullbg',3270.71),(414,'lbackshellbh',4342.62),(415,'asmallthwaitebi',7247.57),(416,'dcarbrybj',9096.20),(417,'gsetterbk',5729.28),(418,'fgleavesbl',1932.88),(419,'gchaudronbm',1469.03),(420,'lgierhardbn',2535.78),(421,'kmathelonbo',555.90),(422,'rpesselbp',5572.28),(423,'clangleybq',3849.85),(424,'mfranzolibr',5496.72),(425,'lduffynbs',5722.35),(426,'dquarmbybt',5306.88),(427,'adombrellbu',9773.37),(428,'eburdenbv',8687.77),(429,'rcharmanbw',1026.51),(430,'gkhalidbx',1773.40),(431,'aspatoniby',8578.94),(432,'delverstonbz',2658.15),(433,'pberriballc0',9188.95),(434,'itruslerc1',8029.43),(435,'labdonc2',2655.77),(436,'bgravesc3',1369.38),(437,'ranglessc4',6565.75),(438,'jplevenc5',4142.27),(439,'fbusec6',3822.37),(440,'ddaenc7',705.25),(441,'imougetc8',1283.64),(442,'asavilec9',792.67),(443,'adibbeca',9253.09),(444,'amagowancb',2756.22),(445,'gstodecc',8862.54),(446,'charlettcd',7230.30),(447,'hpolycotece',7651.62),(448,'wdaytoncf',3283.13),(449,'kpetelcg',853.74),(450,'pchaffynch',3163.74),(451,'blumoxci',5505.65),(452,'jmariacj',6975.16),(453,'thelmck',3214.17),(454,'cburgwyncl',9489.41),(455,'bfallowfieldcm',3285.30),(456,'mdeambrosiscn',8427.79),(457,'larmsbyco',8479.20),(458,'ebradmorecp',6446.01),(459,'ktrappecq',1484.12),(460,'eaffroncr',7390.55),(461,'sdalemancs',8151.82),(462,'ldevenishct',2107.27),(463,'rstonbridgecu',8442.70),(464,'dbailecv',6051.47),(465,'mswindellscw',6432.35),(466,'psalsburycx',1338.33),(467,'bdaftorcy',785.48),(468,'clightningcz',2879.96),(469,'sdinnaged0',8391.60),(470,'crosenfelderd1',1474.74),(471,'sgodind2',1381.57),(472,'jcrenshawd3',2273.40),(473,'gmarskelld4',9406.88),(474,'bwaddiloved5',511.93),(475,'fhilandd6',9765.15),(476,'cfulkerd7',4343.06),(477,'mbeckhamd8',4827.92),(478,'lyerralld9',6462.51),(479,'fwintersonda',4510.84),(480,'jmcgoochdb',9269.86),(481,'ngurdondc',1945.48),(482,'hsarfassdd',5021.88),(483,'fcowherdde',7444.53),(484,'vphilipeauxdf',1796.95),(485,'lrushburydg',8307.62),(486,'afugedh',9998.93),(487,'rwewelldi',9453.03),(488,'hcoventondj',9957.14),(489,'phingeleydk',931.41),(490,'pmarquesdl',3038.43),(491,'aellesworthdm',5779.55),(492,'tclaypoledn',654.59),(493,'feddollsdo',2574.48),(494,'gshobrookdp',2322.85),(495,'praisherdq',5188.90),(496,'jbraitlingdr',6623.41),(497,'ddutchburnds',2963.12),(498,'lpavlikdt',2914.45),(499,'dbiaggidu',4871.48),(500,'dpolottidv',373.01),(501,'ncalenderdw',3984.45),(502,'hcapnordx',1248.79),(503,'efolleydy',5262.92),(504,'mclarkedz',5627.62),(505,'nmcbrydee0',7575.02),(506,'drobathone1',8730.15),(507,'pstrephane2',6161.37),(508,'wpettisalle3',1085.35),(509,'ericoalde4',6184.14),(510,'cpollee5',1112.48),(511,'twaylene6',591.66),(512,'taddeye7',1701.51),(513,'gchalklye8',2622.87),(514,'kfraye9',1000.79),(515,'jstealeyea',6094.28),(516,'bcowleb',247.20),(517,'jcornockec',2728.69),(518,'hlamyed',5894.88),(519,'hsevenee',6599.82),(520,'krodrigef',8699.45),(521,'kgatheridgeeg',5116.97),(522,'kschelleeh',3133.11),(523,'sgarmanei',5995.89),(524,'skretschmerej',5684.82),(525,'swegenerek',7388.48),(526,'dwittenel',5172.20),(527,'cbruckentem',611.26),(528,'roakenfielden',556.91),(529,'korhtmanneo',2915.17),(530,'bmerrillep',9417.27),(531,'pdurretteq',7724.40),(532,'kduckerer',8035.65),(533,'ijurzykes',7763.25),(534,'hakermanet',5271.54),(535,'rlocaleu',1329.00),(536,'griddlesev',1248.54),(537,'srieflinew',5434.96),(538,'rsullivanex',1344.99),(539,'emcgrieleey',8828.46),(540,'everilloez',3623.14),(541,'jdeinhardtf0',3644.97),(542,'ccaplinf1',9217.17),(543,'lellimanf2',9481.84),(544,'mcumptonf3',7866.70),(545,'dcrosserf4',322.51),(546,'dhogganf5',7256.27),(547,'cspearingf6',4212.06),(548,'gcockshootf7',1049.83),(549,'brubinlichtf8',7816.49),(550,'nbeavenf9',8315.81),(551,'etrudgeonfa',3937.03),(552,'jdunnettfb',369.52),(553,'hskittlesfc',5610.33),(554,'sbresnahanfd',9854.75),(555,'rkeeganfe',8456.24),(556,'dpluesff',8634.34),(557,'genokssonfg',1383.12),(558,'ksoreaufh',7189.59),(559,'selijahfi',6077.42),(560,'wpirazzifj',3114.10),(561,'cmcenhillfk',3660.72),(562,'wleggfl',5233.26),(563,'ycadorefm',4096.45),(564,'pdibdallfn',4369.89),(565,'wcoryndonfo',7738.48),(566,'kmillierefp',8520.83),(567,'fchetwinfq',3753.91),(568,'crolffr',8792.42),(569,'gvairowfs',8773.19),(570,'tseadonft',1035.03),(571,'rkillichfu',8490.51),(572,'ekennealyfv',9829.33),(573,'kharcombefw',8593.80),(574,'jdanilchevfx',7518.64),(575,'kcartmerfy',8618.02),(576,'mheavensfz',302.37),(577,'kshureyg0',4127.71),(578,'laddlestoneg1',7524.74),(579,'rkivitsg2',5892.37),(580,'smallochg3',1763.55),(581,'jciciurag4',4205.71),(582,'roldeyg5',552.75),(583,'mslipperg6',9626.72),(584,'stitterellg7',1725.81),(585,'eperrellig8',5520.24),(586,'khyettg9',2542.40),(587,'okmentga',5487.17),(588,'cbergeaugb',4546.54),(589,'ojurgengc',2797.11),(590,'cdrysdallgd',126.66),(591,'mrohloffge',7310.58),(592,'cglenwrightgf',1742.91),(593,'poldroydegg',1036.51),(594,'hwalworchegh',6176.60),(595,'afoottitgi',3050.84),(596,'kleinstergj',431.15),(597,'cpauwelgk',4488.69),(598,'bgrebertgl',7863.62),(599,'rticegm',4066.07),(600,'wnetherwoodgn',8516.76),(601,'mgetcliffgo',2206.16),(602,'pspawtongp',1696.02),(603,'ebatcheldorgq',8480.02),(604,'thourihanegr',2817.78),(605,'gmizzengs',3117.23),(606,'kburnagegt',7542.40),(607,'lgokesgu',3412.31),(608,'gelvishgv',9461.28),(609,'caviesongw',5796.42),(610,'pberggx',7854.07),(611,'lvielgy',3985.92),(612,'mdellagz',3401.56),(613,'ebagotth0',3160.82),(614,'jdavydenkoh1',9261.66),(615,'kbambridgeh2',6318.22),(616,'rmoyesh3',3746.16),(617,'imainh4',2727.92),(618,'cabramamovhh5',7744.41),(619,'bgeeritsh6',321.19),(620,'alorenzoh7',978.35),(621,'msouthouseh8',5100.15),(622,'ewickardth9',4402.14),(623,'rhugonneauha',4229.16),(624,'qrhulehb',4291.05),(625,'ktiddemanhc',9802.10),(626,'vbrendelhd',1646.54),(627,'bgoulbournehe',1442.05),(628,'nmcvittyhf',3211.95),(629,'mleanderhg',9480.46),(630,'hschowenburghh',2489.09),(631,'dgohierhi',3840.79),(632,'tellesworthehj',8391.86),(633,'cpibsworthhk',1727.39),(634,'hmccullenhl',9022.53),(635,'nmatthewmanhm',2630.80),(636,'rblunehn',8768.44),(637,'abaccusho',2946.92),(638,'vfolominhp',9692.49),(639,'gblanthq',5815.06),(640,'lovendalehr',5424.37),(641,'oandrewarthahs',3986.88),(642,'sbeltonht',6707.68),(643,'itilzeyhu',6919.35),(644,'hfrancesconehv',203.30),(645,'thaggushw',564.92),(646,'ikibbehx',8938.83),(647,'glowdyanehy',4891.14),(648,'qbavridgehz',7578.32),(649,'smackroi0',5529.34),(650,'stilliardi1',4813.29),(651,'rmacnellyi2',2994.40),(652,'ureemani3',3684.40),(653,'mbarnewillei4',5459.21),(654,'jritmeyeri5',5513.28),(655,'mwalei6',5262.99),(656,'tgladdori7',6225.99),(657,'amineroi8',4763.26),(658,'lcranmorei9',9800.60),(659,'jswynia',6168.28),(660,'rorcasib',4411.96),(661,'mtribbleic',8703.58),(662,'msigwardid',1017.17),(663,'civanusyevie',3379.78),(664,'wleprovestif',4669.16),(665,'sdodellig',2799.57),(666,'rzanottiih',9943.96),(667,'rspeirii',8403.96),(668,'emccafferkyij',4050.32),(669,'mdiackik',639.52),(670,'dprisleyil',1023.90),(671,'bsinclarim',3215.16),(672,'bholyardin',775.10),(673,'sreynaultio',937.57),(674,'rpileticip',2664.89),(675,'sdowdaiq',5869.68),(676,'bkenvinir',3972.00),(677,'fwanstallis',4765.82),(678,'kdulwichit',4014.19),(679,'mdevliniu',7884.00),(680,'bbyeiv',8464.68),(681,'ecuthilliw',2690.95),(682,'smillenix',6858.95),(683,'bpitkiniy',7610.36),(684,'mogelbeiz',4589.72),(685,'cbeckersj0',6639.67),(686,'dschoutj1',8098.49),(687,'omillbankj2',6310.20),(688,'ajizhakij3',7124.92),(689,'awheldonj4',6896.70),(690,'dduchamj5',5981.32),(691,'ntruscottj6',6057.92),(692,'nstanionj7',4539.19),(693,'rgreetj8',8267.71),(694,'svongrollmannj9',5577.93),(695,'ljeduchja',8627.04),(696,'gcorcoranjb',7196.35),(697,'mcrushamjc',1188.73),(698,'ngoodrickejd',6125.58),(699,'gelgarje',1382.95),(700,'ereevesjf',6249.31),(701,'dsimmancejg',2916.52),(702,'hmunghamjh',8209.22),(703,'rswaineji',9116.58),(704,'ecelizjj',8753.86),(705,'bdekeepjk',1637.42),(706,'wsielyjl',6016.52),(707,'fgarrattjm',2904.15),(708,'lkibbeejn',4517.82),(709,'dchristoforoujo',4314.16),(710,'achurchilljp',5756.00),(711,'bkeeneyjq',3090.95),(712,'ggorrissenjr',4498.60),(713,'lseftonjs',8712.71),(714,'dtoyerjt',4388.51),(715,'lmacbainju',2065.85),(716,'nsibbitjv',4433.51),(717,'pturnerjw',2982.33),(718,'cbartolomeonijx',3272.66),(719,'blanferejy',6142.65),(720,'abettridgejz',7353.79),(721,'gspurdonk0',8095.53),(722,'kaldayk1',7039.66),(723,'mohickeek2',2382.63),(724,'adeemk3',6552.34),(725,'tdillingstonek4',9886.46),(726,'sferrask5',3620.78),(727,'vlaityk6',4778.39),(728,'ccostink7',9933.65),(729,'hmanzellk8',8431.93),(730,'hvanhovek9',3365.88),(731,'bwillettka',8420.62),(732,'mmariottekb',8381.90),(733,'nalbonkc',4451.52),(734,'bleportkd',8197.15),(735,'nmaxwellke',8411.42),(736,'aharcekf',427.80),(737,'jrobertshawkg',9713.70),(738,'lgathercoalkh',9394.30),(739,'jbeekmanki',3880.97),(740,'mlagnekj',4171.79),(741,'dblaszkiewiczkk',2148.22),(742,'cstorrierkl',6664.01),(743,'cvaggskm',4002.93),(744,'gcleaverkn',2383.05),(745,'jsowteko',5577.94),(746,'ecurriekp',4683.69),(747,'sheymeskq',6045.55),(748,'cnealkr',1139.62),(749,'rpalluschekks',5203.28),(750,'mmulqueenykt',8838.08),(751,'mlamckenku',2964.28),(752,'jkristufekkv',3617.61),(753,'cjelleykw',6089.73),(754,'mmcgrannkx',8820.88),(755,'rcaddyky',6978.21),(756,'leedekz',2902.39),(757,'dbogeysl0',4910.20),(758,'csimonettil1',1922.49),(759,'vcursonl2',1421.00),(760,'tmcpikel3',8622.37),(761,'djedrasikl4',1446.30),(762,'jripperl5',5548.41),(763,'qmoulsterl6',20.40),(764,'hdeambrosil7',1132.16),(765,'dbarrassel8',6907.08),(766,'bpocknelll9',5894.31),(767,'mfarryannla',1423.95),(768,'tpidgeleylb',8381.02),(769,'kvasyushkhinlc',8997.51),(770,'bboakeld',253.61),(771,'sheintzle',9080.90),(772,'lgrimelf',4178.42),(773,'ckingscotelg',3449.03),(774,'ballanbylh',5131.85),(775,'tphilippardli',4053.41),(776,'talfordelj',8616.03),(777,'dthurlbylk',7893.12),(778,'jtarrll',9742.46),(779,'mcolliplm',4611.52),(780,'holdcroftln',4311.35),(781,'emccrohonlo',2832.38),(782,'rbeveridgelp',2613.23),(783,'jlackeyelq',3940.38),(784,'gmatouseklr',2435.78),(785,'bouverls',1802.40),(786,'vdaudlt',2134.59),(787,'meschalottelu',9333.53),(788,'thenaughanlv',7378.11),(789,'gleftridgelw',9349.93),(790,'gbunninglx',5218.01),(791,'smoratly',7839.01),(792,'jmusgrovelz',7022.48),(793,'yhandscombem0',5583.51),(794,'mrivalm1',8106.07),(795,'dpickthornem2',7506.90),(796,'grackhamm3',6815.11),(797,'srootesm4',2064.48),(798,'lmaciasm5',4016.95),(799,'svanlintm6',7317.48),(800,'psellerm7',1509.03),(801,'wmcettrickm8',3557.00),(802,'akunkelm9',5602.50),(803,'medgcumbema',5839.55),(804,'dtideymb',2923.51),(805,'spennermc',5739.27),(806,'kcreamermd',7615.89),(807,'aclemenzome',3050.33),(808,'bcantomf',9464.39),(809,'kgamblinmg',1021.58),(810,'talesmh',5767.16),(811,'haylenmi',1047.37),(812,'tstilemanmj',1465.68),(813,'mdebullionmk',6906.06),(814,'anewlandsml',5910.08),(815,'frobynsmm',5816.37),(816,'asongermn',8471.80),(817,'cbirdismo',1298.96),(818,'rzamboninimp',1263.50),(819,'femblinmq',4783.53),(820,'htotenmr',9416.99),(821,'fmcquorkellms',9085.34),(822,'smablymt',8417.88),(823,'smcgarriemu',2797.74),(824,'scotesfordmv',6309.57),(825,'dgyrgorwicxmw',821.66),(826,'mnewismx',1317.40),(827,'cmilbournmy',1611.98),(828,'lvannimz',6671.77),(829,'jmccloshn0',799.18),(830,'abiasionin1',9279.32),(831,'lellyattn2',3454.84),(832,'msymsonn3',3024.39),(833,'cbarrown4',8709.09),(834,'emelrossn5',685.98),(835,'gburgn6',137.59),(836,'emcdualln7',3804.61),(837,'amandryn8',5788.06),(838,'kmathien9',6930.38),(839,'mmilellana',4288.37),(840,'ksindallnb',960.30),(841,'dstangoenc',1467.86),(842,'aquaylend',3555.80),(843,'rbridgnellne',4035.01),(844,'edrowsfieldnf',1264.84),(845,'npitherickng',9850.63),(846,'ogettinsnh',8379.81),(847,'ddrableni',5607.42),(848,'xruggnj',2932.26),(849,'gantramnk',2592.82),(850,'erudolphnl',109.84),(851,'eminchellanm',2882.39),(852,'ahoffnernn',2499.55),(853,'bspirno',671.64),(854,'gjanssennp',2690.62),(855,'bmacveannq',3750.71),(856,'kcassellanr',7073.23),(857,'btwiddellns',7413.82),(858,'krickertsennt',3427.20),(859,'kbrosettinu',1396.00),(860,'ghebditchnv',1545.07),(861,'lwittiernw',9937.43),(862,'rbettisonnx',112.20),(863,'megdalny',3485.03),(864,'tdoughtynz',9925.56),(865,'pgrindlayo0',7760.97),(866,'hifflando1',6520.10),(867,'ckeppeo2',1209.33),(868,'mphairo3',380.39),(869,'tscutto4',6479.34),(870,'jszymanzyko5',9770.67),(871,'fdecorto6',1423.86),(872,'jwarsapo7',3695.50),(873,'tkroppo8',4994.79),(874,'mbetsero9',8796.28),(875,'fcraigheidoa',2791.82),(876,'swohlerob',5580.67),(877,'ksnelgroveoc',9266.36),(878,'dlankesterod',8543.16),(879,'kredselloe',2921.58),(880,'jandreeof',7876.75),(881,'cmantioneog',6577.57),(882,'pchaimoh',2583.32),(883,'agrimleyoi',7308.79),(884,'eantrimoj',6509.22),(885,'jyellopok',2087.75),(886,'alindseyol',7950.77),(887,'flivingstoneom',7271.13),(888,'jkellockon',4206.79),(889,'kcrowtheroo',8718.56),(890,'lpluckop',69.06),(891,'ptapeoq',6712.57),(892,'wsidebothamor',9786.93),(893,'lwaistallos',9780.81),(894,'jgrumbleot',3948.88),(895,'ddesmondou',3658.08),(896,'ccloneyov',8482.15),(897,'civanaevow',2375.97),(898,'imcknielyox',6646.72),(899,'atuxwelloy',5041.98),(900,'mbrosiusoz',4893.98),(901,'jmcdadep0',8194.73),(902,'wcaughtryp1',1175.49),(903,'ciorillop2',1016.59),(904,'cchristmasp3',4119.08),(905,'ataceyp4',9858.71),(906,'rkelseyp5',2194.07),(907,'gthurbyp6',239.61),(908,'cscirmanp7',9071.17),(909,'svanarsdallp8',9485.85),(910,'eminchentonp9',1636.73),(911,'mhiscokepa',8978.58),(912,'rswiggerpb',2734.42),(913,'ggroombridgepc',4284.15),(914,'wcrasswellpd',6882.97),(915,'kantliffpe',8768.49),(916,'thullandpf',5760.81),(917,'agirvinpg',7313.95),(918,'vdelahuntyph',3412.62),(919,'mrockinghampi',6845.09),(920,'gstoppspj',6570.63),(921,'ldankpk',4578.17),(922,'tbabinskipl',9586.66),(923,'gsapsfordepm',8228.98),(924,'pcharltonpn',309.94),(925,'rcartwightpo',6142.79),(926,'gquinceypp',6837.36),(927,'reggerpq',3646.07),(928,'mmeedendorpepr',2691.60),(929,'breadmireps',3058.59),(930,'lclaughtonpt',5031.28),(931,'fleadbeaterpu',5975.87),(932,'gmerriganpv',8849.04),(933,'ktuffinpw',9727.12),(934,'melbournepx',941.04),(935,'dtrickerpy',6728.39),(936,'redinburoughpz',6414.86),(937,'htabourierq0',3504.79),(938,'tlenihanq1',4268.45),(939,'krobillartq2',9016.82),(940,'rfilipsonq3',258.49),(941,'smackaileq4',3375.21),(942,'jitzakq5',2190.77),(943,'lgraemeq6',6424.35),(944,'tkhrishtafovichq7',3189.64),(945,'emarfeq8',4542.86),(946,'groskillyq9',433.28),(947,'cendriciqa',4043.11),(948,'jvonweldenqb',482.85),(949,'sshayesqc',5408.66),(950,'acogglesqd',7973.36),(951,'fbleackleyqe',5526.08),(952,'memsonqf',2244.83),(953,'rgowersqg',9008.03),(954,'egreenliesqh',814.71),(955,'bbattingqi',9015.48),(956,'skneeshaqj',290.99),(957,'jtillerqk',9889.10),(958,'blavisteql',143.88),(959,'chabbalqm',3507.80),(960,'epossellqn',7392.16),(961,'jkaygillqo',7633.33),(962,'awennamqp',7775.48),(963,'rmargerisonqq',5846.67),(964,'pmaciaszekqr',6806.33),(965,'agraffinqs',77.00),(966,'amansionqt',4069.01),(967,'keuelsqu',7564.30),(968,'pvandeveldeqv',6564.57),(969,'mtunesiqw',5114.17),(970,'dwebberqx',9272.41),(971,'cdrakesqy',2818.10),(972,'cpriterqz',1855.30),(973,'ksaphinr0',4039.34),(974,'wclapsonr1',9014.87),(975,'rhandesr2',2209.41),(976,'dmchenryr3',1820.61),(977,'nprestneyr4',6552.95),(978,'njeffryr5',7525.63),(979,'dcoldbather6',578.21),(980,'dhambricr7',9360.03),(981,'gpeircer8',128.08),(982,'frubertellir9',8323.28),(983,'rmionira',4373.07),(984,'mspottswoodrb',8310.80),(985,'lpoizerrc',7894.57),(986,'arappsrd',8574.05),(987,'gmcbethre',998.91),(988,'mluckwellrf',9335.35),(989,'dbilfootrg',8007.56),(990,'lmoriganrh',8949.06),(991,'jbuffyri',6938.31),(992,'amacscherierj',3157.66),(993,'umackneyrk',5958.09),(994,'cphittiplacerl',3394.24),(995,'mbedinrm',8390.84),(996,'egabbitasrn',5160.82),(997,'gdomeniciro',9537.49),(998,'qspoolerp',2958.51),(999,'cbaileyrq',2241.74),(1000,'eezzlerr',3317.47),(123123,'%someUsername%',24.00);
/*!40000 ALTER TABLE `Streamer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-03 16:54:18
