from webbrowser import open_new

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

def test_case_of_basic_search_flow_with_different_search_inputs(setup):

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

    time.sleep(4)

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
    time.sleep(5)

    # element = driver.find_element(by=By.XPATH,
    #                               value="//div[7]//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//div[2]//div[1]//img[1]")
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    # time.sleep(8)

    # elementone = driver.find_element(by=By.XPATH,
    #                               value="//div[55]//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//div[1]//div[1]//img[1]")
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elementone)
    # time.sleep(20)
    search_queries = ["One West", "45 West"]

    time.sleep(8)

    for query in search_queries:
        try:

            search_box = driver.find_element(by=By.XPATH, value="//input[@placeholder  = 'Show me properties in Hinjewadi']")
            time.sleep(2)

            search_properties = driver.find_elements(by=By.CLASS_NAME,
                                                     value="propertyListContainer__div__card__row__col__row__col1__h5")

            for properties in search_properties:
                print(properties.text)

            time.sleep(10)

            search_box_cross_button= driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input-suffix']")
            search_box_cross_button.click()


            time.sleep(5)


            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)

            time.sleep(5)

            # results = driver.find_elements(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > main:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)")
            # if results:
            #     print(f"Search results for '{query}': {results[0].text}")
            # else:
            #     print(f"No results found for '{query}'")

            time.sleep(10)

        except Exception as e:
            print(f"Error searching for '{query}': {e}")

    time.sleep(5)

    driver.quit()
    time.sleep(70)

def test_search_result_with_pune_baner(setup):

    time.sleep(3)
    driver.get("https://uat.app.trythat.ai/")

    time.sleep(6)
    loginelemet = driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    time.sleep(3)
    assert loginelemet.text == "Login"

    time.sleep(7)
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


    search_queries = ["Baner"]

    for query in search_queries:
        try:

            search_box = driver.find_element(by=By.XPATH, value="//input[@placeholder  = 'Search Property...']")


            search_box.clear()
            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)


            time.sleep(4)



        except Exception as e:
            print(f"Error searching for '{query}': {e}")
    time.sleep(10)

    filter_icon = driver.find_element(by=By.XPATH, value="//span[@class='ant-btn-icon']")
    filter_icon.click()

    time.sleep(2)
    filter_window = driver.find_element(by=By.XPATH, value="ant-popover-inner-content")
    time.sleep(2)
    city_field = driver.find_element(by=By.XPATH, value = "//input[@id='rc_select_5']")
    city_field.send_keys("Pune")
    city_field.send_keys(Keys.RETURN)

    time.sleep(3)

    Locality_field = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Select Locality')]")
    Locality_field.send_keys("baner")
    Locality_field.send_keys(Keys.RETURN)

    time.sleep(2)






