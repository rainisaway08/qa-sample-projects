from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait for page to load
time.sleep(1)

# Click on the 'Forgot your password?' link (Assuming there's one)
try:
    forgot_link = driver.find_element(By.LINK_TEXT, "Forgot your password?")
    forgot_link.click()
    time.sleep(2)

    # Check if URL changed or new page is loaded
    current_url = driver.current_url

    if "forgot-password" in current_url or "reset" in current_url:
        print("✅ Forgot password link test passed!")
    else:
        print("❌ Forgot password link test failed — wrong destination.")

except:
    print("⚠️ Forgot password link not found on this page.")

# Cleanup
driver.quit()
