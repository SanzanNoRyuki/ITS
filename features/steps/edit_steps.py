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


@given('the logged customer is at the My Account page')
def step_impl(context):
    pass


@when('the customer clicks on the "Edit Account"')
def step_impl(context):
    pass


@then('the customer is taken to his edit page')
def step_impl(context):
    pass


@given('the customer is at his edit page')
def step_impl(context):
    pass


@when('the customer enters new "E-mail"')
def step_impl(context):
    pass


@when('the customer clicks on the "Continue"')
def step_impl(context):
    pass


@then('the customer "E-mail" is changed')
def step_impl(context):
    pass


@given('the customer has edited his "E-mail"')
def step_impl(context):
    pass


@when('the customer tries to login with an "Old E-mail"')
def step_impl(context):
    pass


@then('the customer access is denied')
def step_impl(context):
    pass
