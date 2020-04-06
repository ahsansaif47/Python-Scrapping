from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/')

## Locating Element to Double Click..
elem = driver.find_element_by_name('permission')

actionchains = ActionChains(driver)
actionchains.double_click(elem).perform()
time.sleep(5)
driver.close()