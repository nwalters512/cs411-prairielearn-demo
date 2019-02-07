CREATE TABLE Students (
  NetId VARCHAR(10),
  FirstName VARCHAR(255),
  LastName VARCHAR(255),
  Department VARCHAR(100),
  PRIMARY KEY (NetID)
);

CREATE TABLE Enrollments (
  NetId VARCHAR(10),
  CRN INT,
  Credits INT,
  Score REAL,
  PRIMARY KEY (NetId, CRN)
);

INSERT INTO Students VALUES
  ("nwalter2", "Nathan", "Walters", "CS"),
  ("rahulr2", "Rahul", "Rameshbabu", "CE"),
  ("ejones3", "Evan", "Jones", "CS");

INSERT INTO Enrollments VALUES
  ("nwalter2", 123, 3, 95),
  ("rahulr2", 123, 3, 100);
