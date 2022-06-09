from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import datetime as dt
import pandas as pd

listeds=[]


url = "https://www.goatbots.com"

option = Options()
option.headless = False
driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

action = webdriver.ActionChains(driver)
search_bar = WebDriverWait(driver,
                           20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cardname-input"]')))
search_bar.send_keys('Dust to Dust')

time.sleep(1)

search_button = WebDriverWait(driver,
                              20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cardname-results"]')))
search_button.click()

search_button2 = WebDriverWait(driver,
                              20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/main/ul/li[2]')))
search_button2.click()

#//*[@id="price-1"]

driver.execute_script('window.scrollTo(0, 250)')

element = WebDriverWait(driver,
                              20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="card-graph-wrap"]')))
loc = element.location
size = element.size

action.move_to_element_with_offset(element, 500, 100).perform()


print(loc)
print(size)