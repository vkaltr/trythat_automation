from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



from selenium.webdriver.chrome.service import Service
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

def test_case_for_store_flow(setup):

    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(4)
    loginelemet= driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    assert loginelemet.text == "Login"

    time.sleep(2)
    mobile_number = driver.find_element(by=By.XPATH, value="//*[@name ='mobile_email']")
    mobile_number.send_keys("9309797984")

    time.sleep(2)

    passwordbutton= driver.find_element(by=By.XPATH, value ="//*[contains(text(), 'Via Password')]")

    passwordbutton.click()

    time.sleep(2)

    passwordfield = driver.find_element(by=By.ID, value='basic_password')
    passwordfield.send_keys("Kadam@12345")


    time.sleep(2)
    try:
        element = driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'Submit')]" )
        element.click()
    except NoSuchElementException:
        print("Element not found. Please check the locator or wait for the element to load.")

    time.sleep(5)

    store_icon = driver.find_element(by=By.XPATH, value= "//*[@class = 'ant-progress-inner']")
    store_icon.click()

    time.sleep(2)

    Store_button_click_action = driver.find_element(by=By.XPATH, value="//body/div/div/ul[@role='menu']/li[2]/span[1]")
    Store_button_click_action.click()

    time.sleep(2)

    Point_add_button = driver.find_element(by=By.XPATH, value="//span[@aria-label='plus']//*[name()='svg']")
    Point_add_button.click()

    time.sleep(2)

    make_payment = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Make Payment')]")
    make_payment.click()

    time.sleep(6)


    close_popup = driver.find_element(by=By.XPATH, value="//*[@stroke = 'currentColor']")
    close_popup.click()

    time.sleep(3)

    # Popup_yes_button =driver.find_element(by=By.XPATH, value="//button[normalize-space()='Yes, exit']")
    # Popup_yes_button.click()
    #
    # time.sleep(4)


