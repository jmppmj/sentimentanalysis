import sqlite3
import pandas as pd
import plotly
import plotly.graph_objs
from plotly.graph_objs import Bar, Scatter, Marker, Layout, Margin

#generates bar chart from SQLite data (sentiment analysis results and title)

def graphRes():
    conn = sqlite3.connect("test.db")
    sq = "SELECT title as Post_Title, sent as Sentiment_Analysis FROM merge;"
    df = pd.read_sql(sq, conn)
    
    plotly.offline.plot({
        "data": [Bar(x = df.Post_Title, y = df.Sentiment_Analysis)],
        "layout": Layout(title = "Comment Sentiment Analysis on Top 25 /r/politics Posts (from Last 24 Hrs)", margin=Margin(b=200))
    })
    
    #close connection
    conn.close()
