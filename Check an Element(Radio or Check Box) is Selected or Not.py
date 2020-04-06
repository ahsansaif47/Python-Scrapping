from selenium import webdriver
import time
path = r"C:\Program Files\chromedriver.exe"
bInst = webdriver.Chrome(path)

bInst.get('https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/')
elem = bInst.find_element_by_name('permission')
time.sleep(3)
print("Selected Status : ", elem.is_selected())
time.sleep(3)

# Clicking on Particular Element
elem.click()
print("Selected Status : ", elem.is_selected())