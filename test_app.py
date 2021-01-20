"""
"""
import time

from driver_setup import test_driver, whatsapp_driver

SIGN_IK_ID = "com.Testing.karthik.extractionofuserid:id/signin"

WHATSAPP_ACCEPT_ID = "com.whatsapp:id/eula_accept"
WHATSAPP_REGISTRATION_COUNTRY = "com.whatsapp:id/registration_country"


_test_driver = test_driver
_whatsapp_driver = whatsapp_driver


def test_button(_test_driver):
    _test_driver.find_element_by_id(SIGN_IK_ID).click()


def test_whatsapp_signin(_whatsapp_driver):
    _whatsapp_driver.find_element_by_id(WHATSAPP_ACCEPT_ID).click()
    time.sleep(1)
    assert _whatsapp_driver.find_element_by_id(WHATSAPP_REGISTRATION_COUNTRY).text == "United States"


if __name__ == '__main__':
    pass
