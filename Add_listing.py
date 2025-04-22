from requests.sessions import preferred_clock
from selenium import webdriver
import time
from datetime import datetime
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

def test_case_for_add_listing_form(setup):
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

    time.sleep(3)


    Sell_button = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Sell / Rent Out')]")
    Sell_button.click()

    time.sleep(1)

    add_list = driver.find_element(by=By.XPATH,
                                   value="//*[@class = 'ant-btn css-m4timi ant-btn-primary listing_form_open_button']")
    add_list.click()

    time.sleep(2)

    listing_the_properties = driver.find_element(by=By.XPATH, value= "//*[@class= 'ant-radio-button-wrapper ant-radio-button-wrapper-in-form-item css-m4timi'][1]")
    listing_the_properties.click()

    time.sleep(2)

    Propertyfor = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Sale')]")
    Propertyfor.click()

    time.sleep(2)

    Propertytype= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Commercial')]")
    Propertytype.click()

    time.sleep(3)

    Go_nextbutton= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Go Next')]")
    Go_nextbutton.click()

    time.sleep(2)

    Building_name= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
    Building_name.send_keys("Vb Capitol")
    Building_name.send_keys(Keys.RETURN)

    time.sleep(2)

    # State= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Select State')]")
    # State.send_keys("Maharashtra")
    # State.send_keys(Keys.RETURN)
    #
    # State.click()
    #
    # time.sleep(1)
    #
    # City_field = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Select City')]")
    # City_field.send_keys("pune")
    # City_field.send_keys(Keys.RETURN)
    #
    # time.sleep(2)
    #
    # Locality_field= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Select Locality')]")
    # Locality_field.send_keys("baner")
    # Locality_field.send_keys(Keys.RETURN)
    #
    # time.sleep(2)
    #
    # latitude= driver.find_element(by=By.ID, value="buildingLatitude")
    # latitude.send_keys("90")
    #
    # time.sleep(2)
    #
    # longitude= driver.find_element(by=By.ID, value="buildingLongitude")
    # longitude.send_keys("90")

    time.sleep(2)

    Unit_type= driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[5]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
    Unit_type.send_keys("2BHK")
    Unit_type.send_keys(Keys.RETURN)

    time.sleep(2)
    Unit_condition = driver.find_element(by=By.XPATH, value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[5]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
    Unit_condition.send_keys("Warmshell")
    Unit_condition.send_keys(Keys.RETURN)
    time.sleep(2)

    Floor_no =driver.find_element(by=By.ID, value="unitFloorNo")
    Floor_no.send_keys("100")

    time.sleep(2)

    Unit_no =driver.find_element(by=By.ID, value="unitNo")
    Unit_no.send_keys("101")

    time.sleep(2)

    Area_type = driver.find_element(by=By.XPATH,
                                         value="/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[6]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/input[1]")
    Area_type.send_keys("Carpet")
    Area_type.send_keys(Keys.RETURN)
    time.sleep(2)

    No_ofrooms = driver.find_element(by=By.ID, value="//body//div//div[@role='tabpanel']//div//div//div//div//div//div//div//div//div//div//div//div[1]//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")
    No_ofrooms.send_keys("5")

    time.sleep(5)

    Capecity = driver.find_element(by=By.ID, value="//body//div//div[@role='tabpanel']//div//div//div//div//div//div//div//div//div//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]")
    Capecity.send_keys("1000")
    time.sleep(2)

    noofrooms= driver.find_element(by=By.ID, value="meetingRoom_0_unitNoRooms")
    noofrooms.send_keys("10")

    time.sleep(2)

    Next_buttonnew= driver.find_element(by=By.XPATH, value= "Go Next")



















