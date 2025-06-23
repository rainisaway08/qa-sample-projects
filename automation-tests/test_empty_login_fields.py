from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait for page to load
time.sleep(1)

# Click the login button without entering credentials
driver.find_element(By.ID, "submit").click()

# Wait for error to appear
time.sleep(2)

# Check if error message is shown
error_msg = driver.find_element(By.ID, "error").text

if "Your username is invalid!" in error_msg:
    print("✅ Empty fields login test passed!")
else:
    print("❌ Empty fields login test failed!")

# Cleanup
driver.quit()
