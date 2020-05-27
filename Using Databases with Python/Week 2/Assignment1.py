'''Counting Organizations
This application will read the mailbox data (mbox.txt) and count the number of email messages per organization
(i.e. domain name of the email address) using a database with the following schema to maintain the counts.

CREATE TABLE Counts (org TEXT, count INTEGER)

You can use this code as a starting point for your application: http://www.py4e.com/code3/emaildb.py.

The data file for this application is the same as in previous assignments: http://www.py4e.com/code3/mbox.txt.'''

import re
import sqlite3



conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'
fh = open(fname)
for line in fh:
	if not line.startswith('From: ') : continue
	pieces = line.split()[1]
	org = pieces.split('@')[1]

	cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
	row = cur.fetchone()
	if row is None:
		cur.execute('''INSERT INTO Counts (org, count)
				VALUES ( ?, 1 )''', ( org, ) )
	else :
		cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
			(org, ))

conn.commit()


sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print(' ')
print("COUNTS:")
for row in cur.execute(sqlstr) :
    print(str(row[0]), row[1])

cur.close()
