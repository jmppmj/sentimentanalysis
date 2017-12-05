import sqlite3

#deletes empty comments in database

def deletecommentsindb():
    #connect to database
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()
    #execute query
    sql = "DELETE FROM sen WHERE comments = '[]';"
    cur.execute(sql)
    #commit changes
    conn.commit()
    #close connection
    cur.close()
    conn.close()
