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

def test_personal_detail_edit_form(setup):
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

    edit_button= driver.find_element(by=By.XPATH, value="//*[contains(text(),'Edit Profile')]")
    edit_button.click()

    time.sleep(3)

    Current_designation = driver.find_element(by=By.ID,value='personalDetails_designation')
    Current_designation.clear()
    Current_designation.send_keys("QA")

    time.sleep(2)

    Last_company_name= driver.find_element(by=By.ID, value="personalDetails_lastCompanyName")
    Last_company_name.clear()

    Last_company_name.send_keys("propvivo")

    time.sleep(3)

    element = driver.find_element(by=By.XPATH,
                                   value="//h1[normalize-space()='My Profile']")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    time.sleep(2)

    Edit_form_save_button = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-form-item editDetails-div css-1v613y0']")
    Edit_form_save_button.click()

    time.sleep(3)









