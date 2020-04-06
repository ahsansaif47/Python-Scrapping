from selenium import webdriver
path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://toronto.craigslist.org")
driver.find_element_by_xpath("""//*[@id="sss0"]/li[5]/a""")
posts = driver.find_elements_by_xpath("""//*[@id="sortable-results"]/ul/li[1]/p/a""")


for p in posts:
    print(p.text)