from selenium import webdriver
path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://toronto.craigslist.ca")
driver.find_element_by_xpath("""/html/body/div/section/div/ul/li[47]/a/b""").click()
driver.find_element_by_xpath("""//*[@id="sss0"]/li[5]/a""").click()
posts = driver.find_elements_by_class_name("hdrlnk")

print(len(posts))

for p in posts:
    print(p.text)
