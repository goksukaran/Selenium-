'''
Created on 24 Dec 2018

@author: goksukara
'''
import time
import os 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from werkzeug.urls import BaseURL

global BaseURL
BaseURL = "https://www.wg-gesucht.de/"


class selenium():

    def __init__(self, cityname, username, password):
        self.cityname = cityname
        self.username = username
        self.password = password
        self.browser = 0
        
    def login(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.browser.get('https://www.wg-gesucht.de/')
        
        text_box_username = self.browser.find_element_by_xpath('//*[@id="login_email_username"]')
        text_box_pass = self.browser.find_element_by_xpath('//*[@id="login_password"]')
        submit_button = self.browser.find_element_by_xpath(' //*[@id="login_submit"]')
        login_button = self.browser.find_element_by_xpath('//*[@id="headbar_wrapper"]/div[2]/a[2]').click()
        time.sleep(2)
        
        text_box_username.send_keys(self.username)
        text_box_pass.send_keys(self.password)
        submit_button.click()
        time.sleep(2)
    
    def islogin_succsessful(self):
        pass

    def send_city_query(self):
       text_box = self.browser.find_element_by_xpath('//*[@id="autocompinp"]')
                                                   
       drop_menu = self.browser.find_element_by_xpath('//*[@id="rubrik-dropdown-menu"]').click()
       time.sleep(2) 
       drop_menu = self.browser.find_element_by_xpath('//*[@id="rubrik-dropdown"]/li[1]/a').click()
       
       text_box.send_keys(self.cityname)
       time.sleep(2) 
       
       time.sleep(2)
       submit_button = self.browser.find_element_by_xpath('//*[@id="search_button"]').click()

    def send_message(self, adress):
        time.sleep(2) 
        self.browser.get(adress)
        submit_button = self.browser.find_element_by_xpath('//*[@id="rhs_column"]/div[4]/div[2]/div/div[13]/a').click()
        text_box = self.browser.find_element_by_xpath('//*[@id="message_input"]')
        text_box.send_keys("Hi")
    
        
    def quit(self):
        self.browser.quit()
        
