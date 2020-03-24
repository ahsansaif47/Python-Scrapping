from selenium import webdriver
import re

chrome_path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.maximize_window()
driver.get('http://www.airindia.in/contact-details.htm')

doc = driver.page_source
phoneNo_3Dig = re.findall(r'[\d]{3}-[\d]{8}', doc)

for phone in phoneNo_3Dig:
    print(phone)