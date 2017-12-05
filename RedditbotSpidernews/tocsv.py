import sqlite3
import pandas

#generates CSV file with post titles and sentiment analysis results

def wtocsv():
    conn = sqlite3.connect("test.db")
    table = pandas.read_sql('SELECT title AS Post_Title, sent AS Sentiment_Analysis FROM merge', conn)
    table.to_csv('results.csv')

    #close connection
    conn.close()

