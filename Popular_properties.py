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

def test_case_for_commercial_and_residential_popular_properties_flow(setup):

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


    time.sleep(6)

    Popular_properties_commercial =driver.find_element(by=By.XPATH, value="//*[contains(text(), 'One Place Baner Phase Iii')]")
    Popular_properties_commercial.click()

    time.sleep(5)

    connected_card_o_unit_available = driver.find_element(by=By.XPATH, value="//*[contains(text(), '0 Unit Available')]")
    connected_card_o_unit_available.click()

    time.sleep(3)

    back_button_onthe_property_detail= driver.find_element(by=By.XPATH, value="//div[@id='root']//div//div//main//section//div//div//div//div//div//div//h4//strong//div//div//span[@aria-label='left']//*[name()='svg']")

    back_button_onthe_property_detail.click()

    time.sleep(3)

    view_all_transaction = driver.find_element(by=By.XPATH,
                                                          value="//span[contains(text(),'View All Transaction')]")
    view_all_transaction.click()

    time.sleep(4)

    back_button_onthe_transaction_detail_page= driver.find_element(by=By.XPATH, value="//div[@id='root']//div//div//main//section//div//div//div//div//div//div//h4//strong//div//div//span[@aria-label='left']//*[name()='svg']")
    back_button_onthe_transaction_detail_page.click()

    time.sleep(4)

    company_card_detial_page =driver.find_element(by=By.XPATH,value="//*[contains(text(), 'View More Details')]")
    company_card_detial_page.click()

    time.sleep(3)
    reportfolio =driver.find_element(by=By.XPATH, value="//*[contains(text(),'RE Portfolio')]")
    reportfolio.click()

    time.sleep(4)

    back_button_onthe_company_detail_page =driver.find_element(by=By.XPATH, value="//span[@aria-label='left']//*[name()='svg']")
    back_button_onthe_company_detail_page.click()

    time.sleep(5)

    Search_button_on_breadcrumb = driver.find_element(by=By.XPATH, value="//a[normalize-space()='Search']")

    Search_button_on_breadcrumb.click()

    time.sleep(3)

    Residential_to_button = driver.find_element(by=By.XPATH, value="//body/div[@id='root']/div/div/header/div/div/div/button[@role='switch']/span[1]")
    Residential_to_button.click()

    time.sleep(2)

    Popular_properties_residential = driver.find_element(by=By.XPATH,
                                                        value="//*[contains(text(), 'Lake Town Chs')]")
    Popular_properties_residential.click()

    time.sleep(4)






