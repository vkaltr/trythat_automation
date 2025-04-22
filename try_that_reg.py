from multiprocessing.resource_tracker import register

from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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


def test_registration_negative_flow(setup):
    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(8)
    loginelemet = driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    assert loginelemet.text == "Login"

    Registration_button= driver.find_element(by=By.XPATH, value= "//*[@class = 'login-to__register']")
    Registration_button.click()

    time.sleep(3)

    Name_field = driver.find_element(by=By.XPATH, value="//*[@id ='basic_name']")
    Name_field.send_keys("Kadam vipul")

    time.sleep(2)

    dropdown_element =driver.find_element(by=By.CLASS_NAME, value="ant-select-selection-search-input" )
    time.sleep(5)
    dropdown_element.send_keys("315 Work Avenue Pune Spaces Private Limited")
    time.sleep(3)
    dropdown_element.send_keys(Keys.RETURN)
    time.sleep(7)

    # option_element= driver.find_element(by=By.XPATH, value = "//span[@title='315 Work Avenue Pune Spaces Private Limited']")
    # option_element.click()
    # time.sleep(6)
    # dropdown_element.send_keys(Keys.RETURN)
    # time.sleep(10)


    email_field =driver.find_element(by=By.XPATH, value="//*[@id ='basic_email']")
    email_field.send_keys("vipul+9@altrr.in")

    time.sleep(2)

    Mobile_number =driver.find_element(by=By.XPATH, value= "//*[@id='basic_phone']")
    Mobile_number.send_keys("9309797984")

    time.sleep(2)
    Password = driver.find_element(by=By.XPATH, value="//*[@id = 'basic_password']")
    Password.send_keys("Kadam@12345#")

    time.sleep(2)

    reset_password = driver.find_element(by=By.XPATH, value="// *[ @ id = 'basic_confirmPassword']")
    reset_password.send_keys("Kadam@12345#")

    time.sleep(2)

    checkbox = driver.find_element(by=By.XPATH, value= "//*[@id='basic_termsAgree']")

    if not checkbox.is_selected():
        checkbox.click()

    time.sleep(3)

    Submit_button = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit')]")
    Submit_button.click()

    time.sleep(5)

    Onboarding_change_loacatiion = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Change Location')]")
    Onboarding_change_loacatiion.click()

    time.sleep(2)

    Location_dropdown = driver.find_element(by=By.XPATH, value="//input[@role='combobox']")
    Location_dropdown.send_keys("Pune,Maharashtra,india")
    Location_dropdown.send_keys(Keys.RETURN)

    time.sleep(3)

    Lets_start= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Let's Start')]")
    Lets_start.click()

    time.sleep(3)










    # time.sleep(2)
    # dropdown_element.click()
    #
    # time.sleep(3)
    #
    # options = driver.find_elements(By.XPATH, "//span[@class='ant-select-selection-item']")
    #
    # time.sleep(4)
    #
    # # Iterate through options and click the one you want
    # for option in options:
    #     if option.text == "315 Work Avenue Pune Spaces Private Limited":  # Replace with the actual option text
    #         option.click()
    #         break



    # select = Select(dropdown_element)
    #
    # # Select by visible text (the option text displayed to the user)
    # select.select_by_visible_text("Mahle Holding India Private Limited")





