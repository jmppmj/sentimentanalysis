import sqlite3

#merges comments by title into a new table, creates id for each title/group of comments, and cleans up titles

def mergecomments():
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    
    sq = "CREATE TABLE merge (id INTEGER PRIMARY KEY autoincrement, title text, comments text, sent INTEGER);"
    cur.execute(sq)
    conn.commit()

    sq1 = "INSERT INTO merge (title, comments) SELECT title, GROUP_CONCAT(comments, ',') AS comments FROM sen GROUP BY title;"
    cur.execute(sq1)
    conn.commit()
    
    sq2 = "UPDATE merge SET title = REPLACE(title,'[','');"
    cur.execute(sq2)
    conn.commit()
    
    sq3 = "UPDATE merge SET title = REPLACE(title,']','');"
    cur.execute(sq3)
    conn.commit()

    sq4 = "UPDATE merge SET title = REPLACE(title,'/','');"
    cur.execute(sq4)
    conn.commit()

    sq5 = "UPDATE merge SET title = REPLACE(title,'\','');"
    cur.execute(sq5)
    conn.commit()
    
    #close connection
    cur.close()
    conn.close()
