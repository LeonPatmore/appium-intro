"""
"""

import time

import pytest
from appium.webdriver.webdriver import WebDriver

from driver_setup import test_driver, whatsapp_driver

# Test app IDs
SIGN_IK_ID = "com.Testing.karthik.extractionofuserid:id/signin"

# Whatsapp IDs
WHATSAPP_ACCEPT_ID = "com.whatsapp:id/eula_accept"
WHATSAPP_REGISTRATION_COUNTRY = "com.whatsapp:id/registration_country"
WHATSAPP_REGISTRATION_PHONE = "com.whatsapp:id/registration_phone"
WHATSAPP_REGISTRATION_SUBMIT = "com.whatsapp:id/registration_submit"

# Generic IDs
ANDROID_MESSAGE = "android:id/message"

_test_driver = test_driver
_whatsapp_driver = whatsapp_driver


@pytest.fixture(autouse=True)
def reset_driver(request):
    """
    Automatically resets the state of the app between each test.
    """
    for arg in list(request.node.funcargs.values()):
        if isinstance(arg, WebDriver):
            arg.reset()


def test_button(_test_driver):
    _test_driver.find_element_by_id(SIGN_IK_ID).click()


def test_whatsapp_registration_default_country_is_us(_whatsapp_driver):
    _whatsapp_driver.find_element_by_id(WHATSAPP_ACCEPT_ID).click()
    time.sleep(1)
    assert _whatsapp_driver.find_element_by_id(WHATSAPP_REGISTRATION_COUNTRY).text == "United States"


WHATSAPP_WRONG_US_NUMBER_ERROR_TEXT = """The phone number you entered is too short for the country: United States.

Include your area code if you haven't."""


def test_whatsapp_registration_with_invalid_us_phone(_whatsapp_driver):
    _whatsapp_driver.find_element_by_id(WHATSAPP_ACCEPT_ID).click()
    time.sleep(1)
    _whatsapp_driver.find_element_by_id(WHATSAPP_REGISTRATION_PHONE).send_keys("9")

    _whatsapp_driver.find_element_by_id(WHATSAPP_REGISTRATION_SUBMIT).click()

    time.sleep(1)

    assert _whatsapp_driver.find_element_by_id(ANDROID_MESSAGE).text == WHATSAPP_WRONG_US_NUMBER_ERROR_TEXT