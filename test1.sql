-- CREATE Tables --
/**
 * Simple User Table
 */
CREATE TABLE IF NOT EXISTS Users_T (
  userID 								SERIAL		  		NOT NULL	UNIQUE,
  email                   				TEXT        		NOT NULL,
  firstName 							TEXT 				NOT NULL,
  lastName 								TEXT 				NOT NULL,
  PRIMARY KEY (userID)
);

CREATE TABLE IF NOT EXISTS Assets_T (
  assetID								SERIAL				NOT NULL	UNIQUE,
  userID								SERIAL				NOT NULL,
  status								TEXT				NOT NULL,
  model									TEXT				NOT NULL,
  asset_name							TEXT				NOT NULL,
  deptID								SERIAL				NOT NULL,
  PRIMARY KEY (assetID),
  CONSTRAINT Assets_T FOREIGN KEY (userID) REFERENCES Users_T (userID)
);

INSERT INTO Users_T (userID, email, firstName, lastName) VALUES ('2', '@gmail.com', 'jon', 'smith');
INSERT INTO Assets_T (assetID, userID, status, model, asset_name, deptID) VALUES 
('1', '2', 'working', '1', 'laptop', '0');

SELECT * FROM Assets_T;