'''
Created on 21 Dec 2018

@author: goksukara
'''
global cityname, districts_list

cityname = "Hamburg"
districts_list = []

from Selenium import selenium


def main():
    print("python main function")
    selenium_instance = selenium(cityname, districts_list)
    selenium_instance.login()

if __name__ == '__main__':
    main()

