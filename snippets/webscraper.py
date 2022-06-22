""" 
file: webscraper.py
version: 1.0
date: 19-06-2022
author: Vincent Koogje

Tought:
"I copy a lot of information found on webpages of website xyz.com and paste it into an excel file, that I then turn into a CSV. I want to automate this".

Goal:
Proof-of-concept for scraping content of a website, and write it to a CSV file  ----> In this case, we'll fetch financial data from Wall Street Journal (WSJ)

Thought Process::
1) Q: how can we automate the opening of websites in python?
   A: We can write our own code for opening websites, or use the build in 'webbrowers'module. But the module is limiting. Lucily, after some looking
   around, we find a powerfull module for this purpose, called "requests".

2) Q: how do we use the module we've found? 
    A: we can acces a lot of examples online, and consult the module's documentation https://requests.readthedocs.io/en/latest/ 
    or source code: https://github.com/psf/requests. Install? Run: python -m pip install requests 


Before we start: Inspect Your Data Source. Look at the document object model (DOM) of the site. Find the base URL and content/page specific URL's, deceipher parameters and their use. 
Step 1: Open the page trough the URL's we've found
Step 2: Scrape HTML Content From a Page
Step 3: Parse HTML Code into a CSV file




"""

# We'll import some modules
import requests                # importing request library for easy web request manipulation
import re                      # importing regex library to do some regex magic
from bs4 import BeautifulSoup  # importing BeautifulSoup library from BeautifulSoup to scrape sites.
import pandas as pd            # importing panda library for excel/cvs file handeling

"""
try:
    open_url.raise_for_status()
    print(open_url.text)

except Exception as message:
    print('Page returns: %s' % (message))

soup = BeautifulSoup(open_url, 'html.parser')
print(soup.title)
"""


try:
    url_to_scrape="https://www.reuters.com/markets/companies/ASML.AS/"
    open_url = requests.get(url_to_scrape)
except Exception as message:
    print('Page returns: %s' % (message))
soup = BeautifulSoup(open_url.text, 'html.parser')
result = soup.select('span', attrs={"class":"text__black"})
print(result)