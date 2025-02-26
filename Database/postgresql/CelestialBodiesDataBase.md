# Celestial Bodies Database Project

**connection**: psql --username=freecodecamp --dbname=postgres

**creation command**: CREATE DATABASE universe;

**connecting to the db** : \c universe

## Creating galaxy, star, planet and moon dbs

    create table galaxy(galaxy_id INT NOT NULL UNIQUE PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1), name varchar(100) NOT NULL UNIQUE,
    galaxy_description text, galaxy_age_in_millions_of_years numeric(12,2), galaxy_type varchar(50), galaxy_distance_from_earth numeric(12,2),
    number_of_planets int, number_of_stars int, galaxy_has_a_nearby_blackhole boolean);

    create table planet(planet_id INT NOT NULL UNIQUE PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1), name varchar(100) NOT NULL UNIQUE,
    planet_description text, planet_age_in_millions_of_years numeric(12,2), planet_type varchar(50), planet_distance_from_earth numeric(12,2),
    number_of_moons_planet_has int, planet_has_lifeforms boolean, planet_has_a_nearby_blackhole boolean, star_id int not null references star(star_id) );

    create table star(star_id INT NOT NULL UNIQUE PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1), name varchar(100) NOT NULL UNIQUE,
    star_description text, star_age_in_millions_of_years numeric(12,2), star_type varchar(50), star_distance_from_earth numeric(12,2),
    number_of_planets_star_has int, star_has_lifeforms boolean, star_has_a_nearby_blackhole boolean, galaxy_id int not null references galaxy(galaxy_id));

    create table moon(moon_id INT NOT NULL UNIQUE PRIMARY KEY GENERATED ALWAYS AS IDENTITY (START WITH 1), name varchar(100) NOT NULL UNIQUE, moon_description text,
    moon_age_in_millions_of_years numeric(12,2), moon_type varchar(50), moon_distance_from_earth numeric(12,2), which_planet_it_belongs_to varchar(50),
    moon_has_water boolean, what_count_is_this_moon int, moon_has_lifeforms boolean, moon_has_a_nearby_blackhole boolean, planet_id int not null references planet(planet_id));

    CREATE TABLE space_station (
    space_station_id INT PRIMARY KEY,
    space_station_name VARCHAR(255),
    space_station_description TEXT,
    space_station_orbit VARCHAR(255)
    );

    CREATE TABLE galaxy_planet_moon_space_station (
    galaxy_id INT,
    planet_id INT,
    moon_id INT,
    space_station_id INT,
    PRIMARY KEY (galaxy_id, planet_id, moon_id, space_station_id),
    FOREIGN KEY (galaxy_id) REFERENCES galaxy(galaxy_id),
    FOREIGN KEY (planet_id) REFERENCES planet(planet_id),
    FOREIGN KEY (moon_id) REFERENCES moon(moon_id),
    FOREIGN KEY (space_station_id) REFERENCES space_station(space_station_id)
    );

## Commands for dumping and recreating db on vm

    pg_dump -cC --inserts -U freecodecamp universe > universe.sql
    psql -U postgres < universe.sql

