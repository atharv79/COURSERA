'''FIRST DATABASE
install the SQLite Browser from http://sqlitebrowser.org/
create a SQLITE database or use an existing database and create a table in the database called "Ages":CREATE TABLE Ages ( 
  
  name VARCHAR(128), 
  age INTEGER
  )
  
Make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Alexx', 32);
INSERT INTO Ages (name, age) VALUES ('Rosea', 29);
INSERT INTO Ages (name, age) VALUES ('Krishan', 36);
INSERT INTO Ages (name, age) VALUES ('Devlin', 18);
INSERT INTO Ages (name, age) VALUES ('Addison', 23);

Once the inserts are done, run the following SQL command:
SELECT hex(name || age) AS X FROM Ages ORDER BY X'''
