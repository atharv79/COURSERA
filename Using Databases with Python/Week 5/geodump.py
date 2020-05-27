'''Retrieving GEOData
Download the code from http://www.py4e.com/code3/geodata.zip - then unzip the file and edit where.data 
to add an address nearby where you live - don't reveal where you live. Then run the geoload.py to lookup
all of the entries in where.data (including the new one) and produce the geodata.sqlite. Then run 
geodump.py to read the database and produce where.js. You can run the programs and then scroll back to 
take your screen shots when the program finishes. Then open where.html to visualize the map. Take screen shots
as described below. Make sure that your added location shows in all three of your screen shots.'''

import sqlite3
import json
import codecs

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand = codecs.open('where.js', 'w', "utf-8")
fhand.write("myData = [\n")
count = 0
for row in cur :
    data = str(row[1].decode())
    try: js = json.loads(str(data))
    except: continue

    if not('status' in js and js['status'] == 'OK') : continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    if lat == 0 or lng == 0 : continue
    where = js['results'][0]['formatted_address']
    where = where.replace("'", "")
    try :
        print(where, lat, lng)

        count = count + 1
        if count > 1 : fhand.write(",\n")
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        fhand.write(output)
    except:
        continue

fhand.write("\n];\n")
cur.close()
fhand.close()
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
