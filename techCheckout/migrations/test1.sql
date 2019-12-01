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
	location						    TEXT				NOT NULL,
	budget							    BIGINT			    NOT NULL,
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
  	asset_id							SERIAL				NOT NULL	UNIQUE,
  	user_id								SERIAL				NOT NULL	UNIQUE,
  	status								TEXT				NOT NULL,
  	model								TEXT				NOT NULL,
  	asset_name							TEXT				NOT NULL,
  	dept_id								SERIAL				NOT NULL	UNIQUE,
  	PRIMARY KEY (asset_id),
  	FOREIGN KEY (user_id) REFERENCES User_T
);

/* Not necessary to use since you can just reference the roles table, but could be used
CREATE TABLE IF NOT EXISTS Permission_T (
	user_id								SERIAL				NOT NULL	UNIQUE,
	role_id								TEXT				NOT NULL,
	permission_level                    INT                 NOT NULL,
	first_name							TEXT				NOT NULL,
	last_name							TEXT				NOT NULL,
	PRIMARY KEY (role_id),
	FOREIGN KEY (user_id) REFERENCES User_T
);
*/

INSERT INTO Role_T(role_name) VALUES ('administrator');
INSERT INTO Role_T(role_name) VALUES ('student');
INSERT INTO Role_T(role_name) VALUES ('worker');
INSERT INTO Role_T(role_name) VALUES ('department head');
INSERT INTO Role_T(role_name) VALUES ('faculty');

INSERT INTO Department_T()

INSERT INTO User_T(email, password_hash, first_name, last_name, phone_number, role_id) VALUES ('brian.harshaw1@marist.edu', 'pbkdf2:sha256:150000$EtOqtq89$7cd8d6bbfc4005c348242921ccf4509e457ef23e26e7a9832d15a151f24c6a9f', 'Brian', 'Harshaw', '8608051042', 1);
INSERT INTO User_T(email, password_hash, first_name, last_name, phone_number, role_id) VALUES ('brian46harshaw@gmail.com','pbkdf2:sha256:150000$h4r1xums$b32c1a11fcd435826bbae4dfd8e7ecaba1b2f3b5842dfe17f9299abd385f9664','Test', 'Student','1111111111',2);
INSERT INTO User_T(email, password_hash, first_name, last_name, phone_number, role_id) VALUES ('brian2harshaw@gmail.com','pbkdf2:sha256:150000$h4r1xums$b32c1a11fcd435826bbae4dfd8e7ecaba1b2f3b5842dfe17f9299abd385f9664','Test', 'Faculty','1111111111',5);




