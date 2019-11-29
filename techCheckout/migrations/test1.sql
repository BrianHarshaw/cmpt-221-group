DROP TABLE IF EXISTS Role_T;
DROP TABLE IF EXISTS User_T;
DROP TABLE IF EXISTS Asset_T;

CREATE TABLE IF NOT EXISTS Role_T (
    role_id         SERIAL          NOT NULL        UNIQUE,
    role_name       TEXT            NOT NULL,
    PRIMARY KEY(role_id)
);

CREATE TABLE IF NOT EXISTS Department_T (
	department_id						SERIAL				NOT NULL	UNIQUE,
	location_id							TEXT				NOT NULL,
	budget_id							SERIAL				NOT NULL,
	PRIMARY KEY (department_id)
);

CREATE TABLE IF NOT EXISTS User_T (
  	user_id 							SERIAL		  		NOT NULL	UNIQUE,
  	email                   			TEXT        		NOT NULL,
  	password_hash                       TEXT                NOT NULL,
  	first_name 							TEXT 				NOT NULL,
  	last_name 							TEXT 				NOT NULL,
  	phone_number                        BIGINT,
  	role_id                             INT                 NOT NULL,
  	PRIMARY KEY (user_id),
  	FOREIGN KEY (role_id) REFERENCES Role_T
);

CREATE TABLE IF NOT EXISTS Asset_T (
  	asset_id								SERIAL				NOT NULL	UNIQUE,
  	user_id								SERIAL				NOT NULL	UNIQUE,
  	status								TEXT				NOT NULL,
  	model								TEXT				NOT NULL,
  	asset_name							TEXT				NOT NULL,
  	dept_id								SERIAL				NOT NULL	UNIQUE,
  	PRIMARY KEY (asset_id),
  	FOREIGN KEY (user_id) REFERENCES User_T
);

INSERT INTO Role_T(role_name) VALUES ('Administrator');
INSERT INTO Role_T(role_name) VALUES ('Student');
INSERT INTO Role_T(role_name) VALUES ('Worker');
INSERT INTO Role_T(role_name) VALUES ('Department Head');
INSERT INTO Role_T(role_name) VALUES ('Faculty');

INSERT INTO User_T(email, password_hash, first_name, last_name, phone_number, role_id) VALUES ('brian.harshaw1@marist.edu', 'pbkdf2:sha256:F407E1D84DE41044FEAF978C975C71632F47138959D80D5018309F18088BC398', 'Brian', 'Harshaw', '8608051042', 1);

/*
Role table is taking the place of this for the time being
CREATE TABLE IF NOT EXISTS Permission_T (
	user_id								SERIAL				NOT NULL	UNIQUE,
	role_id								TEXT				NOT NULL,
	first_name							TEXT				NOT NULL,
	last_name							TEXT				NOT NULL,
	PRIMARY KEY (role_id),
	FOREIGN KEY (user_id) REFERENCES User_T
);

 */
