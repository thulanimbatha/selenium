from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
# find element
count_anchor = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# click on element
count_anchor.click()
driver.quit()