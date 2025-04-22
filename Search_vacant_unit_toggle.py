from ast import Index

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

@pytest.fixture
def setup():

    driver.maximize_window()
    yield driver
    driver.quit()

def test_view_for_vacant_unit_toggle(setup):
    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(5)
    loginelemet = driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    assert loginelemet.text == "Login"

    time.sleep(2)
    mobile_number = driver.find_element(by=By.XPATH, value="//*[@name ='mobile_email']")
    mobile_number.send_keys("9309797984")

    time.sleep(2)

    passwordbutton = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Via Password')]")

    passwordbutton.click()

    time.sleep(2)

    passwordfield = driver.find_element(by=By.ID, value='basic_password')
    passwordfield.send_keys("Kadam@12345")

    time.sleep(2)
    try:
        element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit')]")
        element.click()
    except NoSuchElementException:
        print("Element not found. Please check the locator or wait for the element to load.")

    time.sleep(5)

    search_box = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input css-1v613y0']")
    search_box.send_keys("Baner")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    # search_button = driver.find_element(by=By.XPATH, value="//*[@class ='listing_form_open_button banner-button]")
    # search_button.click()
    # time.sleep(6)

    Only_vacant_unit_toggleon=driver.find_element(by=By.XPATH, value="//body/div/div/div/main/div/div/div/div/div/div/div/button[@role='switch']/span[1]")
    Only_vacant_unit_toggleon.click()

    time.sleep(2)

    Only_vacant_unit_toggleoff =driver.find_element(by=By.XPATH, value= "//body/div/div/div/main/div/div/div/div/div/div/div/button[@role='switch']/span[1]")
    Only_vacant_unit_toggleoff.click()


    time.sleep(3)



