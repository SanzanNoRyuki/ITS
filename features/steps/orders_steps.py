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


@given('the customer is logged in his account')
def step_impl(context):
    pass


@when('the customer places an order')
def step_impl(context):
    pass


@then('Order History contains this order')
def step_impl(context):
    pass


@given('the logged customer has placed an order')
def step_impl(context):
    pass


@when('the customer clicks on the "View" next to order')
def step_impl(context):
    pass


@then('the order information is displayed')
def step_impl(context):
    pass
