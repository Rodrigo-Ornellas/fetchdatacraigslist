#!/usr/bin/python
# -*- coding: utf-8 -*-

from craigscrap import Getcraig
import requests
from bs4 import BeautifulSoup

mainurl = "https://vancouver.craigslist.ca/search/apa?query=burnaby+metrotown&hasPic=1&search_distance=3&postal=v5h1t7&max_price=1200&max_bedrooms=2&availabilityMode=0&sale_date=all+dates"
page = requests.get(mainurl)

# print the response of the HTTP GET
# print (page.status_code)

# print the HTML content of the page
# print (page.content)
soup = BeautifulSoup(page.content, 'html.parser')

urlCollection = soup.findAll("a", {"class": "result-title hdrlnk"})
adCollection = range(len(urlCollection))
# print (len(urlCollection))

for i in range(len(urlCollection)):
    # print i
    u = urlCollection[i].attrs['href']
    # print u
    # print (urlCollection[i].attrs['href'])
    adCollection[i] = u
    # print (adCollection)
    adCollection[i] = Getcraig(u)
    print (adCollection[i])
