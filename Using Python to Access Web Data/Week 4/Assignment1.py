'''In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor
tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link 
and repeat the process a number of times and report the last name you find.
Problem :-
Start at: http://py4e-data.dr-chuck.net/known_by_Amaan.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: T
Strategy
The web pages tweak the height between the links and hide the page after a few seconds to make it difficult for you to 
do the assignment without writing a Python program. But frankly with a little effort and patience you can overcome these
attempts to make it a little harder to complete the assignment without writing a Python program. But that is not the point.
The point is to write a clever Python program to solve the program.'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('ENTER URL: ')
link_line = int(input("ENTER POSITION: ")) - 1
count = int(input("ENTER COUNT: "))

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

while count >= 0:
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, 'html.parser')
   tags = soup('a')
   print('Retrieving: ',url)
   url = tags[link_line].get("href", None)
   count = count - 1
