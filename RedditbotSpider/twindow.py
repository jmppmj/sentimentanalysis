import tkinter
from tkinter import *

#creates tkinter window

class statusWindow(Frame):
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Sentiment Analysis")
        self.master.configure(background="white")
