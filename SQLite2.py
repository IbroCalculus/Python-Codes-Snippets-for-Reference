import sqlite3

#1. CREATE DATABASE
'''
    conn = sqlite3.connect("MyDataBase.db") #extension can be anything. i.e .db, .sqlite3, .dbase, .ibrahim etc, preferrably .db
    cur = conn.cursor()                     #Handle for working with the database
    
    #Close database when you are done with the dbase file
    cur.close()
'''

#2. CREATE A TABLE
'''
    cur.execute (""" CREATE TABLE IF NOT EXISTS employee_records(
        ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        DIVISION TEXT NOT NULL,
        STARS INT NOT NULL
    )
    """)
'''

#3. ADD DATA TO DATABASE TABLE
'''
    cur.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
        VALUES(1,"Ibrahim","Software",5)
    """)
    # Alternatively, use: cur.execute(""" INSERT INTO employee_records(*) """) where * signifies ALL
    # or specify the particular fields to insert into if not all
    # But NOT NULL -> every field must have values, hence All i.e ID,NAME,DIVISION,STARS
    
    #Apply changes to db using commit
    conn.commit()
'''

#4. #ADD DATA TO DATABASE USING A FUNCTION WITH PARAMETERS
'''
    def insert_record(ID,NAME,DIVISION,STARS):
        cur.execute(""" INSERT INTO employee_records(ID,NAME,DIVISION,STARS)
            VALUES(?,?,?,?)""",(ID,NAME,DIVISION,STARS))
        # Alternatively, use: cur.execute(""" INSERT INTO employee_records(*) """) where * signifies ALL
        # or specify the particular fields to insert into if not all
        # But NOT NULL -> every field must have values, hence All i.e ID,NAME,DIVISION,STARS
    
        #Apply changes to db using commit
        conn.commit()
        print("Changes applied")
    
    insert_record(5,"Muhammad","Soldier",9)
    
    
    #Close database when you are done with the dbase file
    cur.close()
'''

#5. #READ DATA FROM DATABASE
