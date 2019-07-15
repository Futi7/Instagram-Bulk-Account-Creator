#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:07:35 2019

@author: d7v7loper
"""

import bs4
import urllib.request
from bs4 import BeautifulSoup as soup
from pymongo import MongoClient
import names
import random

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"
opener = AppURLopener()

client = MongoClient('mongodb://localhost:27017')
database = client['IG-database']
users = database.users


class pushDB:
    def __init__(self, count, opener, table): 
        for i in range(count):
            self.getMail(opener)
            self.getOtherInfos()
            self.pushInfo(table)   
        print('Succesful!')

    def getMail(self, opener):
        response = opener.open('https://temp-mail.org/en/')     
        page_soup = soup(response, "html.parser")
        input = page_soup.find("input",{"id":"mail"}).get('value')
        self.email = input

    def getOtherInfos(self):
       self.fullname = names.get_full_name()
       self.username = 'waxahatchee' + str(random.randint(10, 21))
       self.password = 'nebukadnezzar'
       
    def pushInfo(self, table):
         user = {
                'email'    : self.username + '@mail.com',
                'fullname' : self.fullname,
                'username' : self.username,
                'password' : self.password,
                'usable'   : 1
                }
         table.insert_one(user)

count = input('Enter the count of user infos:\n')
push = pushDB(int(count), opener, users)



