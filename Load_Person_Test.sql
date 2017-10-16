LOAD DATA LOCAL INFILE "C:\\Users\\cfee\\git\\tsvtocsv\\nameBasic.csv"
INTO TABLE mydb2.person
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '\\'
LINES TERMINATED BY '\r\n' STARTING BY ''
IGNORE 0 LINES;

LOAD DATA LOCAL INFILE "C:\\Users\\cfee\\git\\tsvtocsv\\titleBasic.csv"
INTO TABLE mydb2.title
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '\\'
LINES TERMINATED BY '\r\n' STARTING BY ''
IGNORE 0 LINES;

LOAD DATA LOCAL INFILE "C:\\Users\\cfee\\git\\tsvtocsv\\ratingBasic.csv"
INTO TABLE mydb2.rating
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '\\'
LINES TERMINATED BY '\r\n' STARTING BY ''
IGNORE 0 LINES;

LOAD DATA LOCAL INFILE "C:\\Users\\cfee\\git\\tsvtocsv\\episodeBasic.csv"
INTO TABLE mydb2.episode
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '\\'
LINES TERMINATED BY '\r\n' STARTING BY ''
IGNORE 0 LINES;

LOAD DATA LOCAL INFILE "C:\\Users\\cfee\\git\\tsvtocsv\\helpers\\titleGenreId.csv"
INTO TABLE mydb2.titlegenres
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '\\'
LINES TERMINATED BY '\r\n' STARTING BY ''
IGNORE 0 LINES;

LOAD DATA LOCAL INFILE "C:\\Users\\cfee\\git\\tsvtocsv\\helpers\\genreId.csv"
INTO TABLE mydb2.genres
FIELDS TERMINATED BY ',' ENCLOSED BY '"' ESCAPED BY '\\'
LINES TERMINATED BY '\r\n' STARTING BY ''
IGNORE 0 LINES;







