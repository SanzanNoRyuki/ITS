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


@given('the customer has logged in')
def step_impl(context):
    pass


@when('the customer clicks on the "Wish List"')
def step_impl(context):
    pass


@then('the customer is taken to his wishlist')
def step_impl(context):
    pass


@given('the logged customer is at the store home page')
def step_impl(context):
    pass


@when('the customer clicks on the "Canon EOS 5D"')
def step_impl(context):
    pass


@then('"Canon EOS 5D" is added to the customer wishlist')
def step_impl(context):
    pass


@given('the customer has "Canon EOS 5D" in his wishlist')
def step_impl(context):
    pass


@when('the customer clicks on the "Remove" next to the "Canon EOS 5D"')
def step_impl(context):
    pass


@then('"Canon EOS 5D" is removed from the customer wishlist')
def step_impl(context):
    pass


@given('the customer has "iPhone" in his wishlist')
def step_impl(context):
    pass


@when('the customer clicks on the "Add to Cart" next to the "iPhone"')
def step_impl(context):
    pass


@then('"iPhone" is added to the customer shopping cart')
def step_impl(context):
    pass
