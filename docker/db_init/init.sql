-- db_init/init.sql

-- Drop tables if they already exist
DROP TABLE IF EXISTS abilities;
DROP TABLE IF EXISTS operatives;
DROP TABLE IF EXISTS fraction;
DROP TABLE IF EXISTS gear_items;
DROP TABLE IF EXISTS strategic_ploy;
DROP TABLE IF EXISTS firefight_ploy;
DROP TABLE IF EXISTS weapon_special_rules;


-- Create killteams
CREATE TABLE IF NOT EXISTS fraction (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create operatives with embedded weapons JSON
CREATE TABLE IF NOT EXISTS operatives (
    id SERIAL PRIMARY KEY,
    fraction_id INT REFERENCES fraction(id),
    name TEXT NOT NULL,
    type TEXT,
    apl INT,
    move TEXT,
    save TEXT,
    wounds INT,
    weapons JSONB,
    abilities JSONB
    -- Now stores all weapon data as JSON
);

CREATE TABLE IF NOT EXISTS gear_items (
    id SERIAL PRIMARY KEY,
    fraction_id INTEGER NOT NULL REFERENCES fraction(id),
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS strategic_ploy (
    id SERIAL PRIMARY KEY,
    fraction_id INTEGER NOT NULL REFERENCES fraction(id),
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS firefight_ploy (
    id SERIAL PRIMARY KEY,
    fraction_id INTEGER NOT NULL REFERENCES fraction(id),
    name TEXT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE weapon_special_rules (
    id SERIAL PRIMARY KEY,
    rule TEXT
);