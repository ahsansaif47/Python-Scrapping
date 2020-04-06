from selenium import webdriver
import time
path = r"C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.maximize_window()
browser.get('http://www.google.com')

## @class Gets the classes and we are storing them in classe variable..
classes = browser.find_elements_by_xpath('//*[@class]')

## Getting a specific attribute of class from the fetched result..
for i in classes:
    print(i.get_attribute('class'))

time.sleep(15)
browser.close()