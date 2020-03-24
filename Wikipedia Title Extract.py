from selenium import webdriver

## The path for chrome path variable is where chrome driver is installed on my pc.
## You would provide path where you have installed your chrome driver.

chrome_path = r"C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)

driver.get("http://en.wikipedia.org")
print(driver.title)

driver.quit()
