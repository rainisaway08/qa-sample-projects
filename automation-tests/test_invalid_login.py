from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Step 1: Enter valid username
driver.find_element(By.ID, "username").send_keys("student")

# Step 2: Enter invalid password
driver.find_element(By.ID, "password").send_keys("WrongPassword123")

# Step 3: Click login
driver.find_element(By.ID, "submit").click()

# Step 4: Wait for response
time.sleep(2)

# Step 5: Check for error message
error_msg = driver.find_element(By.ID, "error").text

# Step 6: Assert and print result
if "Your password is invalid!" in error_msg:
    print("✅ Invalid login test passed!")
else:
    print("❌ Invalid login test failed!")

# Cleanup
driver.quit()
