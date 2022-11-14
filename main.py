from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://takealot.com/12-rules-for-life/PLID55066610")

# driver.close()  # closes tab
driver.quit()   # closes browser