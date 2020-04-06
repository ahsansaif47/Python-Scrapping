from selenium import webdriver
import time
path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('http://www.youtube.com')
element = driver.find_element_by_id('logo-icon-container')
time.sleep(3)
print("Display Status: ",element.is_displayed())
time.sleep(5)
driver.close()