from appium import webdriver
import os

driver = None

def setup_appium(device_type='android', app=''):
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
        desired_caps['platformName'] = 'android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['fullReset'] = True

        desired_caps['app'] = os.path.realpath(os.path.realpath(__file__) + '/../../') + '/' + app
        desired_caps['newCommandTimeout'] = 1000
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        driver.quit()

    def test_find_elements(self):

        els = self.driver.find_elements_by_xpath('//android.widget.TextView')
        self.assertEqual('API Demos', els[0].text)

        el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Animat")]')
        self.assertEqual('Animation', el.text)

        el = self.driver.find_element_by_accessibility_id("App")
        el.click()

        els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
        # there are more, but at least 10 visible
        self.assertLess(10, len(els))
        # the list includes 2 before the main visible elements
        self.assertEqual('Action Bar', els[2].text)

        els = self.driver.find_elements_by_xpath('//android.widget.TextView')
        self.assertLess(10, len(els))
        self.assertEqual('Action Bar', els[1].text)


