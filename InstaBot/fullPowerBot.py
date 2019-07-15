#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:47:30 2019

@author: d7v7loper
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymongo
import random

client = MongoClient()
client = MongoClient('mongodb://localhost:27017')
database = client['IG-database']
users = database.users

class InstagramBot:
    def __init__(self,users): 
       self.users = users
       self.informations()
       self.driver = webdriver.Firefox()
       self.signUp()
       time.sleep(25)
       self.closeBrowser()
       
    def closeBrowser(self):
        self.driver.close()
        
        
        
    def informations(self):
        infos = self.users.find_one({"usable": 1})   
        self.email = infos['email']
        self.fullname = infos['fullname']
        self.username = infos['username']
        self.password = infos['password']
        infos['usable'] = 0
        self.users.update_one({'_id':infos['_id']}, {"$set": infos}, upsert=False)
        
        
        
        
    def signUp(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(8)
        
        
        email_elem = driver.find_element_by_xpath("//input[@name='emailOrPhone']")
        email_elem.clear()
        email_elem.send_keys(self.email)
        
        fullname_elem = driver.find_element_by_xpath("//input[@name='fullName']")
        fullname_elem.clear()
        fullname_elem.send_keys(self.password)
        
        username_elem = driver.find_element_by_xpath("//input[@name='username']")
        username_elem.clear()
        username_elem.send_keys(self.username)
        
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        
        password_elem.send_keys(Keys.RETURN)
        time.sleep(8)
        

botIG = InstagramBot(users)
