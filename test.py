import os

from appium import webdriver


PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))


desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '11.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = PATH('test-app-2.apk')

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


if __name__ == '__main__':
    pass
