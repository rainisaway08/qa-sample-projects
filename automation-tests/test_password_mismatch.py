from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://example.com/registration")  # 🔁 Replace with actual form URL

# Fill in required fields
driver.find_element(By.ID, "username").send_keys("rain123")
driver.find_element(By.ID, "email").send_keys("rain@example.com")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "confirmPassword").send_keys("Password321")

# Submit the form
driver.find_element(By.ID, "submit").click()
time.sleep(2)

# Check for mismatch error
error_msg = driver.find_element(By.ID, "error").text  # 🔁 Adjust as needed

if "Passwords do not match" in error_msg:
    print("✅ Password mismatch test passed!")
else:
    print("❌ Password mismatch test failed!")

# Cleanup
driver.quit()
