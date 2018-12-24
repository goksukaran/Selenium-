'''
Created on 21 Dec 2018

@author: goksukara
'''
global cityname, districts_list

cityname = "Hamburg"
districts_list = []
username="goksukaran@gmail.com"
password="hfXFpRhNZiJza9J"

from Selenium import selenium
from web_scraping import return_wg_list

global temp
temp="https://www.wg-gesucht.de/wohnungen-in-Hamburg.55.2.1.0.html"
def main():
    print("python main function")
    selenium_instance = selenium(cityname,username,password)
    selenium_instance.login()
    selenium_instance.send_city_query()
    print(selenium_instance.browser.current_url)
    wg_list=return_wg_list(temp)
    
    print(len(wg_list))
    for i in wg_list:
        print(i)

if __name__ == '__main__':
    main()

