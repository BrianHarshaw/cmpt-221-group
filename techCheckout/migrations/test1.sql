CREATE TABLE IF NOT EXISTS User_T (
  	userID 								SERIAL		  		NOT NULL	UNIQUE,
  	email                   					TEXT        			NOT NULL,
  	firstName 							TEXT 				NOT NULL,
  	lastName 							TEXT 				NOT NULL,
  	PRIMARY KEY (userID)
);

CREATE TABLE IF NOT EXISTS Asset_T (
  	assetID								SERIAL				NOT NULL	UNIQUE,
  	userID								SERIAL				NOT NULL	UNIQUE,
  	status								TEXT				NOT NULL,
  	model								TEXT				NOT NULL,
  	asset_name							TEXT				NOT NULL,
  	deptID								SERIAL				NOT NULL	UNIQUE,
  	PRIMARY KEY (assetID),
  	FOREIGN KEY (userID) REFERENCES User_T,
	
);

CREATE TABLE IF NOT EXISTS Deptarment_T (
	deptID								SERIAL				NOT NULL	UNIQUE,
	locationID							TEXT				NOT NULL,
	budgetID							SERIAL				NOT NULL,
	PRIMARY KEY (deptID),
	FOREIGN KEY (deptID) REFERENCES Asset_T,
);

CREATE TABLE IF NOT EXISTS Permission_T (
	userID								SERIAL				NOT NULL	UNIQUE,
	roleID								TEXT				NOT NULL,
	firstName							TEXT				NOT NULL,
	lastName							TEXT				NOT NULL,
	PRIMARY KEY (roleID),
	FOREIGN KEY (userID) REFERENCES User_T,
);