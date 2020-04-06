from selenium import webdriver
path = r"C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('https://www.shutterstock.com/?kw=sites%20for%20images&gclid=CjwKCAjwpqv0BRABEiwA-TySwexURq61k7CeCftUoQ-gG9rF_-BalmyyRL4iKyJjda75Qm4tKWK95BoCBUAQAvD_BwE&gclsrc=aw.ds')
elem = driver.find_element_by_class_name('oc_w_p')
print(elem.size)
