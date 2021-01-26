"""
"""

import os

import pytest
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


def _path(file: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file))


def quit_driver(driver):
    driver.quit()


def _start_remote_webdriver(desired_caps: dict) -> WebDriver:
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


@pytest.fixture(scope="session")
def test_driver(request):
    driver = _start_remote_webdriver({
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'Android Emulator',
        'app': _path('apks/test-app.apk')
    })
    request.addfinalizer(lambda: quit_driver(driver))
    return driver


@pytest.fixture(scope="session")
def whatsapp_driver(request):
    driver = _start_remote_webdriver({
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'Android Emulator',
        'noReset': True,
        'appActivity': 'com.whatsapp.HomeActivity',
        'appPackage': 'com.whatsapp',
        'app': _path('apks/WhatsApp.apk')
    })
    request.addfinalizer(lambda: quit_driver(driver))
    return driver


@pytest.fixture(scope="session")
def messenger_driver(request):
    driver = _start_remote_webdriver({
        'platformName': 'Android',
        'platformVersion': '9.0',
        'deviceName': 'Android Emulator',
        'noReset': True,
        'appActivity': 'com.facebook.orca.auth.StartScreenActivity',
        'appPackage': 'com.facebook.orca',
        'app': _path('apks/Messengerx86.apk')
    })
    request.addfinalizer(lambda: quit_driver(driver))
    return driver
