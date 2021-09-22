##################################################
#                                                #
#          Services NSW auto check in            #
#                                                #
#       Hacked together by BoredManPlays         #
#                                                #
##################################################

import os
import sys
from decouple import config
from selenium import webdriver
import time

try:
    #read values from .env, the URL __MUST__ be the business check-in form not the QR code form
    URL = config("URL")
    FIRST = config("FIRST")
    LAST = config("LAST")
    NUMBER = config("NUMBER")
    #obviously change this to wherever your webdriver is located
    driver_path = 'C:/users/null/pycharmprojects/WorkCheckIn/chromedriver'
    driver = webdriver.Chrome(driver_path)
    #go to the site
    driver.get(URL)
    #firstname junk
    firstName_xpath = '/html/body/div[2]/div/main/div/div[2]/form/div[2]/div[1]/div[1]/input'
    firstName_area = driver.find_element_by_xpath(firstName_xpath)
    firstName_area.clear()
    firstName_area.send_keys(FIRST)
    #lastname junk
    lastName_xpath = '/html/body/div[2]/div/main/div/div[2]/form/div[2]/div[1]/div[2]/input'
    lastName_area = driver.find_element_by_xpath(lastName_xpath)
    lastName_area.clear()
    lastName_area.send_keys(LAST)
    #phone number junk
    number_xpath = '/html/body/div[2]/div/main/div/div[2]/form/div[2]/div[1]/div[3]/input'
    number_area = driver.find_element_by_xpath(number_xpath)
    number_area.clear()
    number_area.send_keys(NUMBER)
    #press the submit button
    submit_xpath = '/html/body/div[2]/div/main/div/div[2]/form/div[5]/button'
    submit_area = driver.find_element_by_xpath(submit_xpath)
    submit_area.click()
    #wait for the approved screen
    time.sleep(2)
    #grab the business name
    business_xpath = '/html/body/div[2]/div/main/div/div[2]/div[3]/div[1]/div[2]/span'
    business_area = driver.find_element_by_xpath(business_xpath)
    business_name = str(business_area.text).title()
    driver.quit()
    msg = "msg * Successfully checked in at " + business_name
    os.system(msg)
except:
    raise os.system("msg * Something went wrong")
