'''
Created on 20 Dec 2018

@author: goksukara
'''
import requests
from bs4 import BeautifulSoup
import re


def return_wg_list(search_url):
    page = requests.get(search_url)
    
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')
    
    _mydivs = soup.find_all("a", class_="detailansicht")
    result = []
    for i in _mydivs:
        
        # print(str(i["href"]))
        
        if ("wg-zimmer-in-" in i["href"]):
            result.append(i["href"]) 
    
    result = set(result)
    
    print(len(result))
    for i in result:
        print(i)
    return result

def extract_info(search_url):
    page = requests.get(search_url)
    
    content = page.content
    soup = BeautifulSoup(content, 'html.parser')