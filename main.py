##################################################
#                                                #
#          Services NSW auto check in            #
#                                                #
#       Hacked together by BoredManPlays         #
#                                                #
##################################################

from decouple import config
from selenium import webdriver
import time


URL = config("URL")
FIRST = config("FIRST")
LAST = config("LAST")
NUMBER = config("NUMBER")

driver_path = 'C:/users/null/pycharmprojects/WorkCheckIn/chromedriver'
driver = webdriver.Chrome(driver_path)
driver.get(URL)

firstName_xpath = '/html/body/div[2]/div/main/div/div[2]/form/div[2]/div[1]/div[1]/input'
firstName_area = driver.find_element_by_xpath(firstName_xpath)
firstName_area.clear()
firstName_area.send_keys(FIRST)
lastName_xpath = '/html/body/div[2]/div/main/div/div[2]/form/div[2]/div[1]/div[2]/input'
lastName_area = driver.find_element_by_xpath(lastName_xpath)
lastName_area.clear()
lastName_area.send_keys(LAST)
number_xpath = '/html/body/div[2]/div/main/div/div[2]/form/div[2]/div[1]/div[3]/input'
number_area = driver.find_element_by_xpath(number_xpath)
number_area.clear()
number_area.send_keys(NUMBER)
submit_xpath = '/html/body/div[2]/div/main/div/div[2]/form/div[5]/button'
submit_area = driver.find_element_by_xpath(submit_xpath)
submit_area.click()
time.sleep(2)
driver.quit()
