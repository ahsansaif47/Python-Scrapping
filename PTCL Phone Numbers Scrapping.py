from selenium import webdriver
import re

## The path for chrome path variable is where chrome driver is installed on my pc.
## You would provide path where you have installed your chrome driver.

chrome_path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.maximize_window()
driver.get('https://ptcl.com.pk/Home/PageDetail?ItemId=74&linkId=134')

doc = driver.page_source
phNo = re.findall(r'[\d]{4}', doc)

for p in phNo:
    print(p)
