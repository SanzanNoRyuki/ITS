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


@given('the logged customer is at the checkout')
def step_impl(context):
    pass


@when('the customer wants to use an existing address')
def step_impl(context):
    pass


@then('"Billing Details" are automatically filled in')
def step_impl(context):
    pass
