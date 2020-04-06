from selenium import webdriver
import logging
import time
path = r"C:\Program Files\chromedriver.exe"

log_FILENAME = 'example.log'
logging.basicConfig(filename=log_FILENAME, level=logging.DEBUG)
driver = webdriver.Chrome(path)
logging.debug('Chrome Instance Started')
print(driver.capabilities['browserVersion'])
logging.debug('Browser Version Printed')
time.sleep(5)
driver.close()