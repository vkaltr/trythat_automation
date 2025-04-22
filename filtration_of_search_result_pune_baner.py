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


def test_filtration_of_search_result_pune_baner(setup):

    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(3)
    loginelemet = driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    time.sleep(3)
    assert loginelemet.text == "Login"

    time.sleep(4)
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

    search_queries = ["one"]

    for query in search_queries:
        try:

            search_box = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input css-1v613y0']")

            search_box.clear()

            search_box.send_keys(query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(4)

        except Exception as e:
            print(f"Error searching for '{query}': {e}")
    time.sleep(5)

    filter_icon = driver.find_element(by=By.XPATH, value="//span[@class='ant-btn-icon']")
    filter_icon.click()

    time.sleep(2)
    filter_window = driver.find_element(by=By.XPATH, value="//body/div/div/div/div[@id='filter-popover']/div[1]")
    # time.sleep(2)
    # city_field = driver.find_element(by=By.XPATH, value="//*[@id= 'rc_select_0']")
    # city_field.send_keys("pune")
    # city_field.send_keys(Keys.RETURN)

    time.sleep(3)

    Locality_field = driver.find_element(by=By.XPATH, value="//*[@id ='rc_select_1']")
    Locality_field.send_keys("baner")
    Locality_field.send_keys(Keys.RETURN)

    time.sleep(3)

    # elementapply = driver.find_element(by=By.XPATH,
    #                               value="//*[contains(text(), 'Apply')]")
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elementapply)

    button =driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'Apply')]")

    if button.is_enabled():
        print("Button is enabled, clicking it.")
        button.click()
    else:
        print("Button is disabled.")

    time.sleep(2)

    # scroll_to_element = driver.find_element(by=By.XPATH,
    #                               value="//h5[contains(text(), 'The Kode')]")
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroll_to_element)
    #
    # time.sleep(5)
    #
    # scroll_to_element = driver.find_element(by=By.XPATH,
    #                                         value="//h5[contains(text(), 'Shri Residency')]")
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroll_to_element)
    #
    # time.sleep(5)
    #
    # scroll_to_element = driver.find_element(by=By.XPATH,
    #                                         value="//h5[contains(text(), 'Galaxy')]")
    # driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", scroll_to_element)
    #
    # time.sleep(5)

    searched_cards = driver.find_elements(by=By.CLASS_NAME, value= 'propertyListContainer__div__card__row__col__row__col1__h5')

    for card in searched_cards:
        print(card.text)

    time.sleep(10)

    Residential_toggle = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-switch-inner']")
    Residential_toggle.click()

    time.sleep(4)











