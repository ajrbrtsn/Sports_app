DROP TABLE matches;
DROP TABLE teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    stadium VARCHAR (255)
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    home_team INT REFERENCES teams(id) ON DELETE CASCADE, 
    away_team INT REFERENCES teams(id) ON DELETE CASCADE,
    home_score INT,
    away_score INT
);