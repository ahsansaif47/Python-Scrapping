from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('http://www.google.com')
nTab = driver.find_element_by_tag_name('body')
time.sleep(5)
driver.execute_script("window.open('body', 'new window')")
time.sleep(5)
nTab.send_keys(Keys.CONTROL+'w')