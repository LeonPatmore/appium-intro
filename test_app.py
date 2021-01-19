"""
"""

from driver_setup import driver, whatsapp_driver

SIGN_IK_ID = "com.Testing.karthik.extractionofuserid:id/signin"

WHATSAPP_ACCEPT_ID = "com.whatsapp:id/eula_accept"


_driver = driver
_whatsapp_driver = whatsapp_driver


def test_button(_driver):
    _driver.find_element_by_id(SIGN_IK_ID).click()


def test_whatsapp_signin(_whatsapp_driver):
    _whatsapp_driver.find_element_by_id(WHATSAPP_ACCEPT_ID).click()
    pass


if __name__ == '__main__':
    pass
