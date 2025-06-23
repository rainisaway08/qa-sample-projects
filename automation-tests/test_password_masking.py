from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait for page to load
time.sleep(1)

# Step: Check password input type
password_field = driver.find_element(By.ID, "password")
input_type = password_field.get_attribute("type")

# Assert and print result
if input_type == "password":
    print("✅ Password field is properly masked.")
else:
    print("❌ Password field is NOT masked!")

# Cleanup
driver.quit()
