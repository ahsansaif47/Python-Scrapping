from selenium import webdriver
path = r"C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)

browser.get('http://www.bing.com')
# Printing the current cookies..
print(browser.get_cookies())

# Adding new Cookies..
Cookie={'fruit' : 'mango', 'chocolate' :'dairy'}
browser.add_cookie(Cookie)
print("Cookie Added..")