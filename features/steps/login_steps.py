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


@given('the customer is at the store homepage')
def step_impl(context):
    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/account")
    sleep(.5)
    if driver.current_url != "http://mys01.fit.vutbr.cz:8027/index.php?route=account/login":
        driver.set_window_size(1936, 1056)
        driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=common/home")


@when('the customer clicks on the "Login"')
def step_impl(context):
    driver.set_window_size(1936, 1056)
    driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    driver.find_element(By.LINK_TEXT, "Login").click()


@then('the customer is taken to the login page')
def step_impl(context):
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/login"


@given('the customer is at the login page')
def step_impl(context):
    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/account")
    sleep(.5)
    if driver.current_url != "http://mys01.fit.vutbr.cz:8027/index.php?route=account/login":
        driver.set_window_size(1936, 1056)
        driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/login")


@when('the customer fills in incorrect informations')
def step_impl(context):
    driver.set_window_size(1936, 1056)
    driver.find_element(By.ID, "input-email").click()
    driver.find_element(By.ID, "input-email").send_keys(fail_email)
    driver.find_element(By.ID, "input-password").click()
    driver.find_element(By.ID, "input-password").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()


@then('the customer has denied access')
def step_impl(context):
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/login"


@given('the customer already has an account')
def step_impl(context):
    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/register")
    sleep(.5)
    if driver.current_url != "http://mys01.fit.vutbr.cz:8027/index.php?route=account/register":
        driver.set_window_size(1936, 1056)
        driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/register")

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

    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/account")
    sleep(.5)
    if driver.current_url != "http://mys01.fit.vutbr.cz:8027/index.php?route=account/login":
        driver.set_window_size(1936, 1056)
        driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/login")


@when('the customer fills in correct informations')
def step_impl(context):
    driver.set_window_size(1936, 1056)
    driver.find_element(By.ID, "input-email").click()
    driver.find_element(By.ID, "input-email").send_keys(succ_email)
    driver.find_element(By.ID, "input-password").click()
    driver.find_element(By.ID, "input-password").send_keys("test")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(3)").click()


@then('the customer is successfully logged in')
def step_impl(context):
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/account"


@given('the customer is logged in')
def step_impl(context):
    driver.get("http://mys01.fit.vutbr.cz:8027/index.php?route=account/account")
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/account"


@when('the customer clicks on the "Logout"')
def step_impl(context):
    driver.set_window_size(1936, 1056)
    driver.find_element(By.CSS_SELECTOR, ".dropdown .hidden-xs").click()
    driver.find_element(By.LINK_TEXT, "Logout").click()


@then('the customer is logged out')
def step_impl(context):
    sleep(.5)
    assert driver.current_url == "http://mys01.fit.vutbr.cz:8027/index.php?route=account/logout"
