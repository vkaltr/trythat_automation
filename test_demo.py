#
# # from multiprocessing.resource_tracker import register
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
#
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# import pytest
#
# # @pytest.fixture
# @pytest.fixture
# def setup():
#     from selenium.webdriver.support.ui import WebDriverWait
#     driver.maximize_window()
#     driver.implicitly_wait(90)
#
# def test_loginone(setup):
#
#     driver.get("https://uat.app.trythat.ai/")
#     # Search_one = driver.find_element(by=By.NAME, value="q")
#     # Search_one.send_keys("mobile")
#     # driver.implicitly_wait(90)
#     # search_button= driver.find_element(by=By.NAME, value="https://uat.app.trythat.ai/")
#     # search_button.click()
#     email_field = driver.find_element(by=By.NAME, value="mobile_email")
#     email_field.send_keys("vipulkadam.vk9@gmail.com")
#     time.sleep(2)
#     email_field = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Via Password')]")
#     email_field.click()
#     time.sleep(3)
#     pass_field = driver.find_element(by=By.ID, value= "basic_password")
#     pass_field.send_keys("Kadam@12345#")
#     time.sleep(3)
#     Submit_field = driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'Submit')]")
#     Submit_field.click()
#     time.sleep(5)
#
#     # element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Social')]")
#
#     # Conditional logic based on element's attribute
#     # if element.is_displayed():  # Check if the element is visible
#     #     element.click()  # If visible, click the element
#     # else:
#     #     print("Element not visible")
#     from selenium import webdriver
#     from selenium.common.exceptions import ElementClickInterceptedException
#     from selenium.common.exceptions import NoSuchElementException
#
#
#
#     max_attempts = 5
#     attempts = 0
#     element_clicked = False
#
#     while not element_clicked and attempts < max_attempts:
#         try:
#             # Try to click the button
#             button = driver.find_element(by = By.XPATH, value= "//*[contains(text(), 'Search')]")
#             button.click()
#             element_clicked = True
#             print("Button clicked!")
#         except ElementClickInterceptedException:
#             # If the click is blocked, wait and retry
#             print(f"Attempt {attempts + 1}: Button not clickable, retrying...")
#             time.sleep(1)  # Wait 1 second before retrying
#             attempts += 1
#
#     if not element_clicked:
#         print("Button could not be clicked after multiple attempts.")
#
#     time.sleep(2)
#     buttons = driver.find_elements(by=By.XPATH, value="//*[@class = 'ant-menu ant-menu-root ant-menu-vertical ant-menu-dark css-m4timi']" )
#
#     # Iterate over each button and click
#     for button in buttons:
#         if button.is_enabled():
#             button.click()
#
#     try:
#         # Locate the element and get its text
#         element = driver.find_element(by=By.XPATH, value="//*[@class = 'ant-menu ant-menu-root ant-menu-vertical ant-menu-dark css-m4timi']" )
#         actual_text = element.text
#
#         # Verify if the element text matches the expected value
#         expected_text = "Welcome to Example!"
#         if actual_text == expected_text:
#             print("Text verification passed.")
#         else:
#             print(f"Text verification failed. Found: {actual_text}")
#
#     except NoSuchElementException:
#         print("The element was not found on the page.")
#
#     time.sleep(4)
#
#     # Wait until the element is clickable
#     # element = WebDriverWait(driver, 10).until(
#     #     EC.element_to_be_clickable((By.XPATH,"//*[contains(text(), 'Search')]" ))
#     # )
#     #
#     # element.click()
#
# @pytest.mark.skip(reason="Skipping this test temporarily")
# def test_registration_negative(setup):
#
#     driver.get("https://uat.app.trythat.ai/")
#     # driver.implicitly_wait(90)
#
#     register = driver.find_element(by=By.XPATH, value="//a[@href='/register']")
#     register.click()
#     time.sleep(2)
#     # frame_element = driver.find_element(by=By.CSS_SELECTOR, value="//*[@class = 'registrationcard-box']")
#     # driver.switch_to.frame(frame_element)
#     Target_element = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Login via Linkedin')]")
#     time.sleep(2)
#     scroll_to_element = driver.execute_script("arguments[0].scrollIntoView(true);", Target_element)
#
#     time.sleep(3)
#
#     checkbox = driver.find_element(by=By.XPATH,
#                                    value="//*[@id='basic_termsAgree']")
#     time.sleep(2)
#     if not checkbox.is_selected():
#         # If the checkbox is not selected, click it to select
#         checkbox.click()
#
#     submit_button = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Submit')]")
#     submit_button.click()
# @pytest.mark.skip(reason="Skipping this test temporarily")
# def test_loginpositive(setup):
#     driver.get("https://uat.app.trythat.ai/")
#     # Search_one = driver.find_element(by=By.NAME, value="q")
#     # Search_one.send_keys("mobile")
#     # driver.implicitly_wait(90)
#     # search_button= driver.find_element(by=By.NAME, value="https://uat.app.trythat.ai/")
#     # search_button.click()
#     email_field = driver.find_element(by=By.NAME, value="mobile_email")
#     email_field.send_keys("gvgsvdjvsc")
#     time.sleep(2)
#     email_field = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Via Password')]")
#     email_field.click()
#     time.sleep(3)
