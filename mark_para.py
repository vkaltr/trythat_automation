import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Parameterized test with different sets of input values
@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("9309797984", "Kadam@12345", "Login Successful"),   # Valid credentials
        ("admin", "wrongpass", "Invalid Credentials"),  # Wrong password
        ("wronguser", "password123", "Invalid Credentials"),  # Wrong username
        ("", "password123", "Username or Password cannot be empty"),  # Empty username
         # Empty password
        ("9309797984", "Kadam@12345", "Start Your Property Search Here"),  # Both fields empty
    ]
)
def test_addition_form(username, password, expected_message):

    driver.get("https://uat.app.trythat.ai/")  # Replace with actual URL

    time.sleep(6)

    # Locate input fields and button
    username_field = driver.find_element(By.XPATH, "//*[@name ='mobile_email']")
    passwordbutton = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Via Password')]")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']")
    add_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]")

    # result_field = driver.find_element(By.ID, "result")  # Assume result appears here

    # Enter values and submit the form
    # username_field.clear()
    username_field.send_keys(username)
    time.sleep(5)

    passwordbutton.click()

    time.sleep(7)

    # password_field.clear()
    password_field.send_keys(password)
    time.sleep(7)

    add_button.click()

    time.sleep(7)  # Wait for the result to appear

    message = driver.find_element(By.XPATH, "//*[contains(text(), 'Start Your Property Search Here')]").text  # Replace with actual locator
    assert message == expected_message, f"Expected '{expected_message}', but got '{message}'"


    driver.quit()