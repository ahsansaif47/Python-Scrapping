from selenium import webdriver

chrome_path = r"C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

driver.get("http://en.wikipedia.org")
print(driver.title)

driver.quit()
