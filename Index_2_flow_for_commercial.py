from ast import Index

from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v129.fetch import fail_request
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


def test_view_commercial_index_2doc_flow(setup):
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

    time.sleep(9)

    search_box = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input css-1v613y0']")
    search_box.send_keys("Vb Capitol")
    search_box.send_keys(Keys.RETURN)

    time.sleep(5)

    # search_button = driver.find_element(by=By.XPATH, value="//*[@class ='listing_form_open_button banner-button]")
    # search_button.click()
    # time.sleep(6)

    proprtyname= driver.find_element(by=By.XPATH, value= "//span[contains(text(), 'Vb Capitol')]")
    proprtyname.click()

    time.sleep(5)

    viewalltransaction = driver.find_element(by=By.XPATH, value ="//span[contains(text(), 'View All Transaction')]")
    viewalltransaction.click()

    time.sleep(4)

    transaction_page_redirection = driver.find_element(by=By.XPATH, value= "//div[@class ='custom-data-grid-row'][2]")
    transaction_page_redirection.click()

    time.sleep(6)

    Index_2 = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'View Index II')]")
    Index_2.click()

    time.sleep(3)
    Confirmation_popup =driver.find_element(by=By.XPATH, value="//*[contains(text(), 'OK')]")
    Confirmation_popup.click()

    time.sleep(2)

    Download_pdf_button =driver.find_element(by=By.XPATH, value ="//span[contains(text(), 'Download PDF')]")
    Download_pdf_button.click()

    time.sleep(30)


# def test_view_index_2_flow_in_case_there_is_balance(setup):
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     import time
#
#     # Initialize WebDriver
#     driver = webdriver.Chrome()
#     driver.get("https://uat.app.trythat.ai/")
#
#     MAX_RETRIES = 3  # Set the max retry attempts
#     retry_count = 0
#
#     while retry_count < MAX_RETRIES:
#         try:
#             urlhitting = driver.get("https://uat.app.trythat.ai/")
#               # Click if found
#             print("Element found and clicked!")
#             break  # Exit loop if successful
#         except:
#             retry_count += 1
#             print(f"Retry {retry_count}/{MAX_RETRIES}: Element not found, retrying...")
#             time.sleep(2)  # Wait before retrying
#
#     if retry_count == MAX_RETRIES:
#         print("Max retries reached. Element not found.")
#
#     driver.quit()
#
#     driver.get("https://uat.app.trythat.ai/")
#
#     time.sleep(8)
#     loginelemet = driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))
#
#     assert loginelemet.text == "Login"
#
#     time.sleep(2)
#     mobile_number = driver.find_element(by=By.XPATH, value="//*[@name ='mobile_email']")
#     mobile_number.send_keys("7887848378")
#
#     time.sleep(2)
#
#     passwordbutton = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Via Password')]")
#
#     passwordbutton.click()
#
#     time.sleep(2)
#
#     passwordfield = driver.find_element(by=By.ID, value='basic_password')
#     passwordfield.send_keys("Kadam@12345")
#
#     time.sleep(2)
#     try:
#         element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit')]")
#         element.click()
#     except NoSuchElementException:
#         print("Element not found. Please check the locator or wait for the element to load.")
#
#     time.sleep(9)
#
#     search_box = driver.find_element(by=By.XPATH, value="//input[@placeholder='Search Property here...']")
#     search_box.send_keys("One West")
#     search_box.send_keys(Keys.RETURN)
#
#     time.sleep(15)
#
#     # search_button = driver.find_element(by=By.XPATH, value="//*[@class ='listing_form_open_button banner-button]")
#     # search_button.click()
#     # time.sleep(6)
#
#     proprtyname = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'One West')]")
#     proprtyname.click()
#
#     time.sleep(10)
#
#     viewalltransaction = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'View All Transaction')]")
#     viewalltransaction.click()
#
#     time.sleep(4)
#
#     transaction_page_redirection = driver.find_element(by=By.XPATH, value="//div[@class ='custom-data-grid-row'][2]")
#     transaction_page_redirection.click()
#
#     time.sleep(6)
#
#
#
#     # Index_2 = (By.XPATH, "//span[contains(text(), 'View Index II')]")
#     # request_button = (By.XPATH, "//main//div[2]//div[1]//button[1]//span[1]")
#
#     # Wait for the first element to be clickable
#     try:
#
#         Index_2 = driver.find_element(By.XPATH, "//span[contains(text(), 'View Index II')]")
#         request_button = driver.find_element (By.XPATH, "//main//div[2]//div[1]//button[1]//span[1]")
#
#         if Index_2.is_enabled():
#             Index_2.click()
#             print("index to button is not clickable")
#             time.sleep(2)
#
#         else:
#             request_button.click()
#             print("there is index is not there we need to request to")
#
#     except :
#         print("the document is aleredy requested")
#
#
#     time.sleep(3)
#     Confirmation_popup = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'OK')]")
#     Confirmation_popup.click()
#
#     time.sleep(2)
#
#     Download_pdf_button = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Download PDF')]")
#     Download_pdf_button.click()
#
#
#
# # def test_view_index_2_flow_of_request_document(setup):
# #     driver.get("https://uat.app.trythat.ai/")
# #
# #     time.sleep(8)
# #     loginelemet = driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))
# #
# #     assert loginelemet.text == "Login"
# #
# #     time.sleep(2)
# #     mobile_number = driver.find_element(by=By.XPATH, value="//*[@name ='mobile_email']")
# #     mobile_number.send_keys("9309797984")
# #
# #     time.sleep(2)
# #
# #     passwordbutton = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Via Password')]")
# #
# #     passwordbutton.click()
# #
# #     time.sleep(2)
# #
# #     passwordfield = driver.find_element(by=By.ID, value='basic_password')
# #     passwordfield.send_keys("Kadam@12345")
# #
# #     time.sleep(2)
# #     try:
# #         element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit')]")
# #         element.click()
# #     except NoSuchElementException:
# #         print("Element not found. Please check the locator or wait for the element to load.")
# #
# #     time.sleep(9)
# #
# #     search_box = driver.find_element(by=By.XPATH, value="//*[@class ='ant-input css-m4timi']")
# #     search_box.send_keys("One West")
# #     search_box.send_keys(Keys.RETURN)
# #
# #     time.sleep(15)
# #
# #     # search_button = driver.find_element(by=By.XPATH, value="//*[@class ='listing_form_open_button banner-button]")
# #     # search_button.click()
# #     # time.sleep(6)
# #
# #     proprtyname = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'One West')]")
# #     proprtyname.click()
# #
# #     time.sleep(10)
# #
# #     viewalltransaction = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'View All Transaction')]")
# #     viewalltransaction.click()
# #
# #     time.sleep(4)
# #
# #     transaction_page_redirection = driver.find_element(by=By.XPATH, value="//div[@class ='custom-data-grid-row'][2]")
# #     transaction_page_redirection.click()
# #
# #     time.sleep(6)
# #
# #     Index_2 = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'View Index II')]")
# #     Index_2.click()
# #
# #     time.sleep(3)
# #     Confirmation_popup = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'OK')]")
# #     Confirmation_popup.click()
# #
# #     time.sleep(2)
# #
# #     Download_pdf_button = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Download PDF')]")
# #     Download_pdf_button.click()















