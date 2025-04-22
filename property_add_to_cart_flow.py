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

def test_proprty_add_to_cart_flow(setup):
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

    time.sleep(7)

    search_box = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input css-1v613y0']")
    search_box.send_keys("Vb Capitol")

    time.sleep(5)

    search_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Search')]")
    search_button.click()
    time.sleep(7)
    #
    # proprtyname= driver.find_element(by=By.XPATH, value= "//span[contains(text(), 'Vb Capitol')]")
    # proprtyname.click()

    # time.sleep(7)

    # unitavaialabe_click = driver.find_element(by=By.XPATH, value="//span[contains(text(), '0 Unit Available')]")
    # unitavaialabe_click.click()
    #
    #
    # time.sleep(3)
    #
    # back_button =driver.find_element(by=By.XPATH, value="//body//div//div//div//main//section//div//div//div//div//div//div//h4//strong//span//span[@aria-label='left']//*[name()='svg']//*[name()='path' and contains(@d,'M724 218.3')]")
    # back_button.click()


    # time.sleep(3)

    add_to_cart_property = driver.find_element(by=By.XPATH, value= "(//div[@class = 'subscribe-section__item subscribe-section__item--bookmark'])[1]")
    add_to_cart_property.click()

    time.sleep(5)

    nav_cart_menu = driver.find_element(by=By.XPATH, value= "//li[@class='ant-menu-item'][4]")
    nav_cart_menu.click()

    time.sleep(4)

    add_to_cart_property_tab =driver.find_element(by=By.XPATH, value= "//div[@id ='rc-tabs-0-tab-2']")
    add_to_cart_property_tab.click()

    time.sleep(2)

    add_to_cart_transaction_tab = driver.find_element(by=By.XPATH, value="//*[@id = 'rc-tabs-0-tab-3']")
    add_to_cart_transaction_tab.click()

    time.sleep(3)

    selected_record_for_unlocking = driver.find_element(by=By.XPATH, value="//span[@aria-describedby=':rjr:']")
    selected_record_for_unlocking.text

    print(selected_record_for_unlocking.text)

    unlocking_record= driver.find_element(by=By.XPATH, value="//td[@class='ant-table-cell ant-table-cell-row-hover']//div[@class='lockicon']//*[name()='svg']")
    unlocking_record.click()


    time.sleep(2)

    My_leads= driver.find_element(by=By.XPATH, value="//li[@class='ant-menu-item'][3]")
    My_leads.click()


    time.sleep(5)

    My_leads_property_tab = driver.find_element(by=By.XPATH, value="//*[@data-node-key= 'Property']")
    My_leads_property_tab.click()

    time.sleep(4)

    My_leads_transaction_tab= driver.find_element(by=By.XPATH, value="//*[@id='rc-tabs-1-tab-Transaction']")
    My_leads_transaction_tab.click()

    time.sleep(4)

    transaction_building_name = driver.find_element(by=By.XPATH,value="//tbody/tr[1]/td[3]/div[1]")
    transaction_building_name.text

    time.sleep(3)

    print(transaction_building_name.text)

    switching_tabs_page = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'For Buyers')]")
    switching_tabs_page.click()








