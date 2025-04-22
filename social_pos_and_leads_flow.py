from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pynput.keyboard import Key,Controller

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


def test_social_post_and_leads_flow(setup):
    driver.get("https://uat.app.altrrtech.com/")


    time.sleep(7)
    loginelemet= driver.find_element(by=By.XPATH, value=("//*[contains(text(), 'Login')]"))

    assert loginelemet.text == "Login"
    time.sleep(2)


    loginbutton = driver.find_element(by=By.XPATH, value="//*[@name ='mobile_email']")
    loginbutton.send_keys("9309797984")

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
    # nav_element = driver.find_elements(by=By.CLASS_NAME,
    #                                    value="ant-menu-item")
    #
    # time.sleep(10)
    #
    # for element in nav_element:
    #     print(element.text)
    #     element.click()
    # Wait for the element to be clickable
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/user/socialApp']")))

    element.click()
    # navigation_social= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Social')]")
    # navigation_social.click()

    time.sleep(4)
    Social_generic_post = driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Generic Post')]")
    Social_generic_post.click()

    time.sleep(3)

    add_posttitle =driver.find_element(by=By.XPATH, value="//*[@id ='post_title']")
    add_posttitle.send_keys("Test Generic post one 12-02")

    time.sleep(3)

    discription_post= driver.find_element(by=By.XPATH, value="//*[@class ='ql-editor ql-blank']")
    discription_post.send_keys("test")

    time.sleep(1)

    Cta_field = driver.find_element(by= By.XPATH, value= "//*[@id = 'cta']")
    Cta_field.send_keys("testcta")

    time.sleep(2)

    link_field = driver.find_element(by=By.XPATH, value="//*[@id ='link']")
    link_field.send_keys("https://four.com")

    time.sleep(2)


    create_post= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Create Post')]")
    create_post.click()

    time.sleep(3)

    Check_added_post= driver.find_element(by=By.XPATH, value="//*[contains(text(), 'Test Generic post one 12-02')]")
    Check_added_post.text

    print(Check_added_post.text)

    time.sleep(3)

    like_post = driver.find_element(by=By.XPATH, value = "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/span[1]/span[1]/*[name()='svg'][1]")
    like_post.click()

    time.sleep(2)

    Comment_icon = driver.find_element(by=By.XPATH, value="//body//div[@id='root']//div[@id='scrolldiv']//div//div//div[1]//div[1]//div[1]//div[3]//div[1]//span[1]//span[2]//*[name()='svg']")
    Comment_icon.click()

    time.sleep(4)

    Add_comment= driver.find_element(by=By.XPATH, value ="//body/div[@id='root']/div[@wrap='wrap']/div/div/main/div/div/div/div/div/div/div/div/div/div[1]/div[2]")
    Add_comment.send_keys("Test social comment")
    Add_comment.send_keys(Keys.RETURN)

    time.sleep(3)

    repost_button = driver.find_element(by=By.XPATH, value= "//span[@class = 'd-flex a-center repost-icon-pos']")
    repost_button.click()

    time.sleep(3)

    repost_button_on_popup =driver.find_element(by=By.XPATH, value="//span[contains(text(), 'Repost')]")
    repost_button_on_popup.click()

    time.sleep(2)

    Save_button = driver.find_element(by=By.XPATH, value= "//span[@class = 'd-flex a-center']")
    Save_button.click()

    time.sleep(2)

    my_account = driver.find_element(by=By.XPATH, value="//li[@class='ant-menu-item'][3]")
    my_account.click()

    time.sleep(5)

    my_post = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'My Posts')]")

    my_post.click()

    time.sleep(2)

    Create_post = driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'Create Posts')]")

    Create_post.click()

    time.sleep(2)

    Saved_post = driver.find_element(by=By.XPATH, value= "//*[contains(text(), 'Saved Posts')]")
    Saved_post.click()

    time.sleep(2)

    # Personal_tabs = driver.find_elements(by=By.CLASS_NAME, value = "ant-tabs-tab-btn")
    #
    # for ptab in Personal_tabs:
    #     ptab.click()
    #     time.sleep(3)
    #     print(ptab.text)

    driver.refresh()

    time.sleep(10)

    My_repostedpost= driver.find_element(by=By.XPATH, value="//body/div/div[@wrap='wrap']/div/div/main/div/div/div/div[@role='tabpanel']/section/div/div/div/div/div/div[@activeaccounttab='personal_details']/div/div/div[@role='tabpanel']/div/div/div/div[1]/div[1]/div[1]/div[2]/span[1]")

    My_repostedpost.click()

    time.sleep(7)

    you_reposted_cross_verify = driver.find_element(by=By.XPATH, value="//*[contains(text(), 'You Reposted')]")
    print(you_reposted_cross_verify.text)

    time.sleep(3)

    social_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/user/socialApp']")))
    social_element.click()

    time.sleep(5)

    social_leads_tabs= driver.find_elements(by=By.CLASS_NAME,value="ant-collapse-header-text")

    for tab in social_leads_tabs:
        tab.click()
        time.sleep(2)
        print(tab.text)

    time.sleep(7)








































