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

def test_case_for_random_company_search(setup):

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

    time.sleep(2)

    search_queries = ["Baner"]

    for query in search_queries:
        try:
            search_box = driver.find_element(by=By.XPATH, value= "//*[@class ='ant-input css-m4timi']")
            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)

            search_properties = driver.find_elements(by=By.CLASS_NAME, value="propertyListContainer__div__card__row__col__row__col1__h5")

            for properties in search_properties:
                print(properties.text)


        except Exception as e:
            print(f"Error searching for '{query}': {e}")
    time.sleep(2)

    # element = driver.find_element(by=By.XPATH,
    #                               value="//div[7]//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//div[2]//div[1]//img[1]")
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    # time.sleep(8)


    # company_button =driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Company')]")
    # company_button.click()
    #
    # time.sleep(3)

    company_button = driver.find_element(by=By.XPATH, value="//*[@class ='  radioBtnCustom']")
    company_button.click()

    time.sleep(3)

    Company_search = driver.find_element(by=By.XPATH, value="//input[@placeholder='Search company name...']")
    Company_search.send_keys("efc limited")
    Company_search.send_keys(Keys.RETURN)

    time.sleep(3)

    cards = driver.find_elements(By.CLASS_NAME, "ant-card-body")


    for card in cards:
        Company_title = card.find_element(By.CLASS_NAME, "organizationListContainer__div__card__row__col__row__col1__h5").text  # Get card title
        Company_type = card.find_element(By.CLASS_NAME, "organizationListContainer__div__card__row__col__row__col1__para").text  # Get card price

        print(f"Checking Card: {Company_title} - {Company_type}")

        if "Efc Limited" in Company_title or "Public Limited Company" in Company_type:

            card.click()

            print(f"✅ Found target card: {Company_title} - {Company_type}")
            break

    time.sleep(4)

    company_detail_page = driver.find_element(by=By.XPATH, value="//span[normalize-space()='View More Details']")
    company_detail_page.click()

    time.sleep(2)

    # reportfolio = driver.find_element(by=By.XPATH, value="//*[contains(text(),'RE Portfolio')]")
    # reportfolio.click()


    time.sleep(2)

    Direction_information = driver.find_element(by=By.XPATH, value="//span[contains(text(),'View Directors')]")
    Direction_information.click()

    time.sleep(2)

    Direction_information = driver.find_element(by=By.XPATH, value="//button[@class= 'ant-modal-close']")
    Direction_information.click()

    time.sleep(2)


    company_backbutton = driver.find_element(by=By.XPATH, value="//span[@aria-label='left']//*[name()='svg']")
    company_backbutton.click()

    time.sleep(2)

    shifting_companies = driver.find_elements(by=By.XPATH, value="//li[@class ='ant-list-item'][1]")

    for companies in shifting_companies:
        companies.click()

    time.sleep(3)

    other_suggetionshifting = driver.find_elements(by=By.XPATH,
                                                   value="//div[@class ='d-flex a-center jc-between mt-15 p-10 similarPropertiesHover similar-properies-allignments'][2]")

    for switch in other_suggetionshifting:
        switch.click()

        time.sleep(3)

