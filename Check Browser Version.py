from selenium import webdriver
import time
path = r"C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get('http://bing.com')
print(browser.capabilities['browserVersion'])
time.sleep(5)
browser.close(5)