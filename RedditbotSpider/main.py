import sys
import os
sys.path.append('RedditbotSpider.spiders')
import sqlite3
import tkinter
from tkinter import *

from deletecomments import deletecommentsindb
from mergecom import mergecomments
from sen import *
from vis import graphRes
from tocsv import wtocsv
from twindow import *

#from RedditbotSpider.__init__ import *
#from RedditbotSpider.items import *
#from RedditbotSpider.middlewares import *
#from RedditbotSpider.pipelines import *
#from RedditbotSpider.settings import *

#from RedditbotSpider.spiders.__init__ import *
#from RedditbotSpider.spiders.RedditbotSpider import *
import RedditbotSpider

def main():
    
    #runs the spider
    os.system("scrapy crawl RedditbotSpider")
        
    #deletes empty comments
    deletecommentsindb()
        
    #merges comments, cleans up data
    mergecomments()
        
    #analyzes sentiment for all 25 post titles
    senti1()
    senti2()
    senti3()
    senti4()
    senti5()
    senti6()
    senti7()
    senti8()
    senti9()
    senti10()
    senti11()
    senti12()
    senti13()
    senti14()
    senti15()
    senti16()
    senti17()
    senti18()
    senti19()
    senti20()
    senti21()
    senti22()
    senti23()
    senti24()
    senti25()
        
    #generates graph
    graphRes()
        
    #generates CSV
    wtocsv()

main()
root = Tk()        
app = statusWindow(root)
root.geometry('600x150')
Text = tkinter.Label(root, text='Scraping complete.', bg='white', font='Times 20').pack()
Text = tkinter.Label(root, text='Bar chart and CSV generated.', bg='white', font='Times 20').pack()
photo = PhotoImage(file='yaya.gif')
Text = Label(root, image=photo).pack()
root.mainloop()
