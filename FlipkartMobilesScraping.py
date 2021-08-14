# Importing libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep
# from bs4 import BeautifulSoup
# import requests
# import time
# import random
# import sys
# import pymongo
# import urllib.parse
# import dns
# from mongoengine import *
# from mongoengine.context_managers import switch_collection

print("Scraping Started...")

# Chrome web driver
chrome_options = Options()
chrome_options.add_argument(" — incognito")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument('--disable-dev-shm-usage')

PATH= r"/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(PATH,options=chrome_options)
driver = webdriver.Chrome(options=chrome_options)

# Opening flipkart link
driver.get("https://www.flipkart.com/")

# For selcting outside of login page
driver.execute_script('el = document.elementFromPoint(47, 457); el.click();')

# Empty data list
data = []

# Searching 
searchWord = "Mobiles"
search = driver.find_element_by_xpath("//*[@title='Search for products, brands and more']")
search.send_keys(searchWord)
search.send_keys(Keys.RETURN)

sleep(5)
# All divs
mobileDivs = driver.find_elements_by_xpath("//*[@class='_1YokD2 _3Mn1Gg']")

# Going throw each divs and adding data in data list
for x in mobileDivs[1].find_elements_by_xpath("./div"):
    div = x.find_element_by_xpath("./div")
    try:
        mobileName = div.find_element_by_xpath("./div/div/a/div[2]/div[1]/div[1]").text
        rating = div.find_element_by_xpath("./div/div/a/div[2]/div[1]/div[2]/span[1]").text
        desc = div.find_element_by_xpath("./div/div/a/div[2]/div[1]/div[3]").text
        price1 = div.find_element_by_xpath("./div/div/a/div[2]/div[2]/div[1]/div/div[1]").text
        price2 = div.find_element_by_xpath("./div/div/a/div[2]/div[2]/div[1]/div/div[2]").text
        per = div.find_element_by_xpath("./div/div/a/div[2]/div[2]/div[1]/div/div[3]").text
        elem1 = div.find_elements_by_tag_name("a")
        elem2 = div.find_elements_by_tag_name("img")
        # print(mobileName.text)
        # print("rating : ", rating.text)
        # print("Description : ", desc.text)
        # print("Dicount Price : ", price1.text)
        # print("Actual Price : ", price2.text)
        # print("% Off : ", per.text)
        # print("link : ", elem1[0].get_attribute("href"))
        # print("Img link : ", elem2[0].get_attribute("src"))
        data.append({"Mobile Name": mobileName, "Rating": rating, "Short Description": desc, "Dicount Price": price1, "Actual Price": price2, "% Off": per, "Link": elem1[0].get_attribute("href"), "Img link": elem2[0].get_attribute("src")})
        print("Data adding in list...")
    except:
        pass

# Adding data in CSV File
dataset = pd.DataFrame(data, columns=['Mobile Name','Rating','Short Description', 'Dicount Price', 'Actual Price', '% Off', 'Link', 'Img link'])
dataset.to_csv('details.csv')
print("==========================")
print("Data added in CSV File...")
print("==========================")
print("Scraping Stopped...")

# Closing driver
driver.close()
