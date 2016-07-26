CREATE TABLE user(
	`id` int(11) NOT NULL AUTO_INCREMENT,
	username varchar(255) NOT NULL UNIQUE,
    pass varchar(255) NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE gpsPoints(
	user_id int(11) NOT NULL,
    latitude Decimal(9,6) NOT NULL,
    longitude Decimal(9,6) NOT NULL, 
    gps_time timestamp NOT NULL,
    PRIMARY KEY (user_id, latitude, longitude, gps_time),
    CONSTRAINT `FK_user` FOREIGN KEY (user_id) REFERENCES user (`id`) ON DELETE CASCADE ON UPDATE NO ACTION
);
  
