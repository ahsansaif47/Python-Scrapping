from selenium import webdriver
import logging
path = r"C:\Program Files\chromedriver.exe"
log_FIle = open("D:\Python - WebScrapping\Log Files\FacebookLog.LOG", "w")

driver = webdriver.Chrome(path)