from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# executable_path depreciated
# chrome_driver_path = "C:\Development\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://takealot.com/12-rules-for-life/PLID55066610")
price = driver.find_element(by=By.CLASS_NAME, value="currency.plus.currency-module_currency_29IIm")

print(price.text)

# driver.close()  # closes tab
driver.quit()   # closes browser