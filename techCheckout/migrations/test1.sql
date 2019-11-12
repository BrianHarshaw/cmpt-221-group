DROP TABLE IF EXISTS Roles;
DROP TABLE IF EXISTS Users;

CREATE TABLE IF NOT EXISTS Role_T (
    role_id         SERIAL          NOT NULL        UNIQUE,
    role_name        TEXT            NOT NULL,
    PRIMARY KEY(role_id)
);

CREATE TABLE IF NOT EXISTS Department_T (
	department_id						SERIAL				NOT NULL	UNIQUE,
	location_id							TEXT				NOT NULL,
	budget_id							SERIAL				NOT NULL,
	PRIMARY KEY (department_id)
);

CREATE TABLE IF NOT EXISTS User_T (
  	user_id 								SERIAL		  		NOT NULL	UNIQUE,
  	email                   			TEXT        		NOT NULL,
  	password_hash                        TEXT                NOT NULL,
  	first_name 							TEXT 				NOT NULL,
  	last_name 							TEXT 				NOT NULL,
  	phone_number                         BIGINT,
  	role_id                              INT                 NOT NULL,
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



CREATE TABLE IF NOT EXISTS Permission_T (
	user_id								SERIAL				NOT NULL	UNIQUE,
	role_id								TEXT				NOT NULL,
	first_name							TEXT				NOT NULL,
	last_name							TEXT				NOT NULL,
	PRIMARY KEY (role_id),
	FOREIGN KEY (user_id) REFERENCES User_T
);