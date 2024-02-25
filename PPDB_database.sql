CREATE TABLE Player (
    player_id INT PRIMARY KEY,
    username TEXT,
    email TEXT,
    password_hash VARCHAR(255),
    salt VARCHAR(255)
);

CREATE TABLE Village (
    village_id INT PRIMARY KEY,
    player_id INT REFERENCES Player
);

CREATE TABLE Building (
    building_id int PRIMARY KEY,
    name TEXT
);

CREATE TABLE Building_upgrade (
    building_id INT REFERENCES Building,
    level INT,
    cost INT,
    upgrade_time INT,
    PRIMARY KEY (building_id, level)
);

CREATE TABLE Player_inventory (
    player_id INT REFERENCES Player,
    gold INT,
    wood INT,
    iron INT,
    /* other resources */
    PRIMARY KEY (player_id)
);

CREATE TABLE Village_building (
    village_id INT REFERENCES Village,
    building_id INT REFERENCES Building,
    level INT,
    position_x INT,
    position_y INT,
    PRIMARY KEY (village_id, building_id)
);

CREATE TABLE Clan (
    clan_id INT PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE ClanMember (
    player_id INT REFERENCES Player PRIMARY KEY,
    clan_id INT REFERENCES Clan
);

CREATE TABLE Clan_invitation (
    player_id INT REFERENCES Player,
    clan_id INT REFERENCES Clan,
    PRIMARY KEY (player_id, clan_id)
);

CREATE TABLE Crops (
    crop_id INT PRIMARY KEY,
    name TEXT,
    grow_time INT
);

CREATE TABLE Livestock (
    livestock_id INT PRIMARY KEY,
    name TEXT,
    production_time INT
);

CREATE TABLE Tasks (
    task_id INT
    /* other things */
);

CREATE TABLE EarningsLeaderboard (
    player_id INT references Player PRIMARY KEY,
    earnings INT
);