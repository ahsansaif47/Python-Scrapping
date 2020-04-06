from selenium import webdriver
chrome_pth = r"C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(chrome_pth)
driver.get('https://www.google.com/')

try:
    ## Original Gmail Styling ID
    driver.find_element_by_id('gbw')

    ## Random ID Test
    ##driver.find_element_by_id('abc')
    print("Test Pass : ID Found")

except Exception as e:
    print("Excaption Found", format(e))

driver.close()