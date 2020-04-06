from selenium import webdriver
import time
path = r"C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)

browser.maximize_window()
browser.get('http://www.google.com')

browser.find_element_by_link_text('Gmail').click()
time.sleep(5)
browser.close()