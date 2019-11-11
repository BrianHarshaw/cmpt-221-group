DROP TABLE IF EXISTS Roles;
DROP TABLE IF EXISTS Users;

CREATE TABLE IF NOT EXISTS Role_T (
    roleID          SERIAL          NOT NULL        UNIQUE,
    roleName        TEXT            NOT NULL,
    PRIMARY KEY(roleID)
);

CREATE TABLE IF NOT EXISTS Department_T (
	departmentID						SERIAL				NOT NULL	UNIQUE,
	locationID							TEXT				NOT NULL,
	budgetID							SERIAL				NOT NULL,
	PRIMARY KEY (departmentID)
);

CREATE TABLE IF NOT EXISTS User_T (
  	userID 								SERIAL		  		NOT NULL	UNIQUE,
  	email                   			TEXT        		NOT NULL,
  	passwordHash                        TEXT                NOT NULL,
  	firstName 							TEXT 				NOT NULL,
  	lastName 							TEXT 				NOT NULL,
  	phoneNumber                         BIGINT,
  	roleID                              INT                 NOT NULL,
  	PRIMARY KEY (userID),
  	FOREIGN KEY (roleID) REFERENCES Role_T
);

CREATE TABLE IF NOT EXISTS Asset_T (
  	assetID								SERIAL				NOT NULL	UNIQUE,
  	userID								SERIAL				NOT NULL	UNIQUE,
  	status								TEXT				NOT NULL,
  	model								TEXT				NOT NULL,
  	assetName							TEXT				NOT NULL,
  	deptID								SERIAL				NOT NULL	UNIQUE,
  	PRIMARY KEY (assetID),
  	FOREIGN KEY (userID) REFERENCES User_T
);



CREATE TABLE IF NOT EXISTS Permission_T (
	userID								SERIAL				NOT NULL	UNIQUE,
	roleID								TEXT				NOT NULL,
	firstName							TEXT				NOT NULL,
	lastName							TEXT				NOT NULL,
	PRIMARY KEY (roleID),
	FOREIGN KEY (userID) REFERENCES User_T
);