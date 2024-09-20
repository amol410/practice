from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Service object with the path to chromedriver
service = Service("C:\Drivers\chromedriver.exe")

# Create a new Chrome driver instance
driver = webdriver.Chrome(service=service)

time.sleep(5)

driver.get("https://opensource-demo.orangehrmlive.com/")

time.sleep(5)


driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")

time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(5)
# # Your code to interact with the browser goes here

# act_title = driver.title
# exp_title = "OrangeHRM"

# if act_title == exp_title:
#     print("Login Test Pass")
# else:
#     print("Login Test Failed ")    
# time.sleep(5)
# # Don't forget to close the browser when you're done
# driver.quit()

