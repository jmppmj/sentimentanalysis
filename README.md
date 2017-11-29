Comment Sentiment Analysis of the Top 25 Posts on a Subreddit (www.reddit.com) (top posts from the last 24 hrs)
Scraper is set to /r/politics, but can be used on any Subreddit by changing the address in RedditbotSpider.py



What the program does:
<ul>
<li>Data is scraped.</li>
<li>Inserted into a sqlite3 database.</li>
<li>Any rows lacking a comment are deleted.</li>
<li>Lexicon (word-based) for sentiment analysis applied to comments corresponding to a certain title.</li>
<li>Data visualization, including an interactive bar chart, CSV file, and completion window are generating using Plotly and Tkinter.</li>
</ul>

<hr>

How to run the program:
<ul>
<li>Install Python 3.6.3</li>
<li>Make sure System PATH includes the path to the Python interpreter</li>
<li>In Windows Command Prompt do/install the following:</li>
<li>pip3 install pandas</li>
<li>pip3 install scrapy</li>
<li>pip3 install plotly</li>
<li>pip install pypiwin32</li>
</ul>

<hr>

Tools/Libraries/Packages used:
<ul>
<li>Python 3.6.3</li>
<li>Scrapy 1.4</li>
<li>SQLite3</li>
<li>Pip/Pip3</li>
<li>Pandas</li>
<li>Plotly</li>
<li>Tkinter</li>
</ul>