## Data Entry

    insert into galaxy(name,galaxy_description,galaxy_age_in_millions_of_years,galaxy_type,galaxy_distance_from_earth,number_of_planets,number_of_stars,galaxy_has_a_nearby_blackhole) values ('Andromeda','Spiral galaxy',1000,'Spiral',2.5370,1000,1000000,false), ('Milky Way','Barred spiral galaxy',13600,'Barred Spiral',0,200,200000,false),('Triangulum','Spiral galaxy',3000,'Spiral',3,500,500000,true), ('Sombrero','Unbarred spiral galaxy',31000,'Unbarred Spiral',31,100,100000,false),('Pinwheel','Face-on spiral galaxy',20000,'Face-on Spiral',20,200,200000,true), ('Whirlpool','Grand-design spiral galaxy',15000,'Grand-design Spiral',15,300,300000,false),('Black Eye','Spiral galaxy',10000,'Spiral',10,400,400000,true),('Cigar','Irregular galaxy',8000,'Irregular',8,500,500000,false),('Hoag s Object','Ring galaxy',12000,'Ring Galaxy',12,600,600000,true),('Cartwheel','Ring galaxy',15000,'Ring Galaxy',15,700,700000,false);

    insert into star(name, star_description, star_age_in_millions_of_years , star_type , star_distance_from_earth , number_of_planets_star_has , star_has_lifeforms , star_has_a_nearby_blackhole , galaxy_id) values ('Sun','G-type main-sequence star',4600,'G-type Main-sequence',0,8,false,false,2),('Proxima Centauri','M-type red dwarf',4850,'M-type Red Dwarf',4.2400,2,false,false,2),('Alpha Centauri A','G-type main-sequence star',4850,'G-type Main-sequence',4.3700,2,false,false,2),('Betelgeuse','Red supergiant','800','Red Supergiant','640','0',false,false,2),('Rigel','Blue-white supergiant','800','Blue-white Supergiant','860','0',false,false,2),('Deneb','Blue-white supergiant','200','Blue-white Supergiant','1400','0',false,false,2),('Vega','White main-sequence star','500','White Main-sequence','25','0',false,false,2),('Capella','Yellow-orange giant','500','Yellow-orange Giant','42','0',false,false,2),('Arcturus','Orange giant','700','Orange Giant','36','0',false,false,2),('Aldebaran','Orange giant','500','Orange Giant','65','0',false,false,2);

    insert into planet(name,planet_description,planet_age_in_millions_of_years,planet_type,planet_distance_from_earth,number_of_moons_planet_has,planet_has_lifeforms,planet_has_a_nearby_blackhole,star_id) values ('Mercury','Innermost planet',4600.0000,'Rocky','0.3900','0',false,false,1),('Venus','Hottest planet',4600.0000,'Rocky','0.7200','0',false,false,1),('Earth','Third planet from the Sun',4600.0000,'Rocky',0.0000,1,true,false,1),('Mars','Red planet',4600.0000,'Rocky',0.5200,2,false,false,1),('Jupiter','Largest planet',4600.0000,'Gas Giant',5.20,'79',false,false,1),('Saturn','Ringed planet',4600.0000,'Gas Giant','9.5000','62',false,false,1),('Uranus','Tilted planet',4600.0000,'Ice Giant','19.1000','27',false,false,1),('Neptune','Coldest planet',4600.0000,'Ice Giant','30.1000',14,false,false,1),('Proxima b','Exoplanet','4850.0000','Rocky','4.2400','0',false,false,2),('Alpha Centauri Bb','Exoplanet','4850.0000','Rocky','4.3700','0',false,false,3),('Betelgeuse b','Exoplanet','800.0000','Gas Giant','640.0000','0',false,false,4),('Rigel b','Exoplanet','800.0000','Gas Giant','860.0000','0',false,false,5),('Deneb b','Exoplanet','200.0000','Gas Giant','1400.0000','0',false,false,6),('Vega b','Exoplanet','500.0000','Rocky','25.0000','0',false,false,7),('Capella b','Exoplanet','500.0000','Gas Giant','42.0000','0',false,false,8);

    insert into moon(name,moon_description,moon_age_in_millions_of_years,moon_type,moon_distance_from_earth,which_planet_it_belongs_to,moon_has_water,what_count_is_this_moon,moon_has_lifeforms,moon_has_a_nearby_blackhole,planet_id) values ('The Moon','Earth s moon',4600.0000,'Rocky',0.0000,'Earth',true,1,false,false,3),('Phobos','Mars moon',4600.0000,'Rocky',0.5200,'Mars',false,1,false,false,4),('Deimos','Mars moon',4600.0000,'Rocky',0.5200,'Mars',false,2,false,false,4),('Io','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,1,false,false,5),('Europa','Jupiter's moon',4600.0000,'Rocky',5.20,'Jupiter',true,2,false,false,5),('Ganymede','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,3,false,false,5),('Callisto','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,4,false,false,5),('Amalthea','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,5,false,false,5),('Thebe','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,6,false,false,5),('Metis','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,7,false,false,5),('Adrastea','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,8,false,false,5),('Themisto','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,9,false,false,5),('Carme','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,10,false,false,5),('Pasiphae','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,11,false,false,5),('Sinope','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,12,false,false,5),('Leda','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,13,false,false,5),('Himalia','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,14,false,false,5),('Lysithea','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,15,false,false,5),('Elara','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,16,false,false,5),('Dia','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,17,false,false,5);

    insert into moon(name,moon_description,moon_age_in_millions_of_years,moon_type,moon_distance_from_earth,which_planet_it_belongs_to,moon_has_water,what_count_is_this_moon,moon_has_lifeforms,moon_has_a_nearby_blackhole,planet_id) values ('Metis','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,7,false,false,5),('Adrastea','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,8,false,false,5),('Themisto','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,9,false,false,5),('Carme','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,10,false,false,5),('Pasiphae','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,11,false,false,5),('Sinope','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,12,false,false,5),('Leda','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,13,false,false,5),('Himalia','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,14,false,false,5),('Lysithea','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,15,false,false,5),('Elara','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,16,false,false,5),('Dia','Jupiter s moon',4600.0000,'Rocky',5.20,'Jupiter',false,17,false,false,5);

## Creating full join to display related info

    SELECT 
    g.name,
    p.name,
    m.name,
    ss.space_station_name
    FROM 
    galaxy g
    FULL JOIN galaxy_planet_moon_space_station j 
        ON g.galaxy_id = j.galaxy_id
    FULL JOIN planet p 
        ON j.planet_id = p.planet_id
    FULL JOIN moon m 
        ON j.moon_id = m.moon_id
    FULL JOIN space_station ss 
        ON j.space_station_id = ss.space_station_id;
