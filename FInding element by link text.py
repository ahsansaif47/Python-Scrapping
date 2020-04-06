from selenium import webdriver
import time
path = r"C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)
browser.get('http://google.com')

try:
    browser.find_element_by_link_text('Gmail')
    print("Test Passed..")

except Exception as e:
    print('Exception FOund', format(e))

time.sleep(6)
browser.close()