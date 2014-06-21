import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('ourdatabase.sqlite')
    
    cur = con.cursor()    

    a = cur.execute('SELECT * FROM "notification";')
    
    data = a.fetchall()
	
    for d in data:
    	app = str(d[0])
    	app= app.split(".")
    	del app[0]
    	app.append(d[-1]) 
    	print app
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()