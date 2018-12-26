'''
Created on 20 Dec 2018

@author: goksukara
'''
import requests
from bs4 import BeautifulSoup
import re
import datetime


class datacontrainer():
    def __init__(self, name, id):
        self.name=name
        self.id=id
        self.date=0
        self.time=0
        self.online_time=0
        self.status=False
        

def return_wg_list(search_url):
    print("return_wg_list")
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
    
  
    return result

def extract_info(element):
    page = requests.get("https://www.wg-gesucht.de/"+element.name)
    
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    element.date = datetime.date.today()
    
    
    return element