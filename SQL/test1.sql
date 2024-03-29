-- CREATE Tables --
/**
 * Simple User Table
 */
CREATE TABLE IF NOT EXISTS User_T (
  	userID 								SERIAL		  		NOT NULL	UNIQUE,
  	email                   			TEXT        		NOT NULL,
  	firstName 							TEXT 				NOT NULL,
  	lastName 							TEXT 				NOT NULL,
  	PRIMARY KEY (userID)
);

CREATE TABLE IF NOT EXISTS Department_T (
	deptID								SERIAL				NOT NULL	UNIQUE,
	locationID							TEXT				NOT NULL,
	budgetID							SERIAL				NOT NULL,
	PRIMARY KEY (deptID)
);

CREATE TABLE IF NOT EXISTS Asset_T (
  	assetID								SERIAL				NOT NULL	UNIQUE,
  	userID								SERIAL				NOT NULL,
  	status								TEXT				NOT NULL,
  	model								TEXT				NOT NULL,
  	asset_name							TEXT				NOT NULL,
  	deptID								SERIAL				NOT NULL	UNIQUE,
  	PRIMARY KEY (assetID),
  	FOREIGN KEY (userID) REFERENCES User_T (userID),
	FOREIGN KEY (deptID) REFERENCES Department_T (deptID)
);


CREATE TABLE IF NOT EXISTS Permission_T (
	userID								SERIAL				NOT NULL	UNIQUE,
	roleID								TEXT				NOT NULL,
	firstName							TEXT				NOT NULL,
	lastName							TEXT				NOT NULL,
	PRIMARY KEY (roleID),
	FOREIGN KEY (userID) REFERENCES User_T (userID)
);
