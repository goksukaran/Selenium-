'''
Created on 21 Dec 2018

@author: goksukara
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://stackoverflow.com/")

body = driver.find_element_by_tag_name("body")
body.send_keys(Keys.CONTROL + 't')

driver.close()