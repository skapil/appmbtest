import os
from os.path import expanduser
import re
from appium.webdriver.common.touch_action import TouchAction
import config

__author__ = 'sandesh'
import subprocess32
import time
import random, string


def wifi_off():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am start -n io.appium.settings/.Settings -e wifi off'])


def wifi_on():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am start -n io.appium.settings/.Settings -e wifi on'])


def airplane_mode_off():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'settings put global airplane_mode_on 0'])


def airplane_mode_on():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'settings put global airplane_mode_on 1'])


def bluetooth_toggle():
    subprocess32.call(['adb', '-s', config.udid, 'shell','am start -a android.settings.BLUETOOTH_SETTINGS'])
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])
    subprocess32.call(['adb', '-s', config.udid, 'shell','am start -a android.settings.BLUETOOTH_SETTINGS'])
    time.sleep(2)
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'input', 'keyevent','23'])


def get_package_name():
    app_path = os.getcwd() + '/' + config.app
    temp = subprocess32.check_output(['aapt', 'dump', 'badging', app_path])  # | awk -v FS="'" '/package: name=/{print $2}', 'shell', 'am start -n io.appium.settings/.Settings -e wifi off'])
    app_package = re.search('package: name=\'(.*?)\'\s', temp).group(1)
    config.app_package = app_package


def get_all_packages():
    temp = subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'pm list packages'])
    print temp
    packages = re.findall('package:(.*)', temp)
    for i in packages:
        config.all_packages.append(i.strip())


def bringAppToForeground():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'monkey','-p', config.app_package, '-c', 'android.intent.category.LAUNCHER 1'])


def bringAppToBackground():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'input', 'keyevent', 'KEYCODE_HOME'])
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am', 'kill', config.app_package])


def makeCall():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am start','-a android.intent.action.CALL -d tel:+10000'])


def sendMessage():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am start','-a android.intent.action.SENDTO -d sms:0000 --es sms_body "SMS" --ez exit_on_sent true'])
    time.sleep(1)
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'input', 'keyevent', '22'])
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'input', 'keyevent', '66'])

def sendEmail():
    subprocess32.call(['adb', '-s', config.udid, 'shell', 'am start','-n com.google.android.gm/com.google.android.gm.ComposeActivityGmail -d email:address@destination.com --es subject "Your\ subject\ goes\ here" --es body "Your\ email\ body\ goes\ here"'])


def get_mem_info():
    return subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys', 'meminfo',  config.app_package])


def get_cpu_info():
    return subprocess32.check_output(['adb', '-s', config.udid, 'shell', 'dumpsys', 'cpuinfo', '|', 'grep', config.app_package])


def enter_api_key(api_key):
    api_key = api_key
    editText_api_key = driver.find_element_by_id("api_key")
    editText_api_key.send_keys(api_key)


def enter_secret_key(secret_key):
    driver = config.driver
    secret_key = secret_key
    editText_secret_key = driver.find_element_by_id("secret")
    editText_secret_key.send_keys(secret_key)


def click_start():
    driver = config.driver
    driver.find_element_by_id("session_control").click()


def hide_keyboard():
    driver = config.driver
    try:
        driver.hide_keyboard()
    except:
        pass

def click_restart():
    driver = config.driver
    driver.find_element_by_id("restart_control").click()


def click_restart_25_times():
    driver = config.driver
    i = 0
    while i < 25:
        driver.find_element_by_id("restart_control").click()
        i += 1


def click_end():
    driver = config.driver
    driver.find_element_by_id("end_control").click()


def enter_event(event):
    driver = config.driver
    editText_event = driver.find_element_by_id("event_string")
    editText_event.send_keys(event)


def enter_special_event():
    driver = config.driver
    editText_event = driver.find_element_by_id("event_string")
    event = ''.join(random.choice(string.ascii_letters + string.punctuation.replace('{', '.').replace('[', '.')) for i in range(20))
    print event
    editText_event.send_keys(event)
    return event


def enter_char_max_event():
    driver = config.driver
    editText_event = driver.find_element_by_id("event_string")
    event = ''.join(random.choice(string.ascii_letters) for i in range(3000))
    print event
    editText_event.send_keys(event)
    return event


def click_record():
    driver = config.driver
    driver.find_element_by_id("event_control").click()


def click_record_multiple_times(number):
    driver = config.driver
    i = 0
    while i < number:
        driver.find_element_by_id("event_control").click()
        i += 1
        time.sleep(1)


def click_50_event():
    driver = config.driver
    driver.find_element_by_id("small_mass_control").click()


def click_1000_event():
    driver = config.driver
    driver.find_element_by_id("mass_control").click()


def click_heartbeat_on():
    driver = config.driver
    driver.find_element_by_id("heartbeat_on_control").click()


def click_heartbeat_off():
    driver = config.driver
    driver.find_element_by_id("heartbeat_off_control").click()


def click_forget_id():
    driver = config.driver
    driver.find_element_by_id("forget").click()


def click_destroy_instance():
    driver = config.driver
    driver.find_element_by_id("no_instance").click()


def click_set_age():
    driver = config.driver
    driver.find_element_by_id("set_age").click()


def click_set_gender():
    driver = config.driver
    driver.find_element_by_id("set_gender").click()


def click_test_timeout():
    driver = config.driver
    action = TouchAction(driver)
    ele1 = driver.find_element_by_id("sessionid")
    ele2 = driver.find_element_by_id("no_instance")
    action.press(ele2).move_to(ele1).release().perform()
    driver.find_element_by_id("test_timeout").click()


def click_exit():
    driver = config.driver
    action = TouchAction(driver)
    ele1 = driver.find_element_by_id("sessionid")
    ele2 = driver.find_element_by_id("no_instance")
    action.press(ele2).move_to(ele1).release().perform()
    driver.find_element_by_id("close_control").click()


def change_aifa(driver):
    driver = driver
    driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[4]/android.widget.RelativeLayout[1]").click()
    driver.find_element_by_xpath("//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[2]/android.support.v7.widget.RecyclerView[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]").click()
    try:
        driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.Button[2]").click()
    except:
        pass
    try:
        driver.find_element_by_xpath("//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.Button[2]").click()
    except:
        pass

def get_session_id_text():
    driver = config.driver
    textView_session_id = driver.find_element_by_id("sessionid")
    config_android.session_id = textView_session_id.text
    return config_android.session_id

def get_restart_session_id_text():
    driver = config.driver
    textView_session_id = driver.find_element_by_id("sessionid")
    config_android.session_id_restart = textView_session_id.text
    return config_android.session_id_restart