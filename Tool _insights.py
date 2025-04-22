import time


from selenium import webdriver
from collections import Counter
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# from AltrrAutomation.pune_residential_property import driver

@pytest.fixture
def set_up():

    driver.maximize_window()
    yield driver
    driver.quit()



def test_tool_and_insights(set_up):

    driver.maximize_window()

    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(6)

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

    toolsandinsights= driver.find_element(by=By.XPATH, value="//li[@class='ant-menu-item'][5]")
    toolsandinsights.click()

    time.sleep(3)

    # City_anyaletics_tab =driver.find_element(by=By.CLASS_NAME, value="ant-card ant-card-bordered ant-card-hoverable active-card css-1v613y0")
    # City_anyaletics_tab.click()

    # time.sleep(2)

    City_anyaletics_tab = driver.find_element(by=By.XPATH,
                                              value="//body/div[@id='root']/div/div/main/div/div[1]/div[1]/div[1]/div[1]")
    City_anyaletics_tab.click()


    time.sleep(3)

    city_anyaletics = driver.find_element(by=By.XPATH, value="//span[@class = 'ant-select-selection-search']")
    city_anyaletics.click()

    time.sleep(2)
    city_anyaletics = driver.find_element(by=By.XPATH, value="//div[@title='Pune']//div[contains(text(),'Pune')]")
    city_anyaletics.click()

    time.sleep(3)

    Locality_anyaletis_tabs = driver.find_element(by=By.XPATH, value="//body/div[@id='root']/div/div/main/div/div/div/div[2]/div[1]")
    Locality_anyaletis_tabs.click()

    time.sleep(2)

    city_fiels = driver.find_element(by=By.XPATH, value="//span[@class = 'ant-select-selection-search']")
    city_fiels.click()

    time.sleep(3)

    city_anyaletics = driver.find_element(by=By.XPATH, value="//div[@title='Pune']//div[contains(text(),'Pune')]")
    city_anyaletics.click()

    time.sleep(3)

    locality_anyaletics = driver.find_element(by=By.XPATH, value="//span[@class= 'ant-select-selection-placeholder']")
    locality_anyaletics.send_keys("Baner")

    time.sleep(4)


 

















































