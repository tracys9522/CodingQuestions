#Use SQLite to create schema and display results
#Tracy Sun

import sqlite3

#connection to init.db file
conn = sqlite3.connect('init.db')
c = conn.cursor()

#c.execute("DROP TABLE car;")

#create table
c.execute("""CREATE TABLE car (
    name text,
    cars text
    )""")

#insert data
c.execute("INSERT INTO car VALUES('Rick','Corvette Z06')")
c.execute("INSERT INTO car VALUES('Rick','Lotus Exite S')")
c.execute("INSERT INTO car VALUES('Rick','BMW M3')")
c.execute("INSERT INTO car VALUES('John','BMW 320d')")
c.execute("INSERT INTO car VALUES('John','Mercedes SLK AMG')")
c.execute("INSERT INTO car VALUES('Zing','Toyota Alphard')")
c.execute("INSERT INTO car VALUES('Zing','Mercedes Sprinter')")
c.execute("INSERT INTO car VALUES('Nan','Toyota Camry')")
c.execute("INSERT INTO car VALUES('Nan','Porsche 911')")
c.execute("INSERT INTO car VALUES('Nan','BMW M5')")
c.execute("INSERT INTO car VALUES('Nan','Jaguar')")
c.execute("INSERT INTO car VALUES('Nan','TukTuk')")
c.execute("INSERT INTO car VALUES('Nan','Mini Cooper')")
c.execute("INSERT INTO car VALUES('Nan','Honda Jazz')")

conn.commit()

#select data order by name
c.execute("SELECT * FROM CAR")

ar = [[str(item) for item in results] for results in c.fetchall()]
for row in ar:
    print(str(row[0])+", "+str(row[1]))
conn.close()
