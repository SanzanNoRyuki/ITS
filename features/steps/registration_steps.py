# -- AUTHOR: Roman Fulla <xfulla00>

from behave import *
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import re

# driver = webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)
driver = webdriver.Firefox(executable_path=r'D:\Roman\Cloud\UNDERCONSTRUCTION\ITS\geckodriver.exe')
fail_email = "regfail@test.com"
succ_email = "regsucc6@test.com"


@given("the customer is at the shop homepage")
def step_impl(context):
    pass


@when('the customer clicks on the "My Account"')
def step_impl(context):
    pass


@then("My Account dropdown menu unfolds")
def step_impl(context):
    pass


@given("the customer isn't logged in")
def step_impl(context):
    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/account")
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/login"


@when('the customer clicks on the "Register"')
def step_impl(context):
    driver.set_window_size(1936, 1056)
    driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    driver.find_element(By.LINK_TEXT, "Register").click()


@then('the customer is taken to the registration formular')
def step_impl(context):
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/register"


@given('the customer is at the registration formular page')
def step_impl(context):
    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/register")
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/register"


@when('the customer fills in every required field except the "City"')
def step_impl(context):
    driver.set_window_size(1936, 1056)
    driver.find_element(By.ID, "input-firstname").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Test")
    driver.find_element(By.ID, "input-lastname").click()
    driver.find_element(By.ID, "input-lastname").send_keys("Test")
    driver.find_element(By.ID, "input-email").click()
    driver.find_element(By.ID, "input-email").send_keys(fail_email)
    driver.find_element(By.ID, "input-telephone").click()
    driver.find_element(By.ID, "input-telephone").send_keys("+420 000 000 000")
    driver.find_element(By.ID, "input-address-1").click()
    driver.find_element(By.ID, "input-address-1").send_keys("Test")
    # driver.find_element(By.ID, "input-city").click()
    # driver.find_element(By.ID, "input-city").send_keys("Test")
    driver.find_element(By.ID, "input-country").click()
    dropdown = driver.find_element(By.ID, "input-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Slovak Republic']").click()
    driver.find_element(By.CSS_SELECTOR, "option:nth-child(201)").click()
    driver.execute_script("window.scrollTo(0,340)")
    driver.find_element(By.ID, "input-zone").click()
    dropdown = driver.find_element(By.ID, "input-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Žilinský']").click()
    driver.find_element(By.CSS_SELECTOR, "#input-zone > option:nth-child(9)").click()
    driver.find_element(By.ID, "input-password").click()
    driver.find_element(By.ID, "input-password").send_keys("test")
    driver.find_element(By.ID, "input-confirm").click()
    driver.find_element(By.ID, "input-confirm").send_keys("test")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@then('registration is unsuccesful')
def step_impl(context):
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/register"


@given("the customer is again at the registration formular page")
def step_impl(context):
    pass


@when('the customer fills in every required field but the "Telephone" is misspelled')
def step_impl(context):
    pass


@then("registration isn't succesful")
def step_impl(context):
    pass


@given('the customer is once again at the registration formular page')
def step_impl(context):
    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/register")
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/register"


@when('the customer fills in every required field correctly')
def step_impl(context):
    driver.set_window_size(1936, 1056)
    driver.find_element(By.ID, "input-firstname").click()
    driver.find_element(By.ID, "input-firstname").send_keys("Test")
    driver.find_element(By.ID, "input-lastname").click()
    driver.find_element(By.ID, "input-lastname").send_keys("Test")
    driver.find_element(By.ID, "input-email").click()
    driver.find_element(By.ID, "input-email").send_keys(succ_email)
    driver.find_element(By.ID, "input-telephone").click()
    driver.find_element(By.ID, "input-telephone").send_keys("+420 000 000 000")
    driver.find_element(By.ID, "input-address-1").click()
    driver.find_element(By.ID, "input-address-1").send_keys("Test")
    driver.find_element(By.ID, "input-city").click()
    driver.find_element(By.ID, "input-city").send_keys("Test")
    driver.find_element(By.ID, "input-country").click()
    dropdown = driver.find_element(By.ID, "input-country")
    dropdown.find_element(By.XPATH, "//option[. = 'Slovak Republic']").click()
    driver.find_element(By.CSS_SELECTOR, "option:nth-child(201)").click()
    driver.execute_script("window.scrollTo(0,340)")
    driver.find_element(By.ID, "input-zone").click()
    dropdown = driver.find_element(By.ID, "input-zone")
    dropdown.find_element(By.XPATH, "//option[. = 'Žilinský']").click()
    driver.find_element(By.CSS_SELECTOR, "#input-zone > option:nth-child(9)").click()
    driver.find_element(By.ID, "input-password").click()
    driver.find_element(By.ID, "input-password").send_keys("test")
    driver.find_element(By.ID, "input-confirm").click()
    driver.find_element(By.ID, "input-confirm").send_keys("test")
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()


@then('registration is succesful')
def step_impl(context):
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/success"


@given("the customer is at the registration formular page once more")
def step_impl(context):
    pass


@when('the customer fills in every required field but the "E-mail" is already in use')
def step_impl(context):
    pass


@then("Then registration is not succesful")
def step_impl(context):
    pass
