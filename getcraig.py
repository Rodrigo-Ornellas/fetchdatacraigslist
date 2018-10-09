#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
from bs4 import BeautifulSoup
import requests
import csv
import sys
import json

class Getcraig:
    '''
    ==========================================
    >> Getcraig >
        ** is a script that takes an URL from Craigslist as a unique parameter:
        -------------------
        1) To get the URL, visit the HOUSING section of Craigslist.
        2) Please define the search parameter on Craigslist's page.
        This search should display the list of ads of apartments available for rent.
        3) Once the list is presented, you can COPY the url as INPUT for Getcraig SCRIPT!
    '''

    # num_of_ads = 0


    def __repr__(self):
        return "AdUrl('{}')".format(self.url)


    def __str__(self):
        return '============ Ad #{} ============== \n1) Move-in date: {} \n2) Details: {} \n3) Apartment size: {} \n4) Price: {} \n5) Google Maps: {} \n6) Ad URL: {} \n7) Title: {} \n8) Lat & Long: {}'.format(self.pid, self.avdate, str(self.details), self.__aptsize(), str(self.price), str(self.mapurl), self.url, str(self.title), self.__geometry())


    def exportCSV(self):
        ''' This will export this unique rental AD information to a CSV file called craig.csv'''
        my_dict = self.__dict__
        with open('craigs.csv', 'w') as f:
            w = csv.DictWriter(f, my_dict.keys())
            w.writeheader()
            w.writerow(my_dict)

    def exportJSON(self):
        ''' This will export this unique rental AD information to a JSON variable'''
        my_dict = self.__dict__
        return json.dumps(my_dict)


    def __geometry(self):
        ''' This returns one text string with Latitude and Longitude'''
        # to call this method there are 2 forms
        # a) instance-name.geometry()  >> access the method through instance
        # b) GetAd.geomentry(instance-name)  >> or access the method through class
        return '{},{}'.format(self.lat, self.lng)

    def __aptsize(self):
        ''' This gets the apartment size in square feet and translate to squared meter if exists'''
        dim = self.details.split('/')
        for i in dim:
            try:
                size = int(i)
                if (size > 100):
                    self.size = str("{0:.2f}".format(int(i) * 0.092903)) + " m2"
                    # print("{0:.2f}".format(a))
                    return self.size
                else:
                    self.size = 0
                    return self.size
            except:
                pass



    def __init__(self, url):
            self.url = url
            self.avdate = ""     #1
            self.details = ""    #2
            self.pid = ""        #3
            self.price = ""      #4
            self.mapurl = ""     #5
            self.housing = ""    #6
            self.title = ""      #7
            self.lat = ""        #8
            self.lng = ""        #8
            # Getcraig.num_of_ads += 1

            # =============================================
            # V) Validate the URL as being part of Craigslist
            valid = 0
            valid = self.url.find(".craigslist.")
            # print (valid)
            if valid == -1:
                sys.exit("Sorry! URL is not from a valid Rental Advertizement Page. Please start again!")


            # =============================================
            # R) Request the URL after validation
            secpage = requests.get(self.url)
            dish = BeautifulSoup(secpage.content, 'html.parser')

            # =============================================
            # 3) var pID  or  <p class="postinginfo">post id:
            try:
                # scrap = dish.find("p", {"class": "postinginfo"}).contents
                self.pid = self.url.split('/')[-1].split('.')[0]
                # self.pid = scrap[0]
                # for z in scrap:
                #     print (z)
            except:
                # sys.exit("Sorry! URL is not from a valid Rental Advertizement Page. Please start again!")
                # print ("3) did not work: PID")
                # sys.exit("Sorry! URL is not from a valid Rental Advertizement Page. Please start again!")
                pass

            # =============================================
            # 1) Avilability Date > data-date="2018-10-01"
            try:
                self.avdate = dish.find("span", {"class": "housing_movein_now property_date shared-line-bubble", "data-date": True})["data-date"]
            except:
                # print ("1) did not work: DATE")
                pass
            # =============================================
            # 2) Details of Unit = class="attrgroup"
            # try:
            # scrap = dish.findAll("span", {"class": "shared-line-bubble"})
            scrap = 0
            try:
                scrap = dish.find("p", {"class": "attrgroup"}).select("span b")
                det = ""
                for i in range(len(scrap)):
                    det = str(scrap[i].contents[0]) + " / " + str(det)

                self.details = det

            except:
                # print ("2) did not work: DETAILS")
                pass


            # =============================================
            # 4) Price = class="price"
            scrap = 0
            try:
                scrap = dish.find("span", {"class": "price"}).contents
                for price in scrap:
                    self.price = price
            except:
                # print ("4) did not work: PRICE")
                pass

            # =============================================
            # 5) Google Maps Link = class="mapaddress"
            try:
                self.mapurl = dish.find("p", {"class": "mapaddress"}).find('a')['href']
            except:
                # print ("5) did not work: MAPS")
                pass

            # =============================================
            # 6) House details = class="housing"
            # scrap = 0
            # try:
            #     scrap = dish.find("span", {"class": "housing"}).contents
            #     for housing in scrap:
            #         self.housing = housing
            # except:
            #     print ("6) did not work: HOUSE")
            #     pass

            # =============================================
            # 7) House details = SPAN / id="titletextonly"
            scrap = 0
            try:
                scrap = dish.find("span", {"id": "titletextonly"}).contents
                for title in scrap:
                    self.title = title
            except:
                pass

            # =============================================
            # 8) Lat & lng = class="viewposting leaflet-container leaflet-touch leaflet-retina leaflet-fade-anim leaflet-grab leaflet-touch-drag leaflet-touch-zoom"
            scrap = 0
            try:
                self.lat = dish.find("div", {"id": "map"})["data-latitude"]
                self.lng = dish.find("div", {"id": "map"})["data-longitude"]
            except:
                pass

            # =============================================
