from appium import webdriver
import os

#driver = None
import subprocess32
import sys
import config

def setup_appium_driver(device_type='android', app=''):
    """
    Setup the appium on android and iOS
    :param device_type: type to device : android or ios
    :param app: app location
    :return: driver
    """
    desired_caps = dict()
    if device_type.lower() == "ios":
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.2.1'
        desired_caps['deviceName'] = 'iPhone Simulator'
        desired_caps['udid'] = '09d905a109245efebd23ab741c0900e83769b3ae'
        desired_caps['fullReset'] = True

    if device_type.lower() == "android":
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['fullReset'] = True
        print os.path.realpath(os.path.realpath(__file__))
        desired_caps['app'] = os.path.realpath(os.path.realpath(__file__) + '/../') + '/' + app
        desired_caps['newCommandTimeout'] = 100
        if config.udid == '04b2aec1251fafbb':
            desired_caps['udid'] = config.udid
        #desired_caps['bp'] = '4724'
            driver_address = 'http://localhost:' + config.port + '/wd/hub'
            config.appium_driver = webdriver.Remote(driver_address, desired_caps)
            print desired_caps
        if config.udid == 'emulator-5554':
            desired_caps['udid'] = config.udid
            #desired_caps['bp'] = '5555'
            print desired_caps
            driver_address = 'http://localhost:' + config.port + '/wd/hub'
            config.appium_driver = webdriver.Remote(driver_address, desired_caps)
        print 'driver1'
        print config.appium_driver
        # print 'driver2'
        # print config.appium_driver2


def tearDown_appium_driver():
    config.appium_driver.quit()

# def test_find_elements(self):
#
#     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
#     self.assertEqual('API Demos', els[0].text)
#
#     el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Animat")]')
#     self.assertEqual('Animation', el.text)
#
#     el = self.driver.find_element_by_accessibility_id("App")
#     el.click()
#
#     els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
#     # there are more, but at least 10 visible
#     self.assertLess(10, len(els))
#     # the list includes 2 before the main visible elements
#     self.assertEqual('Action Bar', els[2].text)
#
#     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
#     self.assertLess(10, len(els))
#     self.assertEqual('Action Bar', els[1].text)


def start_appium_session():
    config.appium_session = subprocess32.Popen(['appium','-p', config.port])


def stop_appium_session():
    print config.appium_session
    config.appium_session.terminate()
