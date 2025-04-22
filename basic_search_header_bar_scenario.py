from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


from selenium.webdriver.chrome.service import service

service= Service(ChromeDriverManager().install())
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture
def setup():

    driver.maximize_window()
    yield driver
    driver.quit()

def test_basic_search_header_bar_scenarios(setup):
    driver.get("https://uat.app.altrrtech.com/")

    time.sleep(7)
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

    time.sleep(6)

    search_box = driver.find_element(by=By.XPATH, value="//*[@class ='ant-input css-1v613y0']")
    search_box.send_keys("pune")

    time.sleep(2)

    search_toggle =driver.find_element(by=By.XPATH, value= "//*[@class='ant-switch-inner']")
    search_toggle.click()

    time.sleep(4)

    search_button =driver.find_element(by=By.XPATH, value= "//button[contains(text(), 'Search')]")
    search_button.click()

    time.sleep(5)


    searchone_toggle =driver.find_element(by=By.XPATH, value = "//*[@class= 'ant-switch-inner']")
    searchone_toggle.click()

    time.sleep(5)

    company_button = driver.find_element(by=By.XPATH, value = "//*[@class ='  radioBtnCustom']")
    company_button.click()

    time.sleep(4)

    Search_box = driver.find_element(by=By.XPATH, value = "//*[@class = 'ant-input css-1v613y0']")
    Search_box.send_keys("Pune")
    Search_box.send_keys(Keys.RETURN)

    time.sleep(6)

    dashbaord_Points_redirection =driver.find_element(by=By.XPATH, value= "//*[@class = 'actions-item headerPointAction']")
    dashbaord_Points_redirection.click()
    time.sleep(2)



    # notification_icon = driver.find_elements(by=By.XPATH, value="//div[@wrap='wrap']//div//div//header//div//div//div//div//div//div//span//img")
    # notification_icon.click()
    #
    # time.sleep(2)
    #
    # my_account= driver.find_element(by=By.XPATH, value= "//*[@class ='ant-progress-inner']")
    # my_account.click()

def second_largest(numbers):
    unique_nums = list(set(numbers))
    unique_nums.sort()
    if len(unique_nums) >= 2:
        return unique_nums[-2]
    else:
        return None

    uni_num = list(set(numbers))
    uni_num.sort()
    if len(uni_num)>= 2:
        return uni_num [-2]


def greater_than_50(lst):
    result = []
    for num in lst:
        if num > 50:
            result.append(num)
    return result


def greater_that_50(lst):
    result =[]
    for num in lst:
        if num > 50:
            result.append(num)
    return result



def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

print(word_frequency("python is fun and python is easy"))


def word_freq(sentence):
    words = sentence.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1

        else:
            freq[word] = 1

    return freq
