from mailcap import subst
from multiprocessing.reduction import duplicate

from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.css import Value
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

def test_property_subscription(setup):
    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(5)
    loginelemet = driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    assert loginelemet.text == "Login"

    time.sleep(6)
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

    time.sleep(6)

    search_box = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input css-1v613y0']")
    search_box.send_keys("Vb Capitol")

    time.sleep(3)

    search_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Search')]")
    search_button.click()
    time.sleep(3)

    # Vbcapitol_poperty= driver.find_element(by=By.XPATH, value= "//span[contains(text(), 'Vb Capitol')]")
    # Vbcapitol_poperty.click()

    time.sleep(4)
    #

    try:
        Subscribe_button = driver.find_element(by=By.XPATH, value= "(//*[contains(text(), 'Subscribe')])[1]")
        Subscribe_button.click()

    except NoSuchElementException:
        print("there is insufficient balance")

    # insufficient_balance = driver.find_element(by=By.XPATH, value="//span[normalize-space()='Oops insufficient points!']")
    #
    # print(insufficient_balance.text)

    #success_message =driver.find_element(by=By.XPATH, value="//span[normalize-space()='Property subscribe successfully!']").text

    time.sleep(5)

    Subscription_menu_nav = driver.find_element(by=By.XPATH, value="//li[@class='ant-menu-item'][6]")
    Subscription_menu_nav.click()

    time.sleep(2)
    try:
        Subscribed_property_name = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Vb Capitol')]")
        Subscribed_property_name.text

    except NoSuchElementException:
        print("there is no such property available due to insufficient balance")

    time.sleep(3)

    Subscription_redirection_arrow =driver.find_element(by=By.XPATH, value="(//span[@class ='ant-btn-icon'])[1]")
    Subscription_redirection_arrow.click()

    time.sleep(2)

    back_button = driver.find_element(by=By.XPATH, value="//div[@class ='title_left']")
    back_button.click()

    time.sleep(5)

    unsubscribe_button = driver.find_element(by=By.XPATH, value= "(//*[@class ='ant-table-cell'])[1]")

    unsubscribe_button.click()

    time.sleep(2)

    Yes_confirm = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Yes, confirm')]")
    Yes_confirm.click()

    time.sleep(3)


































