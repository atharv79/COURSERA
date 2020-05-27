''' Install the SQLite Browser from http://sqlitebrowser.org
Create a SQLITE database or use an existing database and create a table in the database called "Ages".

CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)

Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows 
and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Alexx', 32);
INSERT INTO Ages (name, age) VALUES ('Rosea', 29);
INSERT INTO Ages (name, age) VALUES ('Krishan', 36);
INSERT INTO Ages (name, age) VALUES ('Devlin', 18);
INSERT INTO Ages (name, age) VALUES ('Addison', 23);
Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X

AFTER THE ABOVE STEPS THE CODE RECEIVED : 41646469736F6E3233

'''
