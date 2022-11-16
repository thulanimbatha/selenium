from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url="http://secure-retreat-92358.herokuapp.com/")    # get url

# find the first name input bar
fName = driver.find_element(by=By.NAME, value="fName")
fName.send_keys("Thulani")  # add input
fName.send_keys(Keys.ENTER) # press enter

# find the last name input bar, add input, press enter
lName = driver.find_element(by=By.NAME, value="lName")
lName.send_keys("Mbatha")
fName.send_keys(Keys.ENTER) 

# find the email input bar, add input, press enter
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("something@gmail.com")
fName.send_keys(Keys.ENTER) 

# find "sign up" button, click button
button = driver.find_element(by=By.NAME, value="btn-primary")
button.click()


