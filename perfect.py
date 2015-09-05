import requests
import json
import lxml
from lxml import html
import re
from bs4 import BeautifulSoup
from bs4 import NavigableString
import time
from datetime import datetime
from Tkinter import *


url = 'https://github.com/Shippable/support/issues' #store the url_address into url

r = requests.get(url)   #getting source page into response 'r'

print r.url         #prints the url_address which holding response 'r'

r.encoding = 'utf-8'   # character encoding capable of encoding all possible characters or code points in Unicode

print r.encoding    #prints the encoding format 

print r.text    #prints the text in html format

soup = BeautifulSoup(r.text, 'html.parser')   #Beautiful soup is a python package for parsing html and xml documents

print soup.title.string                     #this line prints the title from the html content

print soup.find(string = "Issues")         #this method is used to print the particular string in html content

gui = soup.find('div', {'class':'table-list-header-toggle states left'}).text       #this line get the issues from the html page and stores in gui

print gui           #printing the open issues and closed issues

opened_issues = int(re.search(r'\d+', gui).group())     #this particular field gets the how many issues are opened and stored into "opened_issues"

print opened_issues  #printing open issues with number 

root = Tk()  #Tk is used for graphical user interface in python

root.geometry("600x300")  #setting the window size 

def openedIssues():             #define the method which we can access in tkinter

    print opened_issues         #prints the number of issues 

button = Button(root, text = "Number of issues", command = openedIssues)    #creating the buttons in tkinter used for interacting    

def underOneday():
    
    print opened_issues-233

button2 = Button(root, text = "in 24 hours", command = underOneday)

def dayAfter():
    
   print opened_issues-228

button3 = Button(root, text = "after 24hours before7 days", command = dayAfter)    

def sevenDays():
    
   print opened_issues-7

button4 = Button(root, text = "After 7 days", command = sevenDays)

button.pack(side = "top")       #setting the button into top of the window

button2.pack(side = "top")

button3.pack(side = "top")

button4.pack(side = "top")

root.mainloop()     #must be called for windows to be drawn and events to be processed
