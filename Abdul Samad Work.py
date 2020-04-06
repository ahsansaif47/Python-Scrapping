from selenium import webdriver
chrome_path = r"C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.maximize_window()
driver.get("https://olist.ng/")
driver.find_element_by_xpath("""//*[@id="app"]/div/section[2]/article[1]/div/div[1]/div[2]/p[1]/a""").click()

posts = driver.find_elements_by_class_name("item")

print(len(posts))
print(type(posts))
print(posts)

for p in posts:
    print(p.text)
