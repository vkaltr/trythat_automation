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

def test_view_all_transaction_unlock_make_payment_flow(setup):
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

    time.sleep(5)

    search_box = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input css-1v613y0']")
    search_box.send_keys("45 West")

    time.sleep(3)

    search_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Search')]")
    search_button.click()
    time.sleep(3)

    proprtyname= driver.find_element(by=By.XPATH, value= "//span[contains(text(),'45 West')]")
    proprtyname.click()

    time.sleep(5)

    viewalltransaction = driver.find_element(by=By.XPATH, value ="//span[contains(text(), 'View All Transaction')]")
    viewalltransaction.click()

    time.sleep(3)

    transaction_page_redirection = driver.find_element(by=By.XPATH, value= "//div[@class ='custom-data-grid-row'][2]")
    transaction_page_redirection.click()

    time.sleep(5)



    # actions = ActionChains(driver)
    #
    # element_to_hover = driver.find_element(by=By.XPATH, value ="//button[@class= 'unlock-btn']")
    # time.sleep(2)
    #
    # actions.move_to_element(element_to_hover).perform()

    # transaction_unlocking = driver.find_element(by=By.XPATH, value= "//div[@class='lockicon-div-occupant-rent-buyer']//div[@class='lockicon']//*[name()='svg']")
    #
    #
    #
    # # Unlock_button= driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'OK')]")
    # Property_back_button = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'One Place - 07')]")

    # if transaction_unlocking.is_enabled() and transaction_unlocking.is_displayed():
    #     print("The search button is clickable.")
    #     transaction_unlocking.click()
    # else :
    #     print("the button is not clickable")
    #     Property_back_button.click()

    transaction_unlocking = (By.XPATH, "//div[@xpath ='1']")
    Property_back_button = (By.XPATH, "//*[contains(text(), '45 West - 103')]")


    try:
        first_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(transaction_unlocking)
        )


        first_element.click()

        try:
            popup_make_payment = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Make Payment')]")
            popup_make_payment.click()

            my_account = driver.find_element(by=By.XPATH, value="//li[@class='ant-menu-item'][3]")
            my_account.click()

            time.sleep(2)
            wait = WebDriverWait(driver, 10)
            element = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Edit Profile')]")))

            print(element.text)
            personal_details_tabs = driver.find_elements(by=By.XPATH, value="ant-tabs-tab")


            transaction_details = driver.find_element(by=By.XPATH,
                                                      value="//div[contains(text(), 'Transactional Details')]")
            transaction_details.click()


        except NoSuchElementException:
            print("there is balance available")
        print("Clicked on the first element.")


    except:
        print("First element is not clickable. Trying the second element.")


        try:
            second_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Property_back_button)
            )


            second_element.click()
            print("Clicked on the second element.")
        except:
            print("Both elements are not clickable.")

    time.sleep(5)

    max_pages = 2
    current_page = 1

    while current_page <= max_pages:
        print(f"Scraping Page {current_page}")

        try:

            next_button = driver.find_element(By.XPATH, "//li[@title='Next Page']//button[@type='button']")

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

    try:
        popup_make_payment = driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'Make Payment')]")
        popup_make_payment.click()

    except NoSuchElementException:
        print("there is balance available")


    time.sleep(5)

    # viewalltransaction = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'View All Transaction')]")
    # viewalltransaction.click()
    #
    # time.sleep(3)
    #
    # transaction_page_redirection = driver.find_element(by=By.XPATH, value="//td[@class='ant-table-cell ant-table-cell-row-hover']//img[@alt='location']")
    # transaction_page_redirection.click()
    #
    # time.sleep(5)
    #
    # transaction_unlocking = (By.XPATH, "//div[@xpath ='1']")
    # Property_back_button = (By.XPATH, "//*[@style=  'cursor: pointer; vertical-align: middle;']")
    #
    # # Wait for the first element to be clickable
    # try:
    #     first_element = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable(transaction_unlocking)
    #     )
    #
    #     # If the first element is clickable, click it
    #     first_element.click()
    #     print("Clicked on the first element.")
    # except:
    #     print("First element is not clickable. Trying the second element.")














