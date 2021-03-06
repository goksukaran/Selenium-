'''
Created on 24 Dec 2018

@author: goksukara
'''
import time
import random
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
from werkzeug.urls import BaseURL
import datetime

global BaseURL_message
BaseURL_message = "https://www.wg-gesucht.de/nachricht-senden.html?message_ad_id="


class selenium():

    def __init__(self, cityname, username, password):
        self.cityname = cityname
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get('https://www.wg-gesucht.de/')
        self.islogined = False
        self.text_messages = open("Text_messages.txt", "r").read().split("<")
        
        
        self.browser.get('https://www.wg-gesucht.de/')
        self.islogined = False
        self.text_messages = open("Text_messages.txt", "r").read().split("<")
        
    def login(self):
        time.sleep(2)
        text_box_username = self.browser.find_element_by_xpath('//*[@id="login_email_username"]')
        text_box_pass = self.browser.find_element_by_xpath('//*[@id="login_password"]')
        submit_button = self.browser.find_element_by_xpath(' //*[@id="login_submit"]')
        login_button = self.browser.find_element_by_xpath('//*[@id="headbar_wrapper"]/div[2]/a[2]').click()
        
        time.sleep(5)
        text_box_username.send_keys(self.username)
        text_box_pass.send_keys(self.password)
        submit_button.click()
        time.sleep(5)
        self.islogined = True
    
    def islogin_succsessful(self):
        pass

    def send_city_query(self):
       text_box = self.browser.find_element_by_xpath('//*[@id="autocompinp"]')
                                                   
       drop_menu = self.browser.find_element_by_xpath('//*[@id="rubrik-dropdown-menu"]').click()
       time.sleep(1) 
       drop_menu = self.browser.find_element_by_xpath('//*[@id="rubrik-dropdown"]/li[1]/a').click()
       
       text_box.send_keys(self.cityname)
       time.sleep(5) 
       submit_button = self.browser.find_element_by_xpath('//*[@id="search_button"]').click()
       
    def send_message(self, element):
        if not(self.islogined):
            self.login() 
        self.browser.get(BaseURL_message + element.id)
        text_box = self.browser.find_element_by_xpath('//*[@id="message_input"]')
        text_box.send_keys(self.text_messages[random.randint(0, 1)])
        print("Message sent")
        element.status = True
        
        return element
        
    def quit(self):
        time.sleep(20)
        self.browser.quit()
        
