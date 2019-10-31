#Use SQLite to create schema and display results
#Tracy Sun

import sqlite3

#connection to init.db file
conn = sqlite3.connect('init.db')
c = conn.cursor()

#select data having count greater than 2 
c.execute("SELECT name,count(*) FROM CAR group by name having count(*)>2")

#print results
ar = [[str(item) for item in results] for results in c.fetchall()]
for row in ar:
    print(str(row[0])+", "+str(row[1]))
conn.close()
