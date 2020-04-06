from selenium import webdriver
path = r"C:\Program Files\chromedriver.exe"

browser = webdriver.Chrome(path)
browser.get('http://www.youtube.com')
ids = browser.find_elements_by_xpath('//*[@href]')

for i in ids:
    print(i.get_attribute('href'))