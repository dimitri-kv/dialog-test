import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By



def test_positive(
                      driver,
                      assert_element_exist_by_id,
                      assert_element_exist_by_xpath,
                      enter_server_use_enter,
                      enter_credentials_on_login_page_use_enter):
    """enter to correct server with correct credentials"""
    d = driver
    d.get("https://ee.dlg.im/")
    d.implicitly_wait(5)
    enter_server_use_enter(d, "https://dsk.eelab.transmit.im")
    enter_credentials_on_login_page_use_enter(d, "test1", "123456")
    assert assert_element_exist_by_id(d, "sidebar_header_menu")
    assert assert_element_exist_by_xpath(d, "/html/body/div[1]/div/aside/div/header/div[1]/a/div[2]")

@pytest.mark.xfail
@pytest.mark.parametrize("server_url, error_message", [("https://dsk.eelab.transmit.iiiiim", "None"),
                                                           ("", "None"),
                                                           (" ", "None"),
                                                           ("abc://test.t", "None"),
                                                           ])
def test_negative_incorrect_server(
                                       driver,
                                       server_url,
                                       error_message,
                                       enter_server_use_enter,
                                       assert_element_exist_by_xpath,
                                       enter_credentials_on_login_page_use_enter,
                                       assert_element_exist_by_id):
    """enter to incorrect server.
    we will either just reload and dont get login page
    or hangout on credentials send event
    Server selection page bahavior seems nfinised, so tests fails and marked as must-fail
    """
    d = driver
    d.get("https://ee.dlg.im/")
    d.implicitly_wait(5)
    enter_server_use_enter(d, server_url)
    try:
        enter_credentials_on_login_page_use_enter(d, "test1", "123456")
    except NoSuchElementException:
        pytest.fail("Do not get login form")
    assert_element_exist_by_id(d, "sidebar_header_menu")


@pytest.mark.parametrize("login, error_message", [("1234567","Password and login mismatched"),
                                                      ("","Invalid nickname."),
                                                      (" ","Invalid nickname."),
                                                      ("-1","Password and login mismatched")
                                          ])
@pytest.mark.parametrize("password", ["1234567",
                                          "",
                                          " ",
                                          "-1"
                                          ])
def test_negative_incorrect_login_password(
                                               driver,
                                               login,
                                               error_message,
                                               password,
                                               assert_element_exist_by_xpath,
                                               enter_server_use_enter,
                                               enter_credentials_on_login_page_use_enter):
    # driver = driver
    driver.get("https://ee.dlg.im/")
    """we use sleep timeout to avoid crash on page load"""
    driver.implicitly_wait(5)
    enter_server_use_enter(driver, "https://dsk.eelab.transmit.im")
    enter_credentials_on_login_page_use_enter(driver, login, password)
    assert assert_element_exist_by_xpath(driver,
                                             "/html/body/div[1]/div/div[2]/div[1]/form/div/div[2]/div/span")
    assert driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/form/div/div[2]/div/span").text == error_message

    """Enter and login to server tests:"""