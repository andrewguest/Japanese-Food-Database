-- --------------------------------------------------------
-- Host:                         nkpl8b2jg68m87ht.cbetxkdyhwsb.us-east-1.rds.amazonaws.com
-- Server version:               10.1.34-MariaDB - MariaDB Server
-- Server OS:                    Linux
-- HeidiSQL Version:             10.2.0.5599
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for Japan
CREATE DATABASE IF NOT EXISTS `Japan` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `Japan`;

-- Dumping structure for table Japan.drink
CREATE TABLE IF NOT EXISTS `drink` (
  `drink_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `taste` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `region` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `url` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `date_added` datetime NOT NULL,
  `image_path` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`drink_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- Dumping data for table Japan.drink: ~0 rows (approximately)
/*!40000 ALTER TABLE `drink` DISABLE KEYS */;
INSERT INTO `drink` (`drink_id`, `name`, `taste`, `region`, `url`, `date_added`, `image_path`) VALUES
	(1, 'Uji Matcha Au Lait', 'green tea', 'Kyoto', 'https://www.bokksu.com/products/uji-matcha-au-lait', '2019-11-16 21:18:10', 'https://cdn.shopify.com/s/files/1/1083/2612/products/UjiMatchaAuLait_Package_2000x.jpg?v=1572020004');
/*!40000 ALTER TABLE `drink` ENABLE KEYS */;

-- Dumping structure for table Japan.food
CREATE TABLE IF NOT EXISTS `food` (
  `food_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `taste` varchar(50) NOT NULL,
  `region` varchar(50) DEFAULT NULL,
  `url` varchar(200) NOT NULL,
  `date_added` datetime NOT NULL,
  `image_path` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`food_id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4;

-- Dumping data for table Japan.food: ~18 rows (approximately)
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` (`food_id`, `name`, `taste`, `region`, `url`, `date_added`, `image_path`) VALUES
	(1, 'Hakata Mitsuki: Delicious Cheese', 'sweet', 'Fukoka', 'https://www.bokksu.com/products/hakata-mitsuki-delicious-cheese-financier-cake', '2019-11-11 19:12:04', 'https://cdn.shopify.com/s/files/1/1083/2612/products/market-hakata-mitsuki-delicious-cheese-financier-cake-16-pieces-3_2000x.jpg?v=1570833978'),
	(2, 'Okashinai Cheese Manju', 'sweet', 'Akita', 'https://www.bokksu.com/products/okashinai-cheese-manju?_pos=1&_sid=ec069d388&_ss=r', '2019-11-11 19:15:54', 'https://cdn.shopify.com/s/files/1/1083/2612/products/OkashinaiCheeseManju_Package_a8a2f985-07d6-4d6d-b828-779b300900d3_1200x.jpg?v=1570832705'),
	(3, 'Black Sesame Taiko: Kumamon Design', 'sweet', 'Kumamoto', 'https://www.bokksu.com/products/black-sesame-taiko-rice-cracker?_pos=1&_sid=daf9f6b4c&_ss=r', '2019-11-11 19:27:00', 'https://cdn.shopify.com/s/files/1/1083/2612/products/market-black-sesame-taiko-kumamon-design-10-pieces-1_1200x.jpg?v=1570833983'),
	(4, 'Kocha Black Tea Donut', 'sweet', 'Tokyo', 'https://www.bokksu.com/products/black-tea-donut?_pos=1&_sid=7ad26bcb2&_ss=r', '2019-11-11 19:29:00', 'https://cdn.shopify.com/s/files/1/1083/2612/products/market-kocha-black-tea-donut-6-pieces-1_2000x.jpg?v=1570832894'),
	(5, 'Kinako Kurumi Walnut Mochi', 'sweet', 'Nagano Prefecture', 'https://www.bokksu.com/products/kinako-walnut-mochi?_pos=1&_sid=5aa825ddc&_ss=r', '2019-11-11 19:29:55', 'https://cdn.shopify.com/s/files/1/1083/2612/products/market-kinako-kurumi-walnut-mochi-9-pieces-1_2000x.jpg?v=1570834107'),
	(6, 'Sanrio Characters: Halloween Cookie Assort', 'sweet', 'Okayama Prefecture', 'https://www.bokksu.com/products/sanrio-cookie-assort?_pos=1&_sid=e07d5d4a3&_ss=r', '2019-11-11 19:30:15', 'https://cdn.shopify.com/s/files/1/1083/2612/products/market-sanrio-characters-halloween-cookie-assortment-20-pieces-1_2000x.jpg?v=1570834114'),
	(7, 'Puchi Pure Gummy: Halloween Grape', 'sweet', 'Tokyo', 'https://www.bokksu.com/products/pure-gummy-halloween-grape?_pos=1&_sid=fa0a616c1&_ss=r', '2019-11-11 19:32:15', 'https://cdn.shopify.com/s/files/1/1083/2612/products/market-puchi-pure-gummy-halloween-grape-12-packs-1_1200x.jpg?v=1570834040'),
	(8, 'Cinnamon Fresh Yatsuhashi Daifuku', 'sweet', 'Nagano Prefecture', 'https://www.bokksu.com/products/nama-yatsuhashi-daifuku-mochi?_pos=1&_sid=30ca7f10e&_ss=r', '2019-11-11 19:33:15', 'https://cdn.shopify.com/s/files/1/1083/2612/products/CinnamonFreshYatsuhashiDaifuku_Tabling_1200x.jpg?v=1572014966'),
	(9, 'Fried Kakinotane: Kyoto Fresh Yatsuhashi Flavor', 'sweet', 'Osaka', 'https://www.bokksu.com/products/nama-yatsuhashi-kakino-tane?_pos=1&_sid=ad755a0a7&_ss=r', '2019-11-11 19:34:15', 'https://cdn.shopify.com/s/files/1/1083/2612/products/FriedKakinotaneKyotoFreshYatsuhashiFlavor_Package_1200x.jpg?v=1572013525'),
	(10, 'Matcha Chocolate Stick Cake', 'sweet', 'Osaka', 'https://www.bokksu.com/products/matcha-chocolate-stick-cake?_pos=1&_sid=062a0490f&_ss=r', '2019-11-11 19:35:15', 'https://cdn.shopify.com/s/files/1/1083/2612/products/MatchaChocolateStickCake_Package_1200x.jpg?v=1572015194'),
	(11, 'Kitsune no Shippo', 'sweet', 'Hokkaido', 'https://www.bokksu.com/collections/september-17-bokksu-memories-of-hokkaido/products/kitsunes-tail', '2019-11-13 16:47:30', 'https://cdn.shopify.com/s/files/1/1083/2612/products/past-snack-kitsune-s-tail-1_1200x.jpg?v=1559686261'),
	(12, 'Calpico Mochi', 'sweet', 'Tokyo', '', '2019-11-13 16:51:00', NULL),
	(13, 'Funwari Meijin Mochi Puffs: Hokkaido Milk', 'sweet', 'Niigata Prefecture', 'https://www.bokksu.com/products/milk-mochi?_pos=1&_sid=c75991484&_ss=r', '2019-11-13 16:57:00', 'https://cdn.shopify.com/s/files/1/1083/2612/products/market-funwari-meijin-mochi-puffs-milk-4-packs-1_1200x.jpg?v=1570833448'),
	(14, 'Natural Yeast Bread Chocolate', 'sweet', 'Gunma Prefecture', 'https://www.bokksu.com/products/natural-yeast-bread-chocolate', '2019-11-14 16:35:30', 'https://cdn.shopify.com/s/files/1/1083/2612/products/past-snack-natural-yeast-bread-chocolate-1_1200x.jpg?v=1559687163'),
	(15, 'Natural Yeast Bread: Hokkaido Cream', 'sweet', 'Tokyo', 'https://www.bokksu.com/products/natural-yeast-bread-hokkaido-cream-1-piece?_pos=2&_sid=9e18ead80&_ss=r', '2019-11-14 16:36:33', 'https://cdn.shopify.com/s/files/1/1083/2612/products/HokkaidoCreamBread_Package_2f68ea45-1f03-43de-9fae-4e434dd9f8c3_1200x.jpg?v=1570832710'),
	(16, 'Shiroi Koibito', 'sweet', 'Hokkaido', 'https://www.bokksu.com/products/shiroi-koibito?_pos=1&_sid=20952c501&_ss=r', '2019-11-14 16:42:00', 'https://cdn.shopify.com/s/files/1/1083/2612/products/market-shiroi-koibito-18-pieces-1_1200x.jpg?v=1570832826'),
	(17, 'White Black Thunder', 'sweet', 'Tokyo', 'https://www.napajapan.com/products/black-thunder-hokkaido-white-chocolate-bar', '2019-11-15 19:26:29', 'https://cdn.shopify.com/s/files/1/1334/9201/products/Black-Thunder-White-Chocolate_e8695a35-ab43-4e34-abb5-9227bc2dd9e6_1024x1024.JPG?v=1556456641'),
	(18, 'Chocolate Dorayaki', 'Sweet', 'Tokyo', 'https://japanhaul.com/products/chocolate-dorayaki?variant=31020987318324', '2019-11-17 15:19:01', 'https://cdn.shopify.com/s/files/1/1423/1710/products/1_9208_480x480.png?v=1572235815');
/*!40000 ALTER TABLE `food` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
