'''
Created on 21 Dec 2018

@author: goksukara
'''
global cityname, districts_list

cityname = "Rostock"
districts_list = []
username = "goksukaran@gmail.com"
password = "hfXFpRhNZiJza9J"

from Selenium import selenium
from Database import database
from web_scraping import return_wg_list, extract_info, datacontrainer
import time, threading

global temp
temp = "https://www.wg-gesucht.de/wg-zimmer-in-Hamburg-Winterhude.4656678.html"


def Routine(selenium_instance, database_instance):
    wg_list = return_wg_list(selenium_instance.browser.current_url)

    for element in wg_list:
        print(element.name)
        print(element.id)
        print(database_instance.is_primarykey_exsist("applied_offers", element.id))
        if not(database_instance.is_primarykey_exsist("applied_offers", element.id)):
            element = extract_info(element)
            selenium_instance.send_message(element)
            df = database_instance.convert_data_frame(element)
            database_instance.insert_data(df)


def main():
    print("python main function")
    
    selenium_instance = selenium(cityname, username, password)
    database_instance = database()
    database_instance.connectdatabase()
    # selenium_instance.login()
    selenium_instance.send_city_query()

    print(selenium_instance.browser.current_url)

    Routine(selenium_instance, database_instance)
            
    #===========================================================================
    # element=datacontrainer("wg-zimmer-in-Rostock-Kroepeliner-Tor-Vorstadt.7065056.html","7065056")
    # print(type(element))
    # element = extract_info(element)
    # element=selenium_instance.send_message(element)
    # df = database_instance.convert_data_frame(element)
    # print(df)
    # database_instance.insert_data(df)
    # selenium_instance.send_message()
    #===========================================================================
    threading.Timer(300, main).start()
    selenium_instance.quit()


if __name__ == '__main__':
    
    main()

