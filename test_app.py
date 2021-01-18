"""
"""

from driver_setup import driver

SIGN_IK_ID = "com.Testing.karthik.extractionofuserid:id/signin"


_driver = driver


def test_button(_driver):
    _driver.find_element_by_id(SIGN_IK_ID).click()


if __name__ == '__main__':
    pass
