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


class selenium():

    def __init__(self, cityname, districts_list):
        self.cityname = cityname
        self.disrits = districts_list
        
    def login(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('http://www.google.com')
        
        search = browser.find_element_by_name('q')
        search.send_keys("google search through python")
        search.send_keys(Keys.RETURN)  # hit return after you enter search text
        time.sleep(5)  # sleep for 5 seconds so you can see the results
        browser.quit()
    
    def islogin_succsessful(self):
        pass

    def send_city_quarry(self):
        pass

    def send_message(self):
        pass
