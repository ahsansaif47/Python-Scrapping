from selenium import webdriver
import time
path = r"C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)

browser.maximize_window()
browser.get('http://www.wikipedia.org')
try:
    browser.find_element_by_partial_link_text('Terms')
    print("Test passed..")

except Exception as e:
    print('Exception Found', format(e))

time.sleep(5)
browser.close()