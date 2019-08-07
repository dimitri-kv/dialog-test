import random
import string
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def assert_element_exist_by_id():
    def f(driver, id):
        """

        :param driver:
        :param id:
        :return:
        """
        # if driver.find_element(By.ID, id):
        #     return True
        # else:
        #     return False
        try:
            driver.find_element(By.ID, id)
        except NoSuchElementException as exception:
            pytest.fail("Element not found")
            return False
        return True
    return f


@pytest.fixture
def assert_element_exist_by_xpath():
    def f(driver, xpath):
        # if driver.find_element(By.XPATH, xpath):
        #     return True
        # else:
        #     return False
        try:
            driver.find_element(By.XPATH, xpath)
        except NoSuchElementException as exception:
            pytest.fail("Element not found")
            return False
        return True
    return f


@pytest.fixture
def long_string():
    def f(stringLength=256):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(stringLength))
    return f


@pytest.fixture
def enter_credentials_on_login_page_use_enter():
    def f(driver, login, password):
        driver.find_element(By.ID, "authorization_form_login").send_keys(login)
        driver.find_element(By.ID, "authorization_form_pass").send_keys(password)
        driver.find_element(By.ID, "authorization_form_pass").send_keys(Keys.ENTER)
        pass
    return f


@pytest.fixture
def enter_credentials_on_login_page_use_click():
    def f(driver, login, password):
        driver.find_element(By.ID, "authorization_form_login").click()
        driver.find_element(By.ID, "authorization_form_login").send_keys(login)
        driver.find_element(By.ID, "authorization_form_pass").click()
        driver.find_element(By.ID, "authorization_form_pass").send_keys(password)
        driver.find_element(By.ID, "authorization_form_step_1_button").click()
        pass
    return f


@pytest.fixture
def enter_server_use_click():
    def f(driver, server_url):
        driver.find_element(By.ID, "form_setup_endpoint").click()
        driver.find_element(By.ID, "form_setup_endpoint").send_keys(server_url)
        driver.find_element(By.ID, "form_setup_submit").click()
        pass
    return f


@pytest.fixture
def enter_server_use_enter():
    def f(driver, server_url):
        driver.find_element(By.ID, "form_setup_endpoint").send_keys(server_url)
        driver.find_element(By.ID, "form_setup_endpoint").send_keys(Keys.ENTER)
        pass
    return f


from selenium import webdriver
@pytest.fixture
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    # driver = webdriver.Firefox()
    vars = {}
    yield driver
    driver.quit()