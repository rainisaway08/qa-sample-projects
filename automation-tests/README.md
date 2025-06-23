# 🤖 Automation Tests

This folder contains basic UI automation test scripts written in Python using Selenium WebDriver.
Each test focuses on common login or form functionality found in web applications.

🛠 Tools & Technologies
🐍 Python

🧪 Selenium WebDriver

🌐 ChromeDriver

⏱️ time module (for basic wait handling)

📑 Test Scripts Included
File Name	Test Description
test_login.py	Valid login using correct credentials
test_invalid_login.py	Invalid login with incorrect password
test_password_masking.py	Ensures password input is masked with asterisks/dots
test_password_mismatch.py	Registration form test for mismatched password confirmation
test_empty_login_fields.py	Attempts login with empty username and password fields
test_forgot_password_link.py	Simulates "Forgot Password" link click and checks redirect

🔎 Note: Some scripts are templates based on typical form behavior and may be adapted to real environments.

🚀 How to Run the Tests
Install Selenium:

bash
Copy
Edit
pip install selenium
Download and match ChromeDriver to your browser version.

Run any test using:

bash
Copy
Edit
python test_login.py
📌 Future Enhancements
Add more test scenarios (e.g., remember me, CAPTCHA handling)
Use unittest or pytest for structured test reporting
Add screenshots on failure
