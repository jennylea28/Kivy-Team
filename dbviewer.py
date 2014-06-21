import sqlite3 as lite
import sys
import datetime
from collections import namedtuple

con = None


year = None
month = None
day = None 
hour  = None
minute = None
second = None

android = 0
twitter = 0
odo = 0
facebook = 0
spotify = 0


try:
    con = lite.connect('ourdatabase.sqlite')
    
    cur = con.cursor()    

    a = cur.execute('SELECT * FROM "notification";')
    
    data = a.fetchall()
	
    for d in data:
        tub = namedtuple("tub"," second minute hour day month year type")
    	app = str(d[0])
    	app= app.split(".")
    	del app[0]
        typey=str(app[0])



    	time = str(d[-1]) 
    	time = time.split("T")
        date_time = time[0]
        clock_time= time[1]
        date_time = date_time.split("-")
        clock_time = clock_time.split(":")

        year = int(date_time[0])
        month = int(date_time[1])
        day = int(date_time[2])
        hour  = int(clock_time[0])
        minute = int(clock_time[1])


        #gets rid of the z on second
        second = list(clock_time[2])
        del second[-1]
        second = "".join(second)
        second = int(second)


        month_converter= {   1:"January",
                            2:"February",
                            3:"March",
                            4:"April",
                            5: "May",
                            6: "June",
                            7: "July",
                            8: "August",
                            9: "September",
                            10:"October",
                            11:"November",
                            12: "December"}    

        test = tub(second,minute,hour,day,month,year,typey)
        if test.type == "android": 
            android +=1
        if test.type == "twitter":
            twitter +=1
        if test.type == "odo":
            odo += 1
        if test.type == "facebook":
            facebook +=1
        if test.type == "spotify":
            spotify +=1   

    print "android :"+str(android) 
    print "twitter :"+str(twitter) 
    print "odo :"+str(odo) 
    print "facebook :"+str(facebook) 
    print "spotify :"+str(spotify) 
    
        


except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()