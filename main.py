from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# executable_path depreciated
# chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# by Class Name
# driver.get("https://takealot.com/12-rules-for-life/PLID55066610")
# price = driver.find_element(by=By.CLASS_NAME, value="currency.plus.currency-module_currency_29IIm")

# print(price.text)

driver.get("https://python.org")
# by Name
# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.get_attribute("placeholder")) 

# by CSS selector
# docs_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a") # anchor tag inside doc-widget class
# print(docs_link.text) 

# by Xpath
# link = driver.find_element(by=By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/p[2]/a')
# print(link.text)

# find upcoming events and store them into a dictionary
event_times = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget a")

for name in event_names:
    print(name.text)


    

# driver.close()  # closes tab
driver.quit()   # closes browser