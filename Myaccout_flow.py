from enum import unique

from selenium import webdriver
import time
import pytest
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

def test_case_For_my_account_flow(setup):
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

    my_account= driver.find_element(by=By.XPATH, value="//li[@class='ant-menu-item'][3]")
    my_account.click()

    time.sleep(4)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Edit Profile')]")))

    print(element.text)
    personal_details_tabs = driver.find_elements(by=By.XPATH, value="ant-tabs-tab")

    for pertabs in personal_details_tabs:
        pertabs.click()
        time.sleep(2)
        print(pertabs.print)
    transaction_details =driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Transactional Details')]")
    transaction_details.click()

    wait = WebDriverWait(driver, 10)
    elementone = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Upgrade Plan')]")))

    # point_usage_details_number2 = driver.find_element(by=By.XPATH, value="//a[contains(text(), '2')]")
    # point_usage_details_number2.click()
    #
    # time.sleep(3)
    #
    # point_usage_details_number3 = driver.find_element(by=By.XPATH, value="//a[contains(text(), '3')]")
    # point_usage_details_number3.click()

    time.sleep(3)

    max_pages = 3
    current_page = 1

    while current_page <= max_pages:

        print(f"Scraping Page {current_page}")

        try:
            next_button = driver.find_element(By.XPATH, "//li[@title='Next Page']//a")

            if next_button.is_enabled():
                next_button.click()
                current_page += 1
                time.sleep(2)
            else:
                print("No more pages or 'Next' button is disabled.")
                break
        except Exception as e:
            print(f"Error: {str(e)}")
            break

    time.sleep(2)






















