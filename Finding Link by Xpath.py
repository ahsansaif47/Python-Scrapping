from selenium import webdriver
import time
path = r"C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)

browser.maximize_window()
browser.get('http://google.com')

try:
    ## Checking Link by class name.. 
    browser.find_element_by_xpath("//a[@class='gb_g']")
    print("Test passed : Link test class found by Xpath..")

except Exception as e:
    print('Exception Found', format(e))

time.sleep(5)
browser.close()