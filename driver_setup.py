"""
"""

import os

import pytest
from appium import webdriver


def _path(file: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file))


def quit_driver(driver):
    driver.quit()


@pytest.fixture(scope="session")
def test_driver(request):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'Android Emulator',
        'app': _path('apks/test-app.apk')}

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.addfinalizer(lambda: quit_driver(driver))
    return driver


@pytest.fixture(scope="session")
def whatsapp_driver(request):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'Android Emulator',
        'noReset': True,
        'appActivity': 'com.whatsapp.HomeActivity',
        'appPackage': 'com.whatsapp',
        'app': _path('apks/WhatsApp.apk')}

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    request.addfinalizer(lambda: quit_driver(driver))
    return driver
