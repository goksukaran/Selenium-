'''
Created on 20 Dec 2018

@author: goksukara
'''
import requests
from bs4 import BeautifulSoup
import re

class datacontrainer():
    def __init__(self, name, id):
        self.name=name
        self.id=id

def return_wg_list(search_url):
    page = requests.get(search_url)
    
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    
    _mydivs = soup.find_all("a", class_="detailansicht")
    result= []
    
    for i in _mydivs:
        
        # print(str(i["href"]))
        
        if ("wg-zimmer-in-" in i["href"]):
            
            _temp=i["href"].split(".")
            for j in _temp:
                if(j.isnumeric()):
                    result.append(datacontrainer(i["href"],j))
             
    
    result = set(result)
    
    print(len(result))
    for i in result:
        print(i)
    return result

def extract_info(search_url):
    page = requests.get(search_url)
    
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')