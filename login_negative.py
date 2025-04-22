from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException

@pytest.fixture
def setup():

    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_negative_flow(setup):
    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(5)
    loginelemet = driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    assert loginelemet.text == "Login"

    time.sleep(2)

    mobile_number = driver.find_element(by=By.XPATH, value="//*[@name ='mobile_email']")

    mobile_number.send_keys("9309797984")

    time.sleep(4)

    try:
        passwordbutton = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Via Password')]")

        if passwordbutton.is_enabled():
           passwordbutton.click()

        else:
           print("password button is not clickable")

    except:
        print("e")

    time.sleep(3)

    passwordfield = driver.find_element(by=By.ID, value='basic_password')
    passwordfield.send_keys("Kadam@")

    time.sleep(2)

    element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit')]")
    element.click()

    time.sleep(3)


    try:
        incorrect_massage = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Invalid credentials']")
        incorrect_massage.is_displayed()
        print(" negative scenario is done, the user have added incorrect password in password field")

        assert incorrect_massage.text == "Invalid credentials"

    except NoSuchElementException:
        print("user have added incorrect password.")

    time.sleep(6)




































       # mobile_number.send_keys(Keys.CONTROL + "a")
       # mobile_number.send_keys(Keys.BACKSPACE)
       #
       #  # Now enter new text
       #
       # mobile_number.send_keys("7887848378")

    # Select all text (Ctrl + A) and delete (Backspace)


    # time.sleep(2)
    #
    # try:
    #     passwordbutton = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Via Password')]")
    #     #
    #
    #     if passwordbutton.is_enabled():
    #         passwordbutton.click()
    #         print("password is added")
    #
    #         time.sleep(2)
    #         passwordfield = driver.find_element(by=By.ID, value='basic_password')
    #         passwordfield.send_keys("Vipul")
    #
    #
    # except ElementClickInterceptedException:
    #     print("inccorect email added")
    #
    #
    # time.sleep(2)
    # try:
    #
    #     element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit')]")
    #     if element.is_enabled():
    #        element.click()
    # except NoSuchElementException:
    #     print("Element not found. Please check the locator or wait for the element to load.")
    #
    # time.sleep(3)
    #
    # #
    #
    # try:
    #     # Find username and password fields
    #     username_field = driver.find_element(By.ID, "username")
    #     password_field = driver.find_element(By.ID, "password")
    #
    #
    #     # If fields exist, enter data
    #     if username_field.is_displayed():
    #         username_field.send_keys("00000000")
    #
    #
    #
    #         # Check for error message
    #         try:
    #             driver.find_element(By.ID, "login-button").click()
    #             if "Invalid" in error_msg:
    #                 print("✅ Test Passed: Invalid credentials error displayed.")
    #             else:
    #                 print("⚠️ Unexpected error message:", error_msg)
    #         except NoSuchElementException:
    #             print("❌ Test Failed: No error message found!")
    #
    #     else:
    #         print("❌ Test Failed: Login fields are not visible!")
    #
    # except NoSuchElementException as e:
    #     print(f"❌ Exception Occurred: {e}")
    #
    # finally:
    #     driver.quit()







