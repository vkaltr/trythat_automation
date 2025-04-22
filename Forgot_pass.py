
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def setup():

    driver.maximize_window()
    yield driver
    driver.quit()

def test_case_of_negative_flow_of_password(setup):
    driver.get("https://uat.app.altrrtech.com/")


    time.sleep(6)
    loginelemet= driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    assert loginelemet.text == "Login"

    time.sleep(2)
    mobilefield = driver.find_element(by=By.XPATH, value="//*[@name ='mobile_email']")
    mobilefield.send_keys("7887848378")

    passwordbutton = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Via Password')]")

    passwordbutton.click()

    time.sleep(2)

    forgot_pass = driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'Forgot Password ?')]")
    forgot_pass.click()

    time.sleep(2)

    Registered_number = driver.find_element(by=By.XPATH, value="//*[@id ='basic_mobileNumber']")
    Registered_number.send_keys("7887848378")

    time.sleep(2)

    send_button = driver.find_element(by=By.XPATH, value = "//*[contains(text(),'Send')]")
    send_button.click()

    time.sleep(3)

    Submit_otp_button = driver.find_element(by=By.XPATH, value= "//*[contains(text(),'Submit')]")
    Submit_otp_button.click()

    time.sleep(2)












































































