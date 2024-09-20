from DrissionPage import ChromiumPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Set up the WebDriver with the path to your chromedriver
service = Service("C:/Drivers/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.beyoung.in/")

time.sleep(2)

driver.maximize_window()

counter = driver.find_elements(By.CLASS_NAME, 'menu-top')

print(len(counter))

links = driver.find_elements(By.TAG_NAME, "a")

print(len(links))

# driver.find_element(By.LINK_TEXT, "WOMEN").click()

time.sleep(3)



driver.quit()