#!/usr/bin/python
# -*- coding: utf-8 -*-

from craigsad import GetAd
import requests
from bs4 import BeautifulSoup

urlCollection = ["https://vancouver.craigslist.ca/bnc/apa/d/1-bedroom-apartment-unit-near/6713471145.html",
"https://vancouver.craigslist.ca/bnc/apa/d/one-bedroom-suite-in-great/6712807053.html",
"https://vancouver.craigslist.ca/bnc/apa/d/1bd-subground-suite/6711483086.html",
"https://vancouver.craigslist.ca/bnc/apa/d/1bed1bath-semi-basement-close/6698060228.html",
"https://vancouver.craigslist.ca/bnc/apa/d/large-1-bedroom-suite/6710742618.html",
"https://vancouver.craigslist.ca/van/apa/d/750-private-room-in-shared/6710601213.html",
"https://vancouver.craigslist.ca/bnc/apa/d/1-unfurnished-bedroom-in-2/6710299590.html",
"https://vancouver.craigslist.ca/bnc/apa/d/single-bedroom-on-15th-floor/6709051892.html"]

# t = GetAd(urlCollection[0])
# print (t)

# ===========================================
# from pygeocoder import Geocoder
# import pandas as pd
# import numpy as np

# import geopy

data = {
'Site 1': "49.227957,-122.995090",
'Site 2': "49.213876,-122.980245",
'Site 3': "49.229810,-122.989195",
'Site 4': "49.223133,-123.001538",
'Site 5': "49.236991,-123.001079",
'Site 6': "49.227393,-122.966117",
'Site 7': "49.223208,-123.003695"
}

lat = "49.227957"
lng = "-122.995090"

results = GoogleV3().reverse(lat,lng)
# results = Geocoder.reverse_geocode(df['latitude'][0], df['longitude'][0]
