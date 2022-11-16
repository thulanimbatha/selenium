from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

count_anchor = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(count_anchor.text)

driver.quit()