from selenium import webdriver

chrome_path = r"C:\Program Files\chromedriver.exe"

driver = webdriver.Chrome(chrome_path)
driver.get("https://www.daraz.pk/smartphones/infinix/?spm=a2a0e.home.cate_1_1.8.35e34937skaCDn")

driver.find_element_by_xpath("""//*[@id="J_5022174600"]/div/ul/ul[1]/li[1]/ul/li[8]/a""").click()

posts = driver.find_elements_by_xpath("""//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/a""")

print(len(posts))

for p in posts:
    print(p.text)
