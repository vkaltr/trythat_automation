from requests.compat import builtin_str
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

def test_cases_building_compaire_flow(setup):
    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(4)
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


    time.sleep(7)

    search_box = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input css-1v613y0']")
    search_box.send_keys("Square")

    time.sleep(4)

    search_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Search')]")
    search_button.click()
    time.sleep(7)

    proprtyname= driver.find_element(by=By.XPATH, value= "//span[contains(text(), 'Square')]")

    proprtyname.click()


    time.sleep(5)

    add_to_cart_property = driver.find_element(by=By.XPATH, value= "//*[@class = 'bookmarkClickable']")
    add_to_cart_property.click()

    time.sleep(5)

    nav_cart_menu = driver.find_element(by=By.XPATH, value= "//li[@class='ant-menu-item'][4]")
    nav_cart_menu.click()

    time.sleep(4)

    add_to_cart_property_tab =driver.find_element(by=By.XPATH, value= "//div[@id ='rc-tabs-0-tab-2']")
    add_to_cart_property_tab.click()

    time.sleep(3)

    building_compaire = driver.find_element(by=By.XPATH, value ="//div[@class='compare-icon-container']//img[@alt='logo']")
    building_compaire.click()

    time.sleep(3)




