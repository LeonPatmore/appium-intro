"""
"""

import os

import pytest
from appium import webdriver


def _path(file: str) -> str:
    return os.path.abspath(os.path.join(os.path.dirname(__file__), file))


@pytest.fixture(scope="session")
def driver():
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'Android Emulator',
        'app': _path('test-app.apk')}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

