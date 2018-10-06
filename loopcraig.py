#!/usr/bin/python
# -*- coding: utf-8 -*-

from getcraig import Getcraig
import requests
from bs4 import BeautifulSoup
import csv
import os.path


def exportCSV(obj):
    header = False
    my_file = 'craigs.csv'
    if not(os.path.isfile(my_file)):
        header = True
    my_dict = obj.__dict__
    with open(my_file, 'a') as f:
        w = csv.DictWriter(f, my_dict.keys())
        if header == True:
            w.writeheader()

        w.writerow(my_dict)


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
    u = urlCollection[i].attrs['href']
    # print u
    adCollection[i] = Getcraig(u)
    print (adCollection[i])
    exportCSV(adCollection[i])
