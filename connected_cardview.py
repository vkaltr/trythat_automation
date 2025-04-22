from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.css import Value
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

def test_case_commercial_property_conected_card_view(setup):
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

    search_box = driver.find_element(by=By.XPATH, value="//*[@class= 'ant-input css-1v613y0']")
    search_box.send_keys("Vb Capitol")

    time.sleep(2)

    search_button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Search')]")
    search_button.click()
    time.sleep(3)

    anyproperty_name= driver.find_element(by=By.XPATH, value= "//div//div//div//div//div//div//div//div//div//div//div//div[1]//div[2]//div[1]//div[1]//div[2]//div[1]//div[1]//h5[1]")
    anyproperty_name.click()

    time.sleep(5)
    Unit_available= driver.find_element(by=By.XPATH, value= "//span[contains(text(),'0 Unit Available')]")
    Unit_available.click()

    time.sleep(2)

    listof_occupant= driver.find_element(by=By.XPATH, value= "//span[contains(text(),'List of Occupants')]")
    listof_occupant.click()

    time.sleep(5)


    building_stats_toggle = driver.find_element(by=By.XPATH, value="//body/div[@id='root']/div/div/main/section/div/div/div/div/div/div/div/div/button[@role='switch']/span[1]")
    building_stats_toggle.click()

    time.sleep(9)

    view_anyaleticsscrolling = driver.find_element(by=By.XPATH,
                                     value="//body/div[@id='root']/div/div/main/section/div/div/div/div/div/button[1]")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", view_anyaleticsscrolling)

    view_anyaletics = driver.find_element(by=By.XPATH, value="//body/div[@id='root']/div/div/main/section/div/div/div/div/div/button[1]")
    view_anyaletics.click()

    time.sleep(5)

    back_property_button = driver.find_element(by=By.XPATH, value="//span[@aria-label='left']//*[name()='svg']")
    back_property_button.click()

    # time.sleep(5)//span[contains(text(),"View More Details")]

    wait = WebDriverWait(driver, 10)
    element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'View More Details')]")))

    print(element.text)
    time.sleep(2)

    company_card_viewdetail= driver.find_element(by=By.XPATH, value="//span[contains(text(),'View More Details')]")
    company_card_viewdetail.click()

    time.sleep(3)

    reportfolio= driver.find_element(by=By.XPATH, value="//*[contains(text(),'RE Portfolio')]")
    reportfolio.click()

    time.sleep(2)

    view_report= driver.find_element(by=By.XPATH, value="//span[contains(text(),'View Directors')]")
    view_report.click()

    time.sleep(3)

    close_viewreport= driver.find_element(by=By.XPATH, value="//button[@class= 'ant-modal-close']")
    close_viewreport.click()

    time.sleep(4)

    company_backbutton = driver.find_element(by=By.XPATH, value="//span[@aria-label='left']//*[name()='svg']")
    company_backbutton.click()

    time.sleep(7)

    shifting_companies= driver.find_elements(by=By.XPATH, value="//li[@class ='ant-list-item'][1]")

    for companies in shifting_companies:
        companies.click()

    time.sleep(3)

    other_suggetionshifting = driver.find_elements(by=By.XPATH, value="//div[@class ='d-flex a-center jc-between mt-15 p-10 similarPropertiesHover similar-properies-allignments'][2]")


    for switch in other_suggetionshifting:
        switch.click()

        time.sleep(3)

















