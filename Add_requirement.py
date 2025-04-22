from requests.sessions import preferred_clock
from selenium import webdriver
import time
from datetime import datetime
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.css import Value
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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

def test_case_for_requirement_form(setup):
    driver.get("https://uat.app.trythat.ai/")

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

    time.sleep(3)

    my_account= driver.find_element(by=By.XPATH, value="//li[@class='ant-menu-item'][3]")
    my_account.click()
    time.sleep(5)

    my_account = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Requirement')]")
    my_account.click()


    time.sleep(5)

    add_requirement = driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'Add Requirements')]")
    add_requirement.click()

    time.sleep(2)

    listing_property_as_button= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Buy')]")
    listing_property_as_button.click()

    time.sleep(3)

    Add_requirement_button = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Buy')]")
    Add_requirement_button.click()

    time.sleep(2)

    Commercial_button = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Commercial')]")
    Commercial_button.click()

    time.sleep(3)

    officespaces = driver.find_element(by=By.XPATH, value="//*[contains(text(),'Office Spaces')]")
    officespaces.click()

    Go_nextONE = driver.find_element(by=By.XPATH,
                                  value="//span[contains(text(), 'Go next')]")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Go_nextONE)

    time.sleep(2)

    GO_next_button = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Go next')]")
    GO_next_button.click()

    time.sleep(2)

    Looking_for = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Yourself')]")
    Looking_for.click()

    time.sleep(2)

    preferred_city = driver.find_element(by=By.XPATH, value="//*[@id ='unitPreferredCity']")
    preferred_city.send_keys("pune")
    preferred_city.send_keys(Keys.RETURN)

    time.sleep(5)

    preferred_locality = driver.find_element(by=By.XPATH, value="//*[@id = 'unitPreferredLocation']")
    preferred_locality.send_keys("baner")
    preferred_locality.send_keys(Keys.RETURN)

    time.sleep(3)

    Required_carpet_area = driver.find_element(by=By.XPATH, value= "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
    driver.execute_script("arguments[0].click();", Required_carpet_area)


    Required_carpet_area.send_keys("Less Than")
    Required_carpet_area.send_keys(Keys.RETURN)

    # try:
    #     first_element = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable(Required_carpet_area)
    #     )
    #
    #     # If the first element is clickable, click it
    #     first_element.click()
    #     print("Clicked on the first element.")
    # except:
    #     print("First element is not clickable. Trying the second element.")


    # time.sleep(2)  //div[@class='dropdown-menu']//div[contains(text(), 'Option Text')]Text


    time.sleep(3)

    app_carpet_area =driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/input[1]")
    app_carpet_area.send_keys("10000")

    time.sleep(2)

    unit_selection= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[5]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
    unit_selection.send_keys("sq.ft")
    unit_selection.send_keys(Keys.RETURN)

    time.sleep(2)

    Go_next = driver.find_element(by=By.XPATH,
                                  value="//span[contains(text(), 'Go next')]")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", Go_next)

    time.sleep(2)

    Want_possession_around_field= driver.find_element(by=By.XPATH, value="// *[ @ id = 'possessionAround']")

    Want_possession_around_field.send_keys("After")
    Want_possession_around_field.send_keys(Keys.RETURN)

    time.sleep(2)

    today = datetime.today().strftime("%d-%m-%y")


    date_picker = driver.find_element(By.XPATH, "//input[@placeholder='DD-MM-YYYY']")

    date_picker.send_keys(today)
    # date_picker.send_keys(Keys.RETURN)

    time.sleep(7)

    # Want_possession_around_date = driver.find_element(by=By.XPATH, value="//*[@id= 'possessionDate']")
    # Want_possession_around_date.send_keys("19-02-2025")
    # Want_possession_around_field.send_keys(Keys.RETURN)

    # time.sleep(2)

    # date_selection= driver.find_element(by=By.XPATH, value="//*[contains(text(), '19-02-2025')]")
    # date_selection.click()




    GO_next_button= driver.find_element(by=By.XPATH, value= "//span[contains(text(), 'Go next')]")
    GO_next_button.click()

    time.sleep(5)






















