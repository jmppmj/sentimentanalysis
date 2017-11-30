<b>Comment Sentiment Analysis of the Top 25 Posts on a Subreddit (www.reddit.com) (top posts from the last 24 hrs)</b>

<b>Purpose of the program:</b>
To define, evaluate, and visualize overall public sentiment towards various news articles. 

Web scraper is set to https://www.reddit.com/r/politics/top/, but can be (theoretically) used on any similar subreddit by changing the address and (if needed) altering the XPath's within RedditbotSpider.py.

<b>What the program does:</b>
<ul>
<li>Web scraper connects to subreddit and collects the top 25 post titles, as well as comments within each post.</li>
<li>Data is inserted into a SQLite database.</li>
<li>Data is cleaned up: any rows lacking a comment are deleted.</li>
<li>Comments are combined for each corresponding title and placed into a new database table.
<li>A unique ID (1-25) is added for each title and corresponding group of comments.
<li>Lexicon (word-based) for sentiment analysis is applied to each set of comments.</li>
<li>Data visualization: an interactive (html) bar chart, CSV file, and completion window are generated.</li>
</ul>

<hr>

<b>Lexicon used to extract an overall sentiment level:</b>
<table style="width:100%">
  <tr>
    <th>Positive +1</th>
    <th>Negative -1</th> 
  </tr>
  <tr>
    <td>good</td>
    <td>fuck</td> 
  </tr>
  <tr>
    <td>great</td>
    <td>corrupt</td> 
  </tr>
    <tr>
    <td>happy</td>
    <td>stupid</td> 
  </tr>
    <tr>
    <td>win</td>
    <td>irrelevant</td> 
  </tr>
    <tr>
    <td>love</td>
    <td>colluding</td> 
  </tr>
    <tr>
    <td>nice</td>
    <td>horrible</td> 
  </tr>
    <tr>
    <td>authentic</td>
    <td>unfair</td> 
  </tr>
    <tr>
    <td>like</td>
    <td>guilty</td> 
  </tr>
    <tr>
    <td>fun</td>
    <td>foolish</td> 
  </tr>
    <tr>
    <td>appreciate</td>
    <td>hateful</td> 
  </tr>
</table>

<hr>

<b>How to run the program:</b>
<ul>
<li>Download and install <a href="https://sqlite.org/download.html">SQLite</a></li>
<li>Download and install <a href="https://www.python.org/downloads/">Python 3.6.3</a></li>
<li>Make sure your System PATH includes the path to Python's interpreter</li>
<li>In Windows Command Prompt do/install the following:</li><ul>
<li>pip3 install pandas</li>
<li>pip3 install scrapy</li>
<li>pip3 install plotly</li>
<li>pip install pypiwin32</li></ul>
<li>Download this repository & unzip it</li>
<li>sentimentanalysis-master->RedditbotSpider->right click on main.py, edit with IDLE->Run->Run Module
</ul>
Note: Before running the program a <i>second</i> time, move or delete the generated/results files: test.db, temp-plot.html, and results.csv out of the RedditbotSpider folder.

<hr>

<b>Tools/Libraries/Packages used:</b>
<ul>
<li><a href="https://www.python.org/downloads/">Python 3.6.3</a></li>
<li><a href="https://scrapy.org/">Scrapy 1.4</a></li>
<li><a href="https://sqlite.org/download.html">SQLite3</a></li>
<li><a href="https://pypi.python.org/pypi/pip">Pip/Pip3</a></li>
<li><a href="https://pandas.pydata.org/">Pandas</a></li>
<li><a href="https://plot.ly/python/">Plotly</a></li>
<li><a href="https://docs.python.org/3/library/tk.html">Tkinter</a></li>
</ul>
