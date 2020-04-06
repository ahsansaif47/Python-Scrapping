from selenium import webdriver

path = r"C:\Program Files\chromedriver.exe"
browser = webdriver.Chrome(path)

## Mention the sites here..
browser.get('http://onecore.net')
## Mentioning here what to get..(and storing it in allHref Variable)
allHrefs = browser.find_elements_by_xpath('//*[@href]')

## Printing all href's..
for i in allHrefs:
    print(i.get_attribute('href'))