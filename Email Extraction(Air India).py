from selenium import webdriver
import re

## The path for chrome path variable is where chrome driver is installed on my pc.
## You would provide path where you have installed your chrome driver.

chrome_path = r"C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.get('http://www.airindia.in/contact-details.htm')
driver.maximize_window()

doc = driver.page_source
emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

for email in emails:
    print(email)
